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
                send_stick(id, 50601)
                sender(id, 'Привет! Что вас интересует? (вступление, отзыв)')
            if msg == 'вступление':
                sender(id, 'О, это отлично! Пожалуйста, заполните эту форму: https://forms.gle/bSwmYoDZyYpuUrBAA, '
                           'позже с вами свяжется администратор.')
            if msg == 'отзыв':
                sender(id, 'Спасибо! Пожалуйста, перейдите по этой ссылке: https://vk.com/topic-200484118_46658255, и '
                           'оставьте отзыв!')
            if msg == 'спасибо':
                send_stick(id, 50599)
                sender(id, 'И Вам спасибо!')

            if msg == 'пока':
                sender(id, 'Возвращайтесь скорее!')

            if msg == 'лох':
                sender(id, 'Нет ты')

            if msg == 'соси':
                sender(id, 'А сам пососать не хочешь?')

            if msg == 'люблю вас':
                sender(id, 'И мы Вас любим!')
