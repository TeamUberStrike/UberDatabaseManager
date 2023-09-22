from pymongo import MongoClient

client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")
db = client.admin
collection = db["FixedUsers"]
collection2 = db["BrokenUsers"]
collection3 = db["Users"]

result = db.Users.find()
total_accounts=len(list(result))
AwardWinners = [2, 5, 13, 69, 71, 114, 118, 140, 224, 491, 555, 670, 815]

for i in AwardWinners:
    print("Cmid:",i)
    BrokenDB = collection2.find_one({"UserId": i,})
    FixedDB = collection.find_one({"UserId": i})
    FixedPointsCount = FixedDB["Wallet"]["Points"]
    BrokenPointsCount = BrokenDB["Wallet"]["Points"]
    
    AwardPoints = BrokenPointsCount + 50000

    db.BrokenUsers.update_one(
        {"UserId": i},
        { "$set": {"Wallet.Points": AwardPoints}}
    )

for j in range(1,total_accounts+1):
    print("Cmid:",j)
    if j >= 1 and j <= 312 or j >= 314 and j <= 504 or j >= 506 and j <= 862:
        BrokenDB = collection2.find_one({"UserId": j,})
        FixedDB = collection.find_one({"UserId": j})
        CurrentDB = collection3.find_one({"UserId": j})
        FixedPointsCount = FixedDB["Wallet"]["Points"]
        BrokenPointsCount = BrokenDB["Wallet"]["Points"]
        CurrentPointsCount = CurrentDB["Wallet"]["Points"]
        FixedKillsCount = FixedDB["Kills"]
        BrokenKillsCount = BrokenDB["Kills"]

        Kills = FixedKillsCount - BrokenKillsCount
        NewBalance = Kills * 10
        NewBalance = NewBalance + CurrentPointsCount
        
        db.TestUser.update_one(
            { "UserId": j},
            { "$set": {"Wallet.Points": NewBalance}}
        )
    
    