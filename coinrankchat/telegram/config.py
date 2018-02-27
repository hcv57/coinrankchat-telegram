from os import environ

# DB
ELASTIC_HOST = environ.get('ELASTIC_HOST', 'localhost')

# Telegram
TELEGRAM_SESSION = 'coinrankchat'
TELEGRAM_API_ID = int(environ.get('TELEGRAM_API_ID', -1))
TELEGRAM_API_HASH = environ.get('TELEGRAM_API_HASH')
TELEGRAM_PHONE = environ.get('TELEGRAM_PHONE')

# S3
S3_REGION_NAME='ams3'
S3_ENDPOINT_URL = 'https://ams3.digitaloceanspaces.com'
S3_BUCKET = 'coinrankchat'
S3_HOST = environ.get('S3_HOST')
S3_KEY_ID = environ.get('S3_KEY_ID')
S3_SECRET = environ.get('S3_SECRET')

NOAVATAR_PICTURE = "noavatar.jpeg"

IMAGE_SERVER_URL = environ.get('IMAGE_SERVER_URL')