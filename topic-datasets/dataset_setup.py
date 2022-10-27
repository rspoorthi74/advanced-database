import dataset

db = dataset.connect('sqlite:///Travel_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'shirts' },
        { "description": 'tshirts' },
        { "description": 'pants' },
        { "description": 'shorts with pockets' },
        { "description": 'toiletries' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()