from vkbottle import Bot, Message
from random import choice
import json


# KEYBOARDS BEGIN


def get_button(label, color, payload='{}'):
    return {
        "action": {
            "type": "text",
            "payload": payload,
            "label": label,
        },
        "color": color,
    }


kb_main = {
    "one_time": False,
    "buttons":
        [
            [
                get_button('Посмотреть расписание', 'primary'),
            ],
            [
                get_button("Будылдина", 'primary'),
                get_button("Букрина", 'primary'),
                get_button("Соловаров", 'primary'),
            ],
        ]
}

kb_timetable = {
    "one_time": False,
    "buttons":
        [
            [
                get_button('Понедельник', 'primary'),
                get_button('Вторник', 'primary'),
                get_button('Среда', 'primary'),
            ],
            [
                get_button('Четверг', 'primary'),
                get_button('Пятница', 'primary'),
                get_button('Суббота', 'primary'),
            ],
            [
                get_button('Посмотреть последнее изменение', 'positive')
            ],
            [
                get_button('Вернуться на главную', 'negative')
            ],
        ]
}


def kb_process(keyboard):
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode("utf-8")
    keyboard = str(keyboard.decode("utf-8"))
    return(keyboard)


kb_main = kb_process(kb_main)
kb_timetable = kb_process(kb_timetable)
# KEYBOARDS END

# ~~~~~~~~~~ CONSTANTS BEGIN ~~~~~~~~~~
bot = Bot("e8b293bfd5efaa3525d69378e8efef482de27fe5f5e3e55e0e6a846ae8e7c1f3bad549597d02841f9cab0")

stickers = ['2466', '2467', '2468', '2469', '2470', '2471', '2472',
            '2473', '2474', '2475', '2476', '2477', '2478', '2479', '2480', '2481', '19411', '19412', '19413', '19414', '19415', '19584', '19797', '20012', '20181', '20279', '163', '131']
commands_days = {'Понедельник': 7, 'Вторник': 1,
                 'Среда': 2, 'Четверг': 3, 'Пятница': 4, 'Суббота': 5}
lecturers_dict = {"Будылдина": "Диск: https://vk.cc/arwilg\nПочта: bnv@urtisi.ru\n",
                  "Букрина": "Диск: https://vk.cc/arwhY4\nПочта mec@urtisi.ru\n",
                  "Соловаров": "Диск: https://vk.cc/arwhRv\nПочта mec@urtisi.ru\n"}
# ~~~~~~~~~~ CONSTANTS END ~~~~~~~~~~

# ~~~~~~~~~~ HANDLER BEGIN ~~~~~~~~~~
@bot.on.message(text="<message>")
async def message_handler(ans: Message, message):
    if message == 'Посмотреть расписание':
        await ans('Нажми на нужный день', keyboard=kb_timetable)
    elif message in lecturers_dict:
        await ans(f"Ссылки для преподавателя {message}")
        await ans(f"{lecturers_dict[message]}")
    elif message in commands_days:
        with open(f'../timetable/{commands_days[message]}_sem_6.txt', 'rt', encoding="utf-8") as file:
            await ans(file.read())
    elif message == 'Посмотреть последнее изменение':
        with open('../last_id.txt', 'rt') as file:
            await ans(f"https://vk.com/raspisanie_urtisi?w=wall-111657899_{file.read()}")
    elif message == 'Вернуться на главную':
        await ans("Главное меню", keyboard=kb_main)
    else:
        await ans(sticker_id=choice(stickers))
bot.run_polling(skip_updates=False)
# ~~~~~~~~~~ HANDLER END ~~~~~~~~~~
