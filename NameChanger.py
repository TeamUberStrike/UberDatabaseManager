from profile import Profile
from pymongo import MongoClient

client = MongoClient("mongodb://uber:admin@localhost:27017/?authMechanism=SCRAM-SHA-1&authSource=admin")
db = client.admin

Cmid = 525

NameChange = "I am Cheater"

CurrentUser = db.Users.find_one({"UserId": Cmid})
CurrentName = CurrentUser["Profile"]["Name"]
db.Users.update_one(
    {"UserId": Cmid},
    { "$set": 
        { "Profile.Name": NameChange }
    }
)
db.Users.update_one(
    {"UserId": Cmid},
    { "$addToSet" : 
     { "Names": CurrentName }
    },
    upsert=True  
)

print("User", {Cmid}, "successfully changed their name from", [CurrentName], "to", [NameChange])