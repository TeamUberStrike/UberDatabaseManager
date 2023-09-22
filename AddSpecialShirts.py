from pymongo import MongoClient

client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")

db = client.admin
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
        
        db.Users.update_one(
            {"UserId": i},
            { "$addToSet": { "Inventory" : 
                {
                    "AmountRemaining": -1,
                    "Cmid": i,
                    "ExpirationDate": None,
                    "ItemId": Item
                }
            }}
        )
        if Item == AdminShirt:
            ItemName = "Admin Shirt"
        elif Item == BetaHeroShirt:
            ItemName = "Beta Hero Shirt"
        elif Item == GlobalModShirt:
            ItemName = "Global Moderator Shirt"
        elif Item == ModShirt:
            ItemName = "Moderator Shirt"
        elif Item == QAShirt:
            ItemName = "QA Shirt"
        elif Item == SLDShirt:
            ItemName = "SLD Clan Shirt"
        elif Item == C4CShirt:
            ItemName = "C4C Clan Shirt"
        elif Item == DEDShirt:
            ItemName = "DED Clan Shirt"
        elif Item == ST6IXShirt:
            ItemName = "ST6IX Clan Shirt"
        print("Item:",ItemName,"was added!")