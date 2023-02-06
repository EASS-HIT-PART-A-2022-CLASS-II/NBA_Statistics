import pymongo
client=pymongo.MongoClient("mongodb+srv://ron_pinto:Aa123456@icons.uvffn44.mongodb.net/icons")
db=client["icons_database"]
collection=db["icons_collection"]
collection.insert_many([
    {
    "image_name": "Hornets",
    "image_url": "https://content.sportslogos.net/logos/6/5120/full/1926_charlotte__hornets_-primary-2015.png"
    },
    {
    "image_name": "Nets",
    "image_url": "https://content.sportslogos.net/logos/6/3786/full/brooklyn_nets_logo_primary_20135043.png"
    },
    {
    "image_name": "Celtics",
    "image_url": "https://content.sportslogos.net/logos/6/213/thumbs/slhg02hbef3j1ov4lsnwyol5o.giff"
    }
])