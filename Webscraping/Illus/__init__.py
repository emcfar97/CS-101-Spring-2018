import threading
from . import gelbooru
from .. import WEBDRIVER, Favorites, sankaku

def start():

    # Favorites.start()

    threads = [
        # threading.Thread(target=gelbooru.setup, args=(WEBDRIVER(),)),
        threading.Thread(target=sankaku.setup, args=(WEBDRIVER(), 1))
        ]
    for thread in threads: thread.start()
    for thread in threads: thread.join()