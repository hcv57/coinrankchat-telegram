# WIP Notes to self

## Telegram handler
`docker run --rm -ti --link elasticsearch:elastic -e "ELASTIC_HOST=elastic" -e "TELEGRAM_API_ID=xxx" -e "TELEGRAM_API_HASH=xxx" -e -e "TELEGRAM_PHONE=xxx" coinrankchat python -m coinrankchat.main`

## API server
`.../gunicorn --reload --bind 0.0.0.0 coinrankchat.api.server`

## Nginx
`docker run --rm -v -P .../coinrankchat/nginx.conf:/etc/nginx/nginx.conf:ro nginx:alpine`

## Requirements generation
`pipenv lock -r > requirements.txt`

## Grant temp access to GCR registry
`gcloud docker --authorize-only `