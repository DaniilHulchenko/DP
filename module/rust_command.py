from pprint import pprint

import requests

BASE = "http://127.0.0.1:5000/"
# response=requests.get(BASE+'create')
# print(response.json())

# data = [{'num': 32, 'capacity': 100, 'schudule': '4:00-21:00','route_length':12,'travel_time':1.3,'route':'some route'},
#         {'num': 14, 'capacity': 120, 'schudule': '6:00-21:00','route_length':2,'travel_time':0.3,'route':'some route'},
#         {'num': 53, 'capacity': 10, 'schudule': '4:00-10:00','route_length':8,'travel_time':1,'route':'some route'}]
#
# last_id=requests.get(BASE+'get_last').json()['id']+1
# for i in range(len(data)):
#     response = requests.put(BASE + "num/" + str(last_id+i), json=data[i])
#     print(response.json())

pprint(requests.get(BASE+'num/9').json())
