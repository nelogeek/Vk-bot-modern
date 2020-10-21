from editor.editor import Edit
from lilly import Lilly
import vk_api.vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from config import vk_api_token


token = '6542d1df28acd256202bb5c1817b52955e103ffae530566a710238c94970b940b78b8eed7d48773abd995'    # access_token
vk = vk_api.VkApi(token=token)
vk_s = vk.get_api()

lilly = Lilly()     # Ядро бота

longpoll = VkBotLongPoll(vk, 171857362)  # VkApi, group_id

# Слушаем сервер
for event in longpoll.listen():

    # Новое сообщение
    if event.type == VkBotEventType.MESSAGE_NEW:
        print('Новое сообщение:')

        if event.group_id:
            print(event.object.from_id, 'пишет: ')

            vk_s.messages.send(peer_id=event.object.peer_id,
                               message=lilly.update_screen(
                                   Edit.clean_str_from_symbol(event.object.text, "[", "]")[1::]))

        print('Текст: ', event.object.text, end="\n")
