#------------------------------------------------
#purpose: grab webmap itemid from list of netview apps
#py ver:    3.x
#---------------------------
import urllib.request, json, csv


apps = {
    "1":"nvge",
    "2":"nvcu",
    "3":"nvop",
    "4":"nvms",
    "5":"nvin",
    "6":"nvpr",
    "7":"nvwo",
    "8":"nvmd",
    "9":"nvdt"
}

env = {
    "dev":"wsldctdgweb",
    "test":"wsldcttgweb",
    "prod":"wsldctpgweb"
    }

with open('group1_webmap_itemId.csv','a',newline='') as wrtieFile:
    writer = csv.writer(wrtieFile)
    writer.writerow(["ENV","CODE","SUBTITLE","APPNAME","ITEMID","DOMAIN"])
    

for e in env:
    source = e
    for a in apps:
        link = "https://{0}.water.internal/nview/appconfig/{1}.json".format(env.get(e),apps.get(a))
        with urllib.request.urlopen(link) as url:
            data = json.loads(url.read().decode())
            print("    title: ", data["title"])
            print("    subtitle: ", data["subtitle"])
            print("    itemId: ", data["map"]["itemId"])
            print("    code: ", apps.get(a))
            print("    domain: ", env.get(e))
            print("")

            row = [source, apps.get(a), data["subtitle"], data["title"], data["map"]["itemId"],env.get(e)]
            #print (row)
            with open('group1_webmap_itemId.csv','a',newline='') as wrtieFile:
                writer = csv.writer(wrtieFile)
                writer.writerow(row)
            


                    














