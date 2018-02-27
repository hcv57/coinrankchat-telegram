import boto3
import requests
import requests_cache
import tempfile

from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest, GetMessagesRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import UpdateNewChannelMessage, Message, ChatPhotoEmpty, MessageService, MessageActionChatEditPhoto

from . import db, config
from .connection import client

import logging


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

s3_client = boto3.session.Session().client(
    's3',
    region_name=config.S3_REGION_NAME,
    endpoint_url=config.S3_ENDPOINT_URL,
    aws_access_key_id=config.S3_KEY_ID,
    aws_secret_access_key=config.S3_SECRET
)

requests_cache.install_cache('s3_cache')


def start():
    client.add_update_handler(_handle_update)
    client.idle()
    client.disconnect()

def join_chat(reference):
    """
    Where reference can either be of the form of
    https://t.me/joinchat/BlIEfhCm--HBjli-lCH0Ew
    or
    https://t.me/hello1290
    """
    if '/joinchat/' in reference:
        client(ImportChatInviteRequest(reference.split('/')[-1]))
    else:
        entity = client.get_entity(reference)
        client(JoinChannelRequest(entity))


def _handle_update(update):
    if isinstance(update, UpdateNewChannelMessage):
        _handleNewChannelMessage(update)

def _handleNewChannelMessage(update):
    log.debug("Handling update: %s " % update)
    if isinstance(update.message, MessageService) and isinstance(update.message.action, MessageActionChatEditPhoto):
        store_profile_photo(update.message.to_id, ignore_cache=True)
    elif isinstance(update.message, Message):
        peer_channel = update.message.to_id
        full_channel = client(GetFullChannelRequest(peer_channel))
        pinnedMessage = None
        if full_channel.full_chat.pinned_msg_id:
            pinnedMessage = client(
                GetMessagesRequest(peer_channel, [full_channel.full_chat.pinned_msg_id])
            ).messages[0].message
        db.ChatUpdate(
            channel_id=peer_channel.channel_id,
            title=full_channel.chats[0].title,
            about=full_channel.full_chat.about,
            pinnedMessage=pinnedMessage,
            username=full_channel.chats[0].username,
            participants_count=full_channel.full_chat.participants_count
        ).save()
        store_profile_photo(update.message.to_id)

def store_profile_photo(channel, ignore_cache=False):
    def fetch(filename, download_big=False):
        url = '%s/%s' % (config.IMAGE_SERVER_URL, filename)
        if ignore_cache or requests.head(url).status_code != 200:
            entity = client.get_entity(channel)
            if isinstance(entity.photo, ChatPhotoEmpty):
                s3_client.upload_file(config.NOAVATAR_PICTURE, config.S3_BUCKET, filename, dict(ACL="public-read"))
            else:
                with tempfile.SpooledTemporaryFile(mode='r+b') as f:
                    client.download_profile_photo(entity, f, download_big=download_big)
                    f.seek(0)
                    s3_client.upload_fileobj(f, config.S3_BUCKET, filename, dict(ACL="public-read"))

    fetch('%s.jpeg' % channel.channel_id)
    fetch('%s-big.jpeg' % channel.channel_id, download_big=True)
