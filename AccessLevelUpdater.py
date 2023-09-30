from pymongo import MongoClient

client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")
db = client.admin

result = db.users.find()

total_accounts = len(list(result))
#Roles
Default = 0
QA = 3
Moderator = 4
SeniorQA = 6
Developer = 6
SeniorModerator = 7
Admin = 10

#Shirts
AdminShirt = 1037
BetaHeroShirt = 1038
GlobalModShirt = 1040
ModShirt = 1041
QAShirt = 1042

Cmids = [39] #Enter Cmids for Users to Update [1, 2, 13]

CmidsAccessLevels = SeniorQA #Enter Access Level list above.
for Cmid in Cmids:
    db.Users.update_one(
        {"UserId": Cmid}, 
        { "$set": { 
            "Profile.AccessLevel": CmidsAccessLevels}} 
    )
    AddShirts = True
    GetUser = db.Users.find_one({"UserId": Cmid})
    Name = GetUser["Profile"]["Name"]
    match CmidsAccessLevels:
        case 10:
            UserRole = "Admin"
            ShirtstoAdd = [AdminShirt]
        case 7:
            UserRole = "Senior Moderator"
            ShirtstoAdd = [GlobalModShirt, ModShirt]
        case 6:
            UserRole = "Senior QA"
            ShirtstoAdd = [QAShirt]
        case 4:
            UserRole = "Moderator"
            ShirtstoAdd = [ModShirt]
        case 3:
            UserRole = "QA"
            ShirtstoAdd = [QAShirt]
        case _:
            UserRole = "Default"
            AddShirts = False
        
    

    if AddShirts == True:
        print(f"User: {Cmid} with Name: {Name} has been given {UserRole} Access and will receive the following shirts!")
        for ItemId in ShirtstoAdd:
            db.Users.update_one(
                {"UserId": Cmid},
                { "$addToSet": { "Inventory" : 
                    {
                        "AmountRemaining": -1,
                        "Cmid": Cmid,
                        "ExpirationDate": None,
                        "ItemId": ItemId
                    }
                }}
            )
            match ItemId:
                case 1037:
                    Shirt = "Admin Shirt"
                case 1038:
                    Shirt = "Beta Hero Shirt"
                case 1040:
                    Shirt = "Global Moderator Shirt"
                case 1041:
                    Shirt = "Moderator Shirt"
                case 1042:
                    Shirt = "QA Shirt"
            print(Shirt)
    else:
        print(f"User: {Cmid} with Name: {Name} has been given {UserRole} Access!")

            


            
