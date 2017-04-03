import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds141410.mlab.com:41410/food_db
host = "ds141410.mlab.com"
port = 41410
db_name = "food_db"
username = "admin"
password = "admin"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())