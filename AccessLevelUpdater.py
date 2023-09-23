from pymongo import MongoClient

client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")
db = client.admin

result = db.users.find()

total_accounts = len(list(result))

Default = 0
QA = 3
Moderator = 4
SeniorQA = 6
SeniorModerator = 7
Admin = 10

Cmids = [1] #Enter Cmids for Users to Update [1, 2, 13]

CmidsAccessLevels = Admin #Enter Access Level list above.
for Cmid in Cmids:
    db.Users.update_one(
        {"UserId": Cmid}, 
        { "$set": { 
            "Profile.AccessLevel": CmidsAccessLevels}}
        
    )
    GetUser = db.Users.find_one({"UserId": Cmid})
    Name = GetUser["Profile"]["Name"]
    if CmidsAccessLevels == 10:
        UserRole = "Admin"
    elif CmidsAccessLevels == 7:
        UserRole = "Senior Moderator"
    elif CmidsAccessLevels == 6:
        UserRole = "Senior QA"
    elif CmidsAccessLevels == 4:
        UserRole = "Moderator"
    elif CmidsAccessLevels == 3:
        UserRole = "QA"
    else:
        UserRole = "Default"
    print({Cmid},Name,"has been given",UserRole,"Access!") 
