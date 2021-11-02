import qimage2ndarray
from os import path
from pathlib import Path
from cv2 import VideoCapture
import mysql.connector as sql
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QCompleter, QMenu, QAction, QActionGroup, QFileDialog

class CONNECT(QObject):
    
    finishedTransaction = pyqtSignal(object)
    finishedSelect = pyqtSignal(object)
    finishedUpdate = pyqtSignal(object)
    finishedDelete = pyqtSignal(object)

    def __init__(self):

        super(CONNECT, self).__init__()
        self.DATAB = sql.connect(option_files=CREDENTIALS)
        self.CURSOR = self.DATAB.cursor(buffered=True)

    def execute(self, statement, arguments=None, many=0, fetch=0, source=None):
        
        try:
            if many: self.CURSOR.executemany(statement, arguments)
            else: self.CURSOR.execute(statement, arguments)

            if statement.startswith('SELECT'):

                if fetch: return self.CURSOR.fetchall()

                self.finishedSelect.emit(self.CURSOR.fetchall())
                
                return
                
            elif statement.startswith('UPDATE'):

                self.DATAB.commit()
                self.finishedUpdate.emit(source)
                
            elif statement.startswith('DELETE'):

                self.finishedDelete.emit(arguments)

            self.finishedTransaction.emit(1)

        except sql.errors.ProgrammingError as error:
            
            print('Programming', error, statement)
            return

        except sql.errors.DatabaseError as error:

            print('Database', error, statement)
            try: self.reconnect(1)
            except Exception as error:
                print('\tDatabase', error, statement)
            
            return

        except sql.errors.InterfaceError as error:

            print('Interface', error, statement)
            try: self.reconnect(1)
            except Exception as error:
                print('\tInterface', error, statement)

            return
            
        except Exception as error:
        
            print('Error', error)
            return

        return

    def rollback(self): self.DATAB.rollback()

    def reconnect(self, attempts=5, time=6):

        self.DATAB.reconnect(attempts, time)

    def commit(self): self.DATAB.commit()
    
    def rowcount(self): return self.CURSOR.rowcount

    def close(self): self.DATAB.close()

class Completer(QCompleter):

    def __init__(self, model, parent=None):

        super(Completer, self).__init__(model, parent)

        self.setCaseSensitivity(Qt.CaseInsensitive)
        self.setCompletionMode(QCompleter.PopupCompletion)
        self.setWrapAround(False)

    # # Add texts instead of replace
    # def pathFromIndex(self, index):

    #     path = QCompleter.pathFromIndex(self, index)

    #     lst = str(self.widget().text()).split(',')

    #     if len(lst) > 1:
    #         path = '%s, %s' % (','.join(lst[:-1]), path)

    #     return path

    # # Add operator to separate between texts
    # def splitPath(self, path):

    #     path = str(path.split(',')[-1]).lstrip(' ')
        
    #     return [path]
        
def create_submenu(parent, name, items, check=None, get_menu=False):
        
    if name is None: menu = parent
    else: menu = QMenu(name, parent)
    action_group = QActionGroup(menu)

    for num, item in enumerate(items):
        
        action = QAction(item, menu, checkable=True)
        if num == check: action.setChecked(True)
        action_group.triggered.connect(parent.parent().parent().populate)
        action_group.addAction(action)
        menu.addAction(action)

    else:
        if name is not None: parent.addMenu(menu)
        action_group.setExclusive(True)
    
    if get_menu: return action_group, menu
    return action_group

def get_frame(path):

    image = VideoCapture(path).read()[-1]
    if image is None: return QPixmap()
    return qimage2ndarray.array2qimage(image).rgbSwapped()

def remove_redundancies():

    from Webscraping import CONNECT

    MYSQL = CONNECT()  
    SELECT = 'SELECT path, artist, tags FROM imagedata WHERE NOT ISNULL(path)'
    UPDATE = 'UPDATE imagedata SET artist=%s, tags=%s WHERE path=%s'

    for (path, artist, tags,) in MYSQL.execute(SELECT, fetch=1):

        artist = f' {" ".join(set(artist.split()))} '.replace('-', '_')
        tags = f' {" ".join(set(tags.split()))} '.replace('-', '_')
        MYSQL.execute(UPDATE, (artist, tags, path))

    MYSQL.commit()
    MYSQL.close()

def update_autocomplete():

    from pathlib import Path
    from Webscraping import CONNECT

    MYSQL = CONNECT()
    
    artist, tags = MYSQL.execute(
        '''SELECT 
        GROUP_CONCAT(DISTINCT artist ORDER BY artist SEPARATOR ""), 
        GROUP_CONCAT(DISTINCT tags ORDER BY tags SEPARATOR "") 
        FROM imagedata''',
        fetch=1)[0]
    text = (
        ' '.join(sorted(set(artist.split()))), 
        ' '.join(sorted(set(tags.split())))
        )
    text = ('\n'.join(text)).encode('ascii', 'ignore')
    Path(r'GUI\autocomplete.txt').write_text(text.decode())
    
    MYSQL.close()

def copy_to(widget, images, sym=False):

        paths = [
            Path(index.data(Qt.UserRole)[0])
            for index in images
            if index.data(300) is not None
            ]
            
        folder = Path(QFileDialog.getExistingDirectory(
            widget, 'Open Directory', str(PATH.parent),
            QFileDialog.ShowDirsOnly
            ))

        for path in paths:

            name = folder / path.name
            if sym and not name.exists(): name.symlink_to(path)
            else: name.write_bytes(path.read_bytes())

BATCH = 10000
CREDENTIALS = r'GUI\credentials.ini'
AUTOCOMPLETE = r'GUI\autocomplete.txt'

ROOT = Path(Path().cwd().drive)
PATH = ROOT / path.expandvars(r'\Users\$USERNAME\Dropbox\ん')
parts = ", ".join([f"'{part}'" for part in PATH.parts]).replace('\\', '')
BASE = f'SELECT full_path(imagedata.path, {parts}), artist, tags, rating, stars, type, site FROM imagedata'
COMIC = 'SELECT parent FROM comic WHERE path=get_name(%s)'
GESTURE = 'UPDATE imagedata SET date_used=CURDATE() WHERE path=get_name(%s)'
MODIFY = 'UPDATE imagedata SET {} WHERE path=get_name(%s)'
DELETE = 'DELETE FROM imagedata WHERE path=get_name(%s)'