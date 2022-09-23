import requests
import json
import datetime

def caller():
    today = str(datetime.date.today())
    gluedjason = ""
    r = requests.get("https://leetcode.com/problemset/all/")
    load = r.text
    load = r.text.split(',')
    for i in range(len(load)):
        if 'state\":{\"data\":{\"dailyCodingChallengeV2\":{' in load[i]:
            result = load[i+1:]
            first = load[i]
    full = first
    for g in range(len(result)):
        full = full + "," + result[g]
    jason = json.loads(json.dumps([full]))
    splitjason = jason[0].split(",")
    for mess in range(len(splitjason)):
        if today in splitjason[mess]:
            if gluedjason == "":
                gluedjason = splitjason[mess:mess+5]
    problemlink = gluedjason[2].split(":")[1].replace('"', "")
    problemid = gluedjason[3].split(":")[2].replace('"', "")
    title = gluedjason[4].split(":")[1].replace('"', "")
#print(today, problemid + ".", title, "https://leetcode.com" + problemlink)
    return today + " " + problemid + ". " + title + " " +  "https://leetcode.com" + problemlink
