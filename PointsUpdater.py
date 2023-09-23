from pymongo import MongoClient

client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")
db = client.admin
CollectionFixedUsers = db["FixedUsers"]
CollectionBrokenUsers = db["BrokenUsers"]
CollectionCurrentUsers = db["Users"]

result = db.Users.find()
total_accounts=len(list(result))
AwardWinners = [2, 5, 13, 69, 71, 114, 118, 140, 224, 491, 555, 670, 815, 883]

#for i in range(1,total_accounts+1):
for i in AwardWinners:
    print("Cmid:",i)
    BrokenDB = CollectionBrokenUsers.find_one({"UserId": i,})
    FixedDB = CollectionFixedUsers.find_one({"UserId": i})
    FixedPointsCount = FixedDB["Wallet"]["Points"]
    BrokenPointsCount = BrokenDB["Wallet"]["Points"]
    
    AwardPoints = BrokenPointsCount + 50000

   # AwardBalanceUsed = AwardPoints - FixedPointsCount

   # print("Cmid:",{i},"Used",AwardBalanceUsed,"Points.")
    db.BrokenUsers.update_one(
        {"UserId": i},
        { "$set": {"Wallet.Points": AwardPoints}}
    )

for j in range(1,total_accounts+1):
    print("Cmid:",j)
    if j >= 1 and j <= 312 or j >= 314 and j <= 504 or j >= 506 and j <= 894:
        BrokenDB = CollectionBrokenUsers.find_one({"UserId": j,})
        FixedDB = CollectionFixedUsers.find_one({"UserId": j})
        CurrentDB = CollectionCurrentUsers.find_one({"UserId": j})
        FixedPointsCount = FixedDB["Wallet"]["Points"]
        BrokenPointsCount = BrokenDB["Wallet"]["Points"]
        CurrentPointsCount = CurrentDB["Wallet"]["Points"]
        FixedKillsCount = FixedDB["Kills"]
        BrokenKillsCount = BrokenDB["Kills"]
        CurrentKillsCount = CurrentDB["Kills"]
    
        AccountBalanceUsed = BrokenPointsCount - FixedPointsCount
        print("Balance Used w/o Adding New Kills.",AccountBalanceUsed)
        KillsforPointsAdded = FixedKillsCount - BrokenKillsCount
        KillsAddedBalance = KillsforPointsAdded * 20
        BalancebeforeLive = KillsAddedBalance + CurrentPointsCount
        print("Balance w/ New Kills",BalancebeforeLive)
        LiveBalance = BalancebeforeLive + AccountBalanceUsed
        print("Live Balance",LiveBalance)
       # db.TestUser.update_one(
       #     { "UserId": j},
       #     { "$set": {"Wallet.Points": LiveBalance}}
       # )
    if j >= 894 and j <=1915:
        FixedDB = CollectionFixedUsers.find_one({"UserId": j})
        CurrentDB = CollectionCurrentUsers.find_one({"UserId": j})
        CurrentPointsCount = CurrentDB["Wallet"]["Points"]
        FixedPointsCount = FixedDB["Wallet"]["Points"]
        CurrentKillsCount = CurrentDB["Kills"]
        KillsAddedBalance = CurrentKillsCount * 20
        
        AccountBalanceUsed = 10000 - FixedPointsCount
        print("Balance Used:",AccountBalanceUsed)
        LiveBalance = AccountBalanceUsed + CurrentPointsCount + KillsAddedBalance
       # db.Users.update_one(
       #     { "UserId": j},
       #     { "$set": {"Wallet.Points": LiveBalance}}
       # )
        print("User:",j,"Live Balance:",LiveBalance)
    