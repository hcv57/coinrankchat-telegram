import os.path

from shutil import copyfile
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import UpdateNewChannelMessage, Message, ChatPhotoEmpty, MessageService, MessageActionChatEditPhoto

from coinrankchat.shared import db, config
from .connection import client


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
    try:
        _join_chat(reference)
        entity = client.get_entity(reference)
        _store_entity_or_default_picture(entity)
    except Exception as e:
        print("Failed to join: ", reference, e)



def _handle_update(update):
    if isinstance(update, UpdateNewChannelMessage):
        _handleNewChannelMessage(update)

def _handleNewChannelMessage(update):
    if isinstance(update.message, MessageService) and isinstance(update.message.action, MessageActionChatEditPhoto):
        entity = client.get_entity(update.message.to_id)
        _store_entity_or_default_picture(entity)
    elif isinstance(update.message, Message):
        peer_channel = update.message.to_id
        full_channel = client(GetFullChannelRequest(peer_channel))
        db.ChatUpdate(
            channel_id=peer_channel.channel_id,
            title=full_channel.chats[0].title,
            username=full_channel.chats[0].username,
            participants_count=full_channel.full_chat.participants_count
        ).save()


def _join_chat(reference):
    if '/joinchat/' in reference:
        client(ImportChatInviteRequest(reference.split('/')[-1]))
    else:
        entity = client.get_entity(reference)
        client(JoinChannelRequest(entity))

def _store_entity_or_default_picture(entity):
    filepath = os.path.join(config.IMAGE_STORAGE_PATH, "%s.jpg" % entity.id)
    if isinstance(entity.photo, ChatPhotoEmpty):
        copyfile(config.NOAVATAR_IMAGE, filepath)
        print("Used noavatar image")
    else:
        with open(filepath, 'wb') as f:
            client.download_profile_photo(entity, file=f, download_big=False)
            print("Fetched profile photo")
