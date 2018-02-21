import falcon
import json

import coinrankchat.shared.db as db

class Home():

    def on_get(self, _req, resp):
        resp.body = "API Home"

class Channels():

    def on_get(self, _req, resp):
        doc = db.load_all_channels()
        resp.body = json.dumps(doc, ensure_ascii=False, indent=" ")


api = application = falcon.API()
api.add_route('/', Home())
api.add_route('/channels', Channels())