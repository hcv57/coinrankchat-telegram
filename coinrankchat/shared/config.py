from os import environ

# DB
ELASTIC_HOST = environ.get('ELASTIC_HOST', 'localhost')

# Telegram
TELEGRAM_SESSION = 'coinrankchat'
TELEGRAM_API_ID = int(environ.get('TELEGRAM_API_ID', -1))
TELEGRAM_API_HASH = environ.get('TELEGRAM_API_HASH')
TELEGRAM_PHONE = environ.get('TELEGRAM_PHONE')

# Group images
NOAVATAR_IMAGE = './noavatar.jpg'
IMAGE_STORAGE_PATH = environ.get('IMAGE_PATH', '.')