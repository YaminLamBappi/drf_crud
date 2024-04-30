import requests
import json


URL = 'http://127.0.0.1:8000/crud/familyapi/'

def create():
    data = {
        'name': 'Jon',
        'phone' : 3,
        'address': 'player'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

create()


def read(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)
    
# read(2)

def update():
    data = {
        'id': 2,
        'name': 'Yamin',
        'address': 'cheif'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
    
# update()
    
def delete(id):
    data = {'id': id}

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)

# delete()