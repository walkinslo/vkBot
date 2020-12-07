import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from toks import main_token

vk_session = vk_api.VkApi(token=main_token)
vk = vk_session.get_api()
longpool = VkLongPoll(vk_session)


def sender(id, text):
    vk.messages.send(user_id=id, message=text, random_id=0)


def send_stick(id, number):
    vk.messages.send(user_id=id, sticker_id=number, random_id=0)


def send_photo(id, url):
    vk.messages.send(user_id=id, attachment=url, random_id=0)


for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id

            if msg == 'привет':
                sender(id, 'привет')
                send_stick(id, 49)
