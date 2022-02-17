import redis
import json

Vrtem_base = redis.Redis(
    host='redis-15296.c57.us-east-1-4.ec2.cloud.redislabs.com',  # ваш хост, если вы поставили Редис к себе
    # на локальную машину, то у вас это будет localhost.
    # Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД,
    # которую мы создавали в скринкасте.
    port=15296,  # порт подключения. На локальной машине это должно быть 6379.
    # Для пользователей облачного сервиса порт всегда разный,
    # поэтому его надо копировать оттуда же, что и host.
    password='39UVjjDqGBg0gNqEcnvnPe9EJ7Z3hOtL'  # для локальной машины пароль не требуется
    # (если вы устанавливали Редис к себе на компьютер и не пользовались облачным сервисом из скринкаста выше).
    # Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password
)

Vrtem_base.set('var1', 'value1')  # записываем в кэш строку "value1"
print(Vrtem_base.get('var1'))  # считываем из кэша данные
print(Vrtem_base.get('varl'))

dict1 = {'name': 'Artem', 'age': 28}  # создаём словарь для записи
Vrtem_base.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(Vrtem_base.get('dict1'))  # с помощью знакомой нам функции превращаем данные,
# полученные из кэша обратно в словарь
print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
print(converted_dict)  # ну и выводим его содержание

Vrtem_base.delete('dict1')  # удаляются ключи с помощью метода .delete()

print('**********************************************************')
# Напишите программу, которая будет записывать и кэшировать номера телефонов ваших друзей.
# Программа должна уметь воспринимать несколько команд:
#    записать номер;
#    показать номер друга в консоли при вводе имени;
#    удалить номер друга по имени.
# Кэширование надо производить с помощью Redis.
# Ввод и вывод информации должен быть реализован через консоль (с помощью функций input() и print()).

cont = True

while cont:
    command = input('Команда:\t')
    if command == 'Запись':
        name = input('name:\t')
        phone = input('phone:\t')
        Vrtem_base.set(name, phone)
    elif command == 'Чтение':
        name = input('name:\t')
        phone = Vrtem_base.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif command == 'Удаление':
        name = input('name:\t')
        phone = Vrtem_base.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif command == 'stop':
        break

