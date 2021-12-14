import argparse, threading

parser = argparse.ArgumentParser(
    prog='Webscraping', 
    description='Command line interface for common webscraping operations and projects'
    )
parser.add_argument(
    '-a', '--arg', type=int,
    help='argument', default=None
    )
parser.add_argument(
    '-i', '--init', type=bool,
    help='initialize', default=True
    )

args = parser.parse_args()

if args.arg == 0: # webscraping

    from Webscraping import get_starred
    
    from Webscraping import Photos, Illus, comics
    
    threads = [
        threading.Thread(target=Photos.main, args=(args.init,)),
        threading.Thread(target=Illus.main, args=(args.init,)),
        threading.Thread(target=comics.main, args=(args.init,))
        ]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    get_starred()

    print('\nComplete')

elif args.arg == 1: # insert_records

    from Webscraping import insert_records, get_starred
    
    from Webscraping.Photos import imagefap

    threads = [
        threading.Thread(target=insert_records.start),
        threading.Thread(target=imagefap.start),
        ]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    get_starred()

    print('\nComplete')

else:

    # from Webscraping.Favorites import deviantart
    from Webscraping.Photos import blogspot

    # deviantart.main(1, 0)
    blogspot.main(1, 0)