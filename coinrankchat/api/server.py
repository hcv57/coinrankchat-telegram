# run from project root with
# gunicorn coinrankchat.api.server
# then visit
# http://127.0.0.1:8000/channels

import falcon
import json

import coinrankchat.shared.db as db

class Channels():

    def on_get(self, _req, resp):
        doc = db.load_all_channels()
        resp.body = json.dumps(doc, ensure_ascii=False, indent=" ")


api = application = falcon.API()
api.add_route('/channels', Channels())