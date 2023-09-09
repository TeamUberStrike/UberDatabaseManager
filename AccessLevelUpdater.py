from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

Default = 0
QA = 3
Moderator = 4
ModeratorHidden = 5
SeniorQA = 6
SeniorModerator = 7
SeniorModeratorHidden = 9
Admin = 10

client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")
db = client.admin

result = db.users.find()

total_accounts = len(list(result))

cmid = 2 #Enter Cmid for User

cmidAccess = Moderator #Enter Access Level from Enum Above

db.Users.update_one(
    {"UserId": cmid}, { "$set": { "Profile.AccessLevel": cmidAccess}}
)

if cmidAccess == 10:
    Role = "Admin"
elif cmidAccess == 9:
    Role = "Senior Moderator Hidden"
elif cmidAccess == 7:
    Role = "Senior Moderator"
elif cmidAccess == 6:
    Role = "Senior QA"
elif cmidAccess == 5:
    Role = "Moderator Hidden"
elif cmidAccess == 4:
    Role = "Moderator"
elif cmidAccess == 3:
    Role = "QA"
else:
    Role = "Default"

print("Cmid:",cmid,"has been given",Role,"Access!") 
