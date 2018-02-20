from os import environ

# DB
ELASTIC_HOST = environ.get('ELASTIC_HOST', 'localhost')

# Telegram
TELEGRAM_SESSION = 'coinrankchat'
TELEGRAM_API_ID = int(environ.get('TELEGRAM_API_ID', -1))
TELEGRAM_API_HASH = environ.get('TELEGRAM_API_HASH')
TELEGRAM_PHONE = environ.get('TELEGRAM_PHONE')

# Group images (TODO remove in favour of S3)
NOAVATAR_IMAGE = './noavatar.jpg'
IMAGE_STORAGE_PATH = environ.get('IMAGE_PATH', '.')

# S3
S3_HOST = environ.get('S3_HOST')
S3_BUCKET = environ.get('S3_BUCKET')
S3_KEY = environ.get('S3_KEY')
S3_SECRET = environ.get('S3_SECRET')
