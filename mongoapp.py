from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")
db=client.admin
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)
result = db.Users.find()

total_accounts=len(list(result)) #get number of total accounts
print("Total accounts:", total_accounts)
for i in range(1,total_accounts+1): #iterate through all documents in Users collection, add +1 to total_accounts so last document will be updated as well
    db.Users.update_one(
        { "UserId" : i },
        { "$set": {   "Inventory": [
        {
        "AmountRemaining": -1,
        "Cmid": i,
        "ExpirationDate": None,
        "ItemId": 1
        },
        {
        "AmountRemaining": -1,
        "Cmid": i,
        "ExpirationDate": None,
        "ItemId": 12
        }
    ]} }
    )
    db.Users.update_one(
        { "UserId" : i },
        { "$set": {     "Loadout": {
            "Backpack": 0,
            "Boots": 1089,
            "Cmid": i,
            "Face": 0,
            "FunctionalItem1": 0,
            "FunctionalItem2": 0,
            "FunctionalItem3": 0,
            "Gloves": 1086,
            "Head": 1084,
            "LoadoutId": 0,
            "LowerBody": 1088,
            "MeleeWeapon": 1,
            "QuickItem1": 0,
            "QuickItem2": 0,
            "QuickItem3": 0,
            "SkinColor": "#FFFFFF",
            "Type": 0,
            "UpperBody": 1087,
            "Weapon1": 12,
            "Weapon1Mod1": 0,
            "Weapon1Mod2": 0,
            "Weapon1Mod3": 0,
            "Weapon2": 0,
            "Weapon2Mod1": 0,
            "Weapon2Mod2": 0,
            "Weapon2Mod3": 0,
            "Weapon3": 0,
            "Weapon3Mod1": 0,
            "Weapon3Mod2": 0,
            "Weapon3Mod3": 0,
            "Webbing": 0
    }} }
    )