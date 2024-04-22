import requests
ril = "https://games.roblox.com/v1/games?universeIds="
def get_data(id):
    url=f"https://games.roblox.com/v2/groups/{str(id)}/games?accessFilter=Public&cursor=&limit=50&sortOrder=Desc"
    universeids=[]
    for _ in requests.get(url).json()["data"]:
        universeids.append(_["id"])
    data = {"visit": 0, "fav": 0, "plr": 0}
    for uid in universeids:
        response = requests.get(ril + str(uid)).json()["data"][0]
        data["visit"] += response["visits"]
        data["fav"] += response["favoritedCount"]
        data["plr"] += response["playing"]
    return data
print(get_data(16982915))