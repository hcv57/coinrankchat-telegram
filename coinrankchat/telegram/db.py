import time
from elasticsearch_dsl import connections, DocType, Text, Integer, Date, datetime, Keyword, Float

from . import config

_connection = connections.create_connection(hosts=[config.ELASTIC_HOST], timeout=10, max_retries=20)

while not _connection.ping():
    time.sleep(5)

class ChatUpdate(DocType):
    channel_id = Keyword()
    from_id = Keyword()
    title = Text()
    about = Text()
    pinnedMessage = Text()
    sentimentPolarity = Float()
    sentimentSubjectivity = Float()
    username = Keyword()
    participants_count = Integer()
    created_at = Date()

    class Meta:
        index = 'chatupdates'

    def save(self, **kwargs):
        self.created_at = datetime.utcnow()
        return super().save(**kwargs)

def _setup_database():
    ChatUpdate.init()

_setup_database()
