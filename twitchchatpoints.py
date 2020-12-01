import json
import os
from datetime import datetime

#Return Code List: 0 - Func1 Success, 1 - Added Points Successfully
#2 - Subtracted Points Successfully, 3 - Failed To Subtract Points
def appendToUserList(user):
    if os.path.exists("scoreboard.json") == True:
        with open("scoreboard.json", "r") as f:
            data = json.load(f)
            data[user] = 0
            os.remove("scoreboard.json")
        with open("scoreboard.json", "w") as f:
            json.dump(data, f)
    else:
        with open("scoreboard.json", "w") as f:
            data = {}
            data[user] = 0
            json.dump(data, f)
    print(f"LOG {datetime.now()}: Successfully Appended User {user} to User List")
    return 0
            
def addPoints(user, points):
    userExists = False
    if os.path.exists("scoreboard.json") == True:
        with open("scoreboard.json", "r") as f:
            data = json.load(f)
            if data[user] != None:
                print(f"LOG {datetime.now()}: Adding {points} points to {user}'s total readout...")
                curPoints = int(data[user])
                curPoints += points
                data[user] = curPoints
                print(f"LOG {datetime.now()}: Successfully added points to {user}'s readout... Removing original file...")
                userExists = True
                os.remove("scoreboard.json")
                print(f"LOG {datetime.now()}: Successfully removed original file... Adding new file...")
                return 1
            else:
                print(f"LOG {datetime.now()}: Err - User not in list! Adding user to list...")
                userExists = False

        if userExists == True:
            with open("scoreboard.json", "w") as f:
                json.dump(data, f)
                print(f"LOG {datetime.now()}: Successfully added updated file!")
        else:
            appendToUserList(user)

    else:
        print(f"LOG {datetime.now()}: Err - scoreboard file not found in expected location... Creating new file...")
        appendToUserList(user)

def removePoints(user, points):
    userExists = False
    if os.path.exists("scoreboard.json") == True:
        with open("scoreboard.json", "r") as f:
            data = json.load(f)
            if data[user] != None:
                if int(data[user]) - points >= 0:
                    print(f"LOG {datetime.now()}: Subtracting {points} points from {user}'s total readout...")
                    curPoints = int(data[user])
                    curPoints -= points
                    data[user] = curPoints
                    print(f"LOG {datetime.now()}: Successfully subtracted points from {user}'s readout... Removing original file...")
                    userExists = 1
                    os.remove("scoreboard.json")
                    print(f"LOG {datetime.now()}: Successfully removed original file... Adding new file...")
                else:
                    userExists = 2
                    print(f"LOG {datetime.now()}: Err - could not subtract points from user (Reason: Negative Readout Detected)")
            else:
                print(f"LOG {datetime.now()}: Err - User not in list! Adding user to list...")
                userExists = 0

        if userExists == 1:
            with open("scoreboard.json", "w") as f:
                json.dump(data, f)
                print(f"LOG {datetime.now()}: Successfully added updated file!")
                return 2
        elif userExists == 0:
            appendToUserList(user)
        else:
            print(f"LOG {datetime.now()}: File update cancelled.")
            return 3

    else:
        print(f"LOG {datetime.now()}: Err - scoreboard file not found in expected location... Creating new file...")
        appendToUserList(user)
                
