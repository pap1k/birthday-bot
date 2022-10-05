from core import VK
from vkobjects import Message
import config
def new_message(message, vk : VK):
    if type(message) != Message:
        message = Message(**message['message'])
    if message.from_id == config.self_id:
        return
    if message.peer_id > 2000000000:
        if f'id{config.self_id}|' not in message.text:
            return
    
    found = 0
    for word in config.words:
        if message.text.lower().find(word) != -1:
            found += 1
    if found >= config.accuracy:
        vk.api("messages.send", peer_id=message.peer_id, message=config.answer)