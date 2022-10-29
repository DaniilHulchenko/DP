from pprint import pprint
import pymysql
import requests
from threading import Lock, Thread


# class singleton(type):
#     _instance=None
#     _lock: Lock = Lock()
#     def __call__(cls, *args, **kwargs):
#         with cls._lock:
#             if  cls._instance==None:
#                 # cls._instance[cls] = super(singleton, cls).__call__(*args, **kwargs)
#                 cls._instance = super().__call__(*args, **kwargs)
#         return cls._instance
class singleton(type):
    _instance = {}
    # _instance = None
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instance:
                # cls._instance[cls] = super(singleton, cls).__call__(*args, **kwargs)
                cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class weather(metaclass=singleton):
    def __init__(self):
        self.connect()
        self.update_citys_data()

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='Silverus',
                password='Sql320652548!',
                database='lab4',
                cursorclass=pymysql.cursors.DictCursor
            )
            print('Connection success!\n')
        except Exception as ex:
            import sys
            print("Connection failed...")
            print(ex)
            sys.exit()

    def __del__(self):
        self.connection.commit()
        self.connection.close()
        print("\nConnection closed!")

    def __used_citys(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select city_name as 'city', count(*)as 'amo' from weather group by city_name;")
            citys = [i['city'] for i in cursor.fetchall()]
            return citys

    def add_citys_data(self, city='toronto', APPID="ec64d45f232434d9a23b90eebdf1db86"):
        all_info = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APPID}&units=metric').json()
        try:
            with self.connection.cursor() as cursor:
                if all_info['name'] not in self.__used_citys():
                    command = f'insert into weather(city_name,temp,feels_like,sky,wild_speed,visibility\n)'\
                              f'\tvalue("{str(all_info["name"])}",{float(all_info["main"]["temp"])},{float(all_info["main"]["feels_like"])},"{str(all_info["weather"][0]["description"])}",{float(all_info["wind"]["speed"])},{int(all_info["visibility"])});'
                else:
                    command = f'update weather set '\
                              f'\n\ttemp={float(all_info["main"]["temp"])},feels_like={float(all_info["main"]["feels_like"])},sky="{str(all_info["weather"][0]["description"])}",wild_speed={float(all_info["wind"]["speed"])},visibility={int(all_info["visibility"])}'\
                              f'\n\twhere city_name="{all_info["name"]}"'
                cursor.execute(command)
        except Exception as ex:
            print("err:\n", ex)
        finally:
            self.connection.commit()

    def update_citys_data(self,APPID="ec64d45f232434d9a23b90eebdf1db86"):
        try:
            with self.connection.cursor() as cursor:
                for city in self.__used_citys():
                    all_info = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APPID}&units=metric').json()
                    command = f'update weather set ' \
                              f'\n\ttemp={float(all_info["main"]["temp"])},feels_like={float(all_info["main"]["feels_like"])},sky="{str(all_info["weather"][0]["description"])}",wild_speed={float(all_info["wind"]["speed"])},visibility={int(all_info["visibility"])}' \
                              f'\n\twhere city_name="{all_info["name"]}"'
                    cursor.execute(command)
        except Exception as ex:
            print("err:\n", ex)
        finally:
            self.connection.commit()

    def show_db(self):
        with self.connection.cursor() as cursor:
            cursor.execute('select * from weather;')
            pprint(cursor.fetchall())

    def _rebild_db(self):
        with self.connection.cursor() as cursor:
            cursor.execute('drop table if exists weather;')
            cursor.execute('create table weather('\
                            'id int auto_increment,'\
                            'city_name varchar(30),'\
                            'temp float,'\
                            'feels_like float,'\
                            'sky varchar(30),'\
                            'wild_speed float,'\
                            'visibility int,'\
                            'primary key(id)'\
                            ');')

    def commands(self,command):
        with self.connection.cursor() as cursor:
            cursor.execute(command)
            pprint(cursor.fetchall())


if __name__ == '__main__':
    t = weather()
    t2 = weather()
    # # t._drop_db()
    #
    # t.add_citys_data(city="Toronto")
    # t.add_citys_data(city="Rom")
    # t.add_citys_data(city="Lviv")

    t.show_db()
    print(t," ",t2)

    # t.commands('select * from weather;')

########################################################################################################
# Connection success!
#
# [{'city_name': 'Toronto',
#   'feels_like': 2.24,
#   'id': 1,
#   'sky': 'clear sky',
#   'temp': 6.11,
#   'visibility': 10000,
#   'wild_speed': 6.17},
#  {'city_name': 'Rome',
#   'feels_like': 16.55,
#   'id': 2,
#   'sky': 'clear sky',
#   'temp': 16.78,
#   'visibility': 10000,
#   'wild_speed': 2.06},
#  {'city_name': 'Lviv',
#   'feels_like': 8.04,
#   'id': 3,
#   'sky': 'few clouds',
#   'temp': 9.73,
#   'visibility': 10000,
#   'wild_speed': 3.27}]
# <__main__.weather object at 0x00000213E09AA950>   <__main__.weather object at 0x00000213E09AA950>
#
# Connection closed!

