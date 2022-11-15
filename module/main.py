from abc import ABC, abstractmethod
from pprint import pprint
from threading import Lock

import requests
from maps import find_route,BASE


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
class Department(metaclass=singleton):
    """Abstract fabric + singletone"""
    @abstractmethod
    def pave_way(self,start_point, finish_point, cityб,build_map=False):pass
    @abstractmethod
    def make_schudule(self,schudule):
        return Schudule().make_schudule(schudule)
    @abstractmethod
    def make_transport(self,num,capacity):pass

    def show_transport_list(self):
        return requests.get(BASE+'num/0').json()
    def buy_ticket(self):
        return 'You buy ticket!'
    def take_a_transport(self,passenger):
        if passenger.ticket:
            return ('You take a transport!')
        else:
            return ('You dont have a ticket')


class Station(Department):
    def pave_way(self,start_point, finish_point, city,build_map=False):
        return road_Route(start_point, finish_point, city,build_map)
    def make_transport(self,num,capacity):
        return Bus(num,capacity)


class Depo(Department):
    def pave_way(self,start_point, finish_point,city,build_map=False):
        return railway_Route(start_point, finish_point, city,build_map)
    def make_transport(self,num,capacity):
        return Train(num,capacity)




class Route(ABC):
    def __init__(self, start_point, finish_point,city,build_map):
        self.city=city
        self.start_point= start_point
        self.finish_point=finish_point
        self.build_map=build_map
    @abstractmethod
    def find_route(self) -> dict: pass

class railway_Route(Route):
    def find_route(self) -> dict:
        return find_route(CITY=self.city,FROM=self.start_point,TO=self.finish_point,mode='drive_service',build_map=self.build_map)
class road_Route(Route):
    def find_route(self) -> dict:
        return find_route(CITY=self.city,FROM=self.start_point,TO=self.finish_point,mode='drive',build_map=self.build_map)


class Schudule():
    def make_schudule(self,shedule:list):
        return str(shedule[0])+":00-"+str(shedule[1])+":00"


class Transport(ABC):
    def __init__(self,number,capacity):
        self.number=number
        self.capacity=capacity
    @abstractmethod
    def launch_tranport(self,route,schudule):pass

class Train(Transport):
    def launch_tranport(self,route,schudule):
        data = {'num': self.number, 'capacity': self.capacity, 'schudule': schudule,
                'route_length': route['route_length'],
                'travel_time': route['travel_time'], 'route': str(route['route'])}

        last_id = str(requests.get(BASE + 'get_last').json()['id'] + 1)
        response = requests.put(BASE + "num/" + last_id, json=data)
        return f'You successfully launch Train {response.json()}'
class Bus(Transport):
    def launch_tranport(self,route,schudule):
        data={'num': self.number, 'capacity': self.capacity, 'schudule': schudule, 'route_length': route['route_length'],
         'travel_time': route['travel_time'],'route': str(route['route'])}

        last_id=str(requests.get(BASE+'get_last').json()['id']+1)
        response = requests.put(BASE+"num/"+last_id, json=data)
        return f'You successfully launch Bus {response.json()}'
class Truck(Transport):
    def launch_tranport(self,route,schudule):
        data = {'num': self.number, 'capacity': self.capacity, 'schudule': schudule,
                'route_length': route['route_length'],
                'travel_time': route['travel_time'], 'route': str(route['route'])}

        last_id = str(requests.get(BASE + 'get_last').json()['id'] + 1)
        response = requests.put(BASE + "num/" + last_id, json=data)
        return f'You successfully launch Truck {response.json()}'




class Passangerinfo(ABC):
    def __init__(self,name,privileges,age):
        self.name:str=name
        self.privileges:bool=privileges
        self.age:float=age
class Passanger(Passangerinfo):
    def __init__(self,A,B,name,privileges,age):
        if privileges==1:
            self.ticket:bool=1
        else:
            self.ticket: bool = 0
        self.A:str=A
        self.B:str=B
        super().__init__(name,privileges,age)

    def buy_ticket(self):
        self.ticket=1
        return Department().buy_ticket()


def add_route(place: Department, city, start_point, finish_point, shedule, num, capacity,build_map: bool = False):
    way = place.pave_way(start_point=start_point, finish_point=finish_point, city=city,build_map=False).find_route()
    schudule = place.make_schudule(shedule)
    tramsport = place.make_transport(num, capacity)
    tramsport=tramsport.launch_tranport(way, schudule)
    # response = requests.put("http://127.0.0.1:5000/num/" + str(i), json=tramsport)
    return (tramsport)


# print(add_route(Station(), 'North York, Toronto, Canada', '4401 Bathurst St',
#                     '16 Hendon Ave', [6,23], 874, 100))

# pprint(Department().show_transport_list(),sort_dicts=False)

# passanger=Passanger('4401 Bathurst St','16 Hendon Ave','Glam',0,28)
# passanger.buy_ticket()
# print(Department().take_a_transport(passanger))




