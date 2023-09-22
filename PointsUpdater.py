from pymongo import MongoClient

client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")
db = client.admin
CollectionFixedUsers = db["FixedUsers"]
CollectionBrokenUsers = db["BrokenUsers"]
CollectionCurrentUsers = db["Users"]

result = db.Users.find()
total_accounts=len(list(result))

def addPointsToAwardWinners()
    AwardWinners = [2, 5, 13, 69, 71, 114, 118, 140, 224, 491, 555, 670, 815, 883]
    for i in AwardWinners:
        AwardBalance = NewBalance + 50000
    
    db.Users.update_one(
        { "UserId": j},
        { "$set": {"Wallet.Points": AwardBalance}}
    )

addPointsToAwardWinners()


for j in range(1,total_accounts+1):
    if j >= 1 and j <= 312 or j >= 314 and j <= 504 or j >= 506 and j <= 862:
        BrokenDB = CollectionBrokenUsers.find_one({"UserId": j,})
        FixedDB = CollectionFixedUsers.find_one({"UserId": j})
        CurrentDB = CollectionCurrentUsers.find_one({"UserId": j})
        FixedPointsCount = FixedDB["Wallet"]["Points"]
        BrokenPointsCount = BrokenDB["Wallet"]["Points"]
        CurrentPointsCount = CurrentDB["Wallet"]["Points"]
        FixedKillsCount = FixedDB["Kills"]
        BrokenKillsCount = BrokenDB["Kills"]
        CurrentKillsCount = CurrentDB["Kills"]

        AddPointsforKills = FixedKillsCount - BrokenKillsCount
        NewBalance = AddPointsforKills * 10
        NewBalance = NewBalance + CurrentPointsCount
        
    
        db.Users.update_one(
            { "UserId": j},
            { "$set": {"Wallet.Points": NewBalance}}
        )
    if j >= 863:
        FixedDB = CollectionFixedUsers.find_one({"UserId": j})
        CurrentDB = CollectionCurrentUsers.find_one({"UserId": j})
        CurrentPointsCount = CurrentDB["Wallet"]["Points"]
        CurrentKillsCount = CurrentDB["Kills"]
        NewBalance = CurrentKillsCount * 10
        NewBalance = NewBalance + CurrentPointsCount
        
        db.Users.update_one(
            { "UserId": j},
            { "$set": {"Wallet.Points": NewBalance}}
        )
#print("User:",j,"Points:",NewBalance)



    