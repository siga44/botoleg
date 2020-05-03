import datetime
from time import sleep
from random import randint

import vk_api

# CONSTANTS BEGIN
keywords = ['ИТ-71б',
            'Тарасов', 'Тарасова', 'ТарасовЕ.С.', 'Тарасову',
            '3 курс', '3 курса', '3 курсу', 'третий курс', 'третьему курсу', 'третьем курсе',
            'Букрин', 'Букрина', 'Букриной', 'БукринаЕ.В.',
            'Кусайкин', 'КусайкинД.В.', 'Кусайкина', 'Кусайкину',
                        'Евдаков', 'ЕвдаковаЛ.Н', 'Евдакова', 'Евдаковой',
                        'Соловаров', 'Соловарова', 'Соловарову',
                        'Будылдин', 'Будылдина', 'Будылдиной',
                        'Обвинцев', 'Обвинцева', ]
keywords_exceptions = ['второй курс', 'второму курсу', '1 курс', '1 курсу', '1 курса',
                       'первый курс', 'первому курсу', '2 курс', '2 курсу', '2 курса',
                       'четвертый курс', 'четвертому курсу', '4 курс', '4 курса', '4 курсу',
                       'МЕ91', 'ИТ91', 'ОЕ91', 'ПЕ91', 'ТЕ91', 'ИТ92', 'ПЕ92', 'СПО',
                       'МЕ81', 'ИТ81', 'ОЕ81', 'ПЕ81',
                       'МЕ61', 'ИТ61', 'ОЕ61', 'ПЕ81', ]

api_v = '5.103'
group_token = 'e8b293bfd5efaa3525d69378e8efef482de27fe5f5e3e55e0e6a846ae8e7c1f3bad549597d02841f9cab0'
app_token = 'f6d3fc52f6d3fc52f6d3fc5296f6a3f516ff6d3f6d3fc52a8a63d8782e7ea96c4072f1a'
vk_group_session = vk_api.VkApi(token=group_token, api_version=api_v)
vk_app_session = vk_api.VkApi(token=app_token, api_version=api_v)
target_id = -111657899
posts_count = 30
# CONSTANTS END
# HANDLERS BEGIN


def posts_filter(response, last_id):
    for item in response['items']:
        if item['id'] > last_id:
            if item['text'].find(keywords[0]) != -1:
                last_id = item['id']
                return last_id
            for kw in keywords:
                if item['text'].find(kw) != -1:
                    for ekw in keywords_exceptions:
                        if item['text'].find(ekw) == -1:
                            last_id = item['id']
                            return last_id
        else:
            return last_id


def main(last_id):
    response = vk_app_session.method(
        "wall.get", {"owner_id": target_id, "count": posts_count})
    new_last = posts_filter(response, last_id)
    if new_last > last_id:
        with open('last_id.txt', 'w') as file:
            file.write(str(new_last))
        with open('user_ids.txt') as user_ids:
            user_ids = user_ids.read()
        message = f"Последнее изменение:\nhttps://vk.com/raspisanie_urtisi?w=wall-111657899_{last_id}"
        vk_group_session.method('messages.send', {
                                'user_ids': user_ids, 'random_id': randint(1, 2**63), "message": message})


# HANDLERS END
# ENTER POINT START
def runner():
    try:
        with open('last_id.txt') as file:
            last_id = file.read()
        main(int(last_id))
        print(datetime.datetime.now().strftime('%H:%M'), last_id)
        sleep(30)
        runner()
    except:
        sleep(120)


if __name__ == '__main__':
    runner()
# ENTER POINT END
