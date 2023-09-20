from pymongo import MongoClient

client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")
db = client.admin
collection = db["Test"]

result = db.Test.find()
total_accounts=len(list(result))

AdminShirt = 1037
BetaHeroShirt = 1038
GlobalModShirt = 1040
ModShirt = 1041
QAShirt = 1042
SLDShirt = 1044
DEDShirt = 1045
C4CShirt = 1046
ST6IXShirt = 1047
#Admins [1, 530], SeniorModerator [3, 38], SeniorQA [39], Moderator [2, 4], QA [5, 6, 7, 9, 30, 105]
Cmids = [1]
ItemstoAdd = [AdminShirt]

CmidRange = len(list(Cmids))

for i in Cmids:
    print("Cmid:",i)
    for Item in ItemstoAdd:
        ItemId = Item
        print("Item:",ItemId)
        db.TestUser.update_one(
            {"UserId": i},
            { "$addToSet": { "Inventory" : 
                {
                    "AmountRemaining": -1,
                    "Cmid": i,
                    "ExpirationDate": None,
                    "ItemId": ItemId
                }
            }}
        )