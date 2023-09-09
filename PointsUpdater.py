from pymongo import MongoClient
import json
client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")

db = client.admin
collection = db["FixedUsers"]
collection2 = db["BrokenUsers"]
collection3 = db["Users"]
result = db.Users.find()

total_accounts=len(list(result))
print("Total accounts Database", total_accounts)

for i in range(506,total_accounts+1): #Only 864 Accounts in Old Database
    if i >= 1 and i <= 843:
        CurrentUser = collection.find_one({"UserId": i})
        CurrentUser2 = collection2.find_one({"UserId": i})
        CurrentUser3 = collection3.find_one({"UserId": i})
        CurrentUserName = CurrentUser["Profile"]["Name"]
        CurrentUserKillsCount = CurrentUser["Kills"]
        CurrentUserKillsCount2 =CurrentUser2["Kills"]
        points_balance_current = CurrentUser3["Wallet"]["Points"]

        print("{", i,"}", "Name: ", CurrentUserName)
       # if CurrentUser and "Wallet" in CurrentUser:
       #     points_balance = CurrentUser["Wallet"]["Points"]
       #     print("Fixed Database Points: ", points_balance)

       # if CurrentUser2 and "Wallet" in CurrentUser2:
       #     points_balance_old = CurrentUser2["Wallet"]["Points"]
       #     print("Broken Database Points: ", points_balance_old)

        CurrentUserKillsDifference = CurrentUserKillsCount - CurrentUserKillsCount2
    
        # print("There is ", CurrentUserKillsDifference, "More kills in the New Database")
    
        PointBalanceMultiplier = CurrentUserKillsDifference * 10
    
        print("User",CurrentUserName, "will receive",PointBalanceMultiplier,"extra points added to their balance.")
        
        #if points_balance_old >= points_balance:

        #    NewPointsBalance = points_balance_old + PointBalanceMultiplier
        
        # print("Point Balance: ", NewPointsBalance)
       
        #else:
    
        #    NewPointsBalance = points_balance + PointBalanceMultiplier
        NewPointsBalance = points_balance_current + PointBalanceMultiplier
        print("Point Balance: ", NewPointsBalance)

    elif i >= 864:
        CurrentUser = collection3.find_one({"UserId": i})
        CurrentUserName = CurrentUser["Profile"]["Name"]
        CurrentUserKillsCount = CurrentUser["Kills"]
        if CurrentUser and "Wallet" in CurrentUser:
            points_balance = CurrentUser["Wallet"]["Points"]
        
        NewPointsBalance = points_balance + CurrentUserKillsCount * 10

        print("User",CurrentUserName, "Points Balance will be set to",NewPointsBalance)
    
    db.Users.update_one(

        {"UserId": i},
        { "$set": { "Wallet.Points": NewPointsBalance}}
    )