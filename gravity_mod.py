########################################################################
##
## CS 101
## Program Gravity Module
## Name
## Email
##
## PROBLEM : Creates the Gravity UI module
##
## ERROR HANDLING:
##      
##
## OTHER COMMENTS:
##      
##
########################################################################


# tkinter is used for UI
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


class Rect(object):
    """ Rectangle object, contains the corners and color of the rectangle """
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.color = color


# Window size and structure size are set
default_width = 800
default_height = 599

# Set the coordinates of the Drawing Canvas
canvas_top = 0
canvas_left = 0
canvas_height = default_height
canvas_width = 599


class GravWindow(object):
    """ Creates a Tkinter window for the Gravity Interface """
    def __init__(self, title="Python Graphics", background="Black"):
        
        self.__root = tk.Tk()
        self.__root.columnconfigure(1, weight=1)
        self.canvas = tk.Canvas(self.__root, width=canvas_width, height=default_height)
        self.canvas.grid(row=0, column=0)
        self.canvas.config(background=background)
        self.frame = tk.Frame(self.__root, relief = tk.RAISED, borderwidth=1, width=default_width-canvas_width, \
                              height=default_height)
        self.frame.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
        self.frame.rowconfigure(0, weight=10)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(6, weight=10)
        self.frame.columnconfigure(0, weight=1)

        self.clear_button = tk.Button(self.frame, text="Clear Screen", command=self.__clr_screen)
        self.stone_button = tk.Button(self.frame, text="Stone", command=self.__stone)
        self.sand_button = tk.Button(self.frame, text="Sand", command=self.__sand)
        self.water_button = tk.Button(self.frame, text="Water", command=self.__water)
        self.clear_button.grid(row=1, column=0, padx=5, pady=5, stick='ew')
        self.stone_button.grid(row=3, column=0, padx=5, pady=5, stick='ew')
        self.sand_button.grid(row=4, column=0, padx=5, pady=5, stick='ew')
        self.water_button.grid(row=5, column=0, padx=5, pady=5, stick='ew')
        self.stone_button.config(relief=tk.SUNKEN)
        self.material = 0  # 0 for stone, 1 for sand, 2 for water 
        
        self.__root.resizable(width=False, height=False)
        self.__root.geometry('{}x{}'.format(default_width, default_height))
        self.__mouseX = None
        self.__mouseY = None
        self.canvas.bind("<Button-1>", self.__on_click)
        self.canvas.bind("<ButtonRelease-1>", self.__mouse_release)
        self.canvas.bind("<B1-Motion>", self.__mouse_move)
        self.__win = tk.Canvas(self.__root, width=default_width, height=default_height, background=background)
        self.__root.title(title)
        self.__objects = []
        self.events = []
        self.mouse_btn = 0
        self.mouse_pos = None

    def __clr_screen(self):
        self.events.append("CLEAR")

    def __stone(self):
        self.stone_button.config(relief=tk.SUNKEN)
        self.sand_button.config(relief=tk.RAISED)
        self.water_button.config(relief=tk.RAISED)
        self.material = 0

    def __sand(self):
        self.stone_button.config(relief=tk.RAISED)
        self.sand_button.config(relief=tk.SUNKEN)
        self.water_button.config(relief=tk.RAISED)
        self.material = 1

    def __water(self):
        self.stone_button.config(relief=tk.RAISED)
        self.sand_button.config(relief=tk.RAISED)
        self.water_button.config(relief=tk.SUNKEN)
        self.material = 2

    def __material_name(self):
        if self.material == 0:
            return "STONE"
        elif self.material == 1:
            return "SAND"
        else:
            return "WATER"

    @staticmethod
    def __on_canvas(x, y):
        if 0 <= x <= canvas_width and 0 <= y <= canvas_height:
            return True
        return False

    def __on_click(self, e):
        if self.__on_canvas(e.x, e.y):
            self.events.append((self.__material_name(), e.x, e.y))
            self.mouse_btn = 1
            self.mouse_pos = e.x, e.y
            
    def __mouse_move(self, e):
        if self.__on_canvas(e.x, e.y):
            self.events.append((self.__material_name(), e.x, e.y))
            self.mouse_pos = e.x, e.y

    def __mouse_release(self, e):
        self.mouse_btn = 0

    def get_events(self):
        """
        :return: list - The list are the commands that have happened since the last call.
                Each element is either a tuple or a string.
        """
        e = self.events
        self.events = []
        return e

    def refresh(self):
        self.__win.update()

    def draw_screen(self):
        """ Draws any objects you've sent to the screen """
        self.canvas.delete(tk.ALL)

        for item in self.__objects:
            if isinstance(item, Rect):
                self.canvas.create_rectangle(item.x1, item.y1, item.x2, item.y2, fill=item.color, outline=item.color)

        self.canvas.update()
        self.__objects.clear()

        if self.mouse_btn == 1:
            self.events.append((self.__material_name(), self.mouse_pos[0], self.mouse_pos[1]))

    def draw_rect(self, x1: int, y1: int, x2: int, y2: int, fill: str):
        """ Draws a square at the given location
        :param x1: x-coord pixel of the top left corner rectangle.
        :param y1: y-coord pixel of the top left corner
        :param x2: x-coord pixel of the lower right corner of the rectangle
        :param y2: y-coord of the lower right corner of the rectangle
        :param fill: color to fill the rectangle with ( can be text or text of color value #FFFFFF etc.
        :return: None
        """
        self.__objects.append(Rect(x1, y1, x2, y2, fill))
