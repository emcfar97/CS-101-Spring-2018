from .. import CONNECT, INSERT, SELECT, WEBDRIVER
from ..utils import Progress, get_hash, get_name, get_tags, generate_tags, bs4, re, save_image
import time
from PIL import Image
from selenium.webdriver.common.keys import Keys

SITE = 'pinterest'

def page_handler(hrefs, section):
    
    progress = Progress(len(hrefs), section)

    for href in hrefs:
        
        print(progress)

        DRIVER.get(f'https://www.pinterest.com{href.get("href")}')
        time.sleep(1)
        html = bs4.BeautifulSoup(DRIVER.page_source(), 'lxml')
        target = html.find('a', href=True, attrs={'data-test-id':'image-link'})
        try: src = target.findAll('img', src=re.compile('.+pinimg.+'))[-1].get('src')
        except: continue

        if (name:=get_name(src, 0, 1)).exists(): continue
        save_image(name, src)

        if name.suffix in ('.jpg'):

            tags, rating, exif = generate_tags(
                general=get_tags(DRIVER, name), 
                custom=True, rating=True, exif=True
                )
            Image.open(name).save(name, exif=exif)

        elif name.suffix in ('.gif', '.webm', '.mp4'):
            
            tags, rating = generate_tags(
                general=get_tags(DRIVER, name), 
                custom=True, rating=True, exif=False
                )

        if section not in tags: tags += f' {section}'
        hash_ = get_hash(src, True)

        CONNECTION.execute(
            INSERT[5], (str(name), '', tags, rating, 0, hash_, src, SITE), commit=1
            )
        
    print(progress)
    
def start(retry=0):

    global CONNECTION, DRIVER
    CONNECTION = CONNECT()
    DRIVER = WEBDRIVER()
    
    DRIVER.login(SITE)
    boards = {
        # 'winter-casual':['jeans', 'leggings', 'shorts', 'skirt'],
        'summer-casual':{'jeans', 'leggings', 'shorts', 'skirt'},
        # 'athletic-wear':['',],
        # 'dresses':['',],
        # 'business':['',],
        # 'your-pinterest-likes': ['']
        }
    query = set(
        href for href, in CONNECTION.execute(SELECT[0], (SITE,), fetch=1)
        )

    for board, sections in boards.items():

        total = set()

        for section in sections:
            
            DRIVER.get(f'https://pinterest.com/chairekakia/{board}/{section}')
            
            while True:
                
                time.sleep(1)
                html = bs4.BeautifulSoup(DRIVER.page_source(), 'lxml')
                targets = html.find(class_='gridCentered').findAll(
                    'a', href=re.compile('/pin/\d+/')
                    )
                targets = set(targets) - total
                total = (total | targets) - query
                
                if not targets:
                    if retry >= 2:
                        page_handler(total, section)
                        break
                    else: retry += 1
                else: retry = 0
                
                for _ in range(3):
                    DRIVER.find('html', Keys.PAGE_DOWN, type_=6)
                    time.sleep(2)
            
    DRIVER.close()