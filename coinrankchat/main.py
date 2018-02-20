import logging
import coinrankchat.telegram.handler

def main():
    coinrankchat.telegram.handler.start()


if __name__ == '__main__':
    # FIXME remove logging
    logger = logging.getLogger('telethon')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
    main()