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
print(total_accounts)
for i in range(1,total_accounts+1): #iterate through all documents in Users collection, add +1 to total_accounts so last document will be updated as well
    db.Users.update_one(
        { "UserId" : i },
        { "$set": {   "Inventory": [
        {
        "AmountRemaining": -1,
        "Cmid": i,
        "ExpirationDate": "null",
        "ItemId": 1
        },
        {
        "AmountRemaining": -1,
        "Cmid": i,
        "ExpirationDate": "null",
        "ItemId": 12
        }
    ]} }
    )