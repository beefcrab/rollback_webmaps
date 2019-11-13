#-----------------------------------------------------------------------------
# WTF is this shiz?:   * rollback list of webmaps in case Steve screws up
# Who wrote this crap?  :Slau
#-----------------------------------------------------------------------------

from arcgis.gis import GIS
from arcgis.gis import Item
import arcgis.mapping

##PARAMETERS

#ENV:
DEV  = "wsldctdgweb.water.internal/portal/"
TEST = "wsldcttgweb.water.internal/portal/"
PROD = "wsldctpgweb.water.internal/portal/"
AGOL = "arcgis.com"

#list of items to transfer
#DEV
rollBackListDEV = {
##    'nvge':{"name":"Netview General",                 "source":"4e4a6d54ff60462888c046805bfa888a",  "destination":""},
##    'nvcu':{"name":"Netview for Customer",            "source":"ea94dc8ffa86488eac3dc4ffe7490666",  "destination":""},
##    'nvop':{"name":"Netview for Operations",          "source":"1baf49046fd5482098de330b8ef1f88d",  "destination":"6f570f80c4b1469cbcb3b07d9adf53b0"}
##    'nvms':{"name":"Netview for MSN",                 "source":"b570377b6e50448aae9040d69f757d1e",  "destination":""},
##    'nvin':{"name":"Netview for Planning",            "source":"a87d625d6df44955a982928293481671",  "destination":""},
##    'nvpr':{"name":"Netview for Property",            "source":"a8e8c13232b44cebadb66d18cd92e3e7",  "destination":""},
##    'nvdt':{"name":"Netview for Developer Services",  "source":"20b3c724258947ccba95f5ad3be57a8c",  "destination":""},
##    'nvmd':{"name":"Netview for Major Developments",  "source":"f24b6693818c4724995b36dfff1614b1",  "destination":""},
##    'nvwo':{"name":"Netview for Worksover",           "source":"57f6c1744b3d4085ab24ca82f55206a3",  "destination":""}
    }

#TEST
rollBackListTEST = {
##    'nvge':{"name":"Netview General",                 "source":"64cbd89bed4643bd9517f5f19ecf4402",  "destination":"fcb97e5c8c5d4d3ca11aa39be1263d69"},
##    'nvcu':{"name":"Netview for Customer",            "source":"b5848da15113459c884a4a0d16b2beb0",  "destination":"6803dfc79f6944d68e8160d9bb0c27ab"},
##    'nvop':{"name":"Netview for Operations",          "source":"6237748f1f4e4d78b650944acda9ce0f",  "destination":"1a913175fa7f467db92efb987bea2bc3"},
##    'nvms':{"name":"Netview for MSN",                 "destination":"9c8bd3d73d984ab8b05475bdea665b57",  "source":"7a730c0d627342ab8e79e193c3cee007"},
##    'nvin':{"name":"Netview for Planning",            "source":"7634844c7335467abee40653940963ed",  "destination":"eefd8ef0ac974036a8dda3593b587ada"},
##    'nvpr':{"name":"Netview for Property",            "source":"cbd6c0149cf04275afd5d69a512dca3b",  "destination":"883a23f063c14b87a33815c7aece9e85"},
##    'nvdt':{"name":"Netview for Developer Services",  "source":"2f91f928e1d84a35a67dbd64ac3770b1",  "destination":"d72f8c0415eb432fa7bbc4973020a579"},
##    'nvmd':{"name":"Netview for Major Developments",  "source":"1b731a9079f542798f3b90ce935f0311",  "destination":"b4e4726fd0bd409689e57173ec70d2c2"},
##    'nvwo':{"name":"Netview for Worksover",           "source":"6ef1f788d1b74ae5b11f889bac781148",  "destination":"cd5bca4d8e3e40b7899d47f9e394b2df"}
    }

#PROD
rollBackListPROD = {
##    'nvge':{"name":"Netview General",                 "source":"01466cdb5be841dd889a47b091bf461d",  "destination":"d9afc1e2ad6948e58dadedf6e49db3ae"},
##    'nvcu':{"name":"Netview for Customer",            "source":"99e0c8d5361c41c68b024b47fcd0ad0b",  "destination":"f1dd7875b748426fb631b272607f5146"},
    'nvop':{"name":"Netview for Operations",          "source":"ee47835831014091a688274020e5ec4a",  "destination":"7d09ca16482643f6ad29b32cd28c6ca9"}
##    'nvms':{"name":"Netview for MSN",                 "source":"4b51ca66a6184e15bb7454c11a077fc7",  "destination":"ae846eaf833446d28f7ae7e6ee5542ac"},
##    'nvin':{"name":"Netview for Planning",            "source":"42adbd692d2d4271a9f6e7ab8c302800",  "destination":"93c3ab0a065544eba7fc8e5bc791d58f"},
##    'nvpr':{"name":"Netview for Property",            "source":"239e11492d2942debbab6c4c8ad8190d",  "destination":"3f025412952d427cb4b532f9342ac2f4"},
##    'nvdt':{"name":"Netview for Developer Services",  "source":"217882f274d04ee8953e0f8d50b6e65d",  "destination":"1a9224c4630348318e9289c1ac7cfd39"},
##    'nvmd':{"name":"Netview for Major Developments",  "source":"7f134260b8a44286a6b6bf3a0cb4162c",  "destination":"08f728b26c20488184cadd336c948ce3"},
##    'nvwo':{"name":"Netview for Worksover",           "source":"2b92642a9b8b41e7a3b8f0ce0b2f3886",  "destination":"11f9469105aa41598e56c44e9821548d"}
    }

#AGOL
rollBackListAGOL = {
    }


##WEBMAP PARAMETERS :
#source:
src = PROD
src_admin = ""
src_admin_pwd = ""
src_owner = ""

#if you only want a print out of the items, = True. If transferring the items, = False
readOnly = False
rollBackList = rollBackListPROD

##FUNCTIONS
def transfer(src, des):
    opsLayers = src.get_data()['operationalLayers']
    mapDestObj = arcgis.mapping.WebMap(des)
    mapDestObj.definition['operationalLayers'] = opsLayers
    mapDestObj.update()

##BS BEGINS
portal = GIS("https://" + src, src_admin, src_admin_pwd, verify_cert=False)
print(portal)

#loop through dictionary
for i in rollBackList:
    #define variables
    srcId = rollBackList[i]['source']
    desId = rollBackList[i]['destination']
    srcMap = Item(portal, srcId)
    destMap= Item(portal, desId)
    
    #print actions to check, if destination and source titels are different... you'll be fired
    print("-------------------------")
    print(rollBackList[i]['name'])
    print("-------------------------")
    print(" Source item title:      " + srcMap.title)
    print(" Destination item title: " + destMap.title)
    print("    SOURCE:      " + srcId)
    print("    DESTINATION: " + desId)

    #transfer begins
    if readOnly == False:
        transfer(srcMap,destMap)
        print ("    Transfer Complete for this item")
    elif readOnly == True:
        print ("    READ ONLY: No edits were done to this item")

##JOB COMPLETE
print ("")
print ("--------------------------Script complete---------------------------------")
if readOnly == False:
    print (" In total, " + str(len(rollBackList)) + " item(s) has been processed")
elif readOnly == True:
    print (" In total, " + str(len(rollBackList)) + " item(s) has been printed")








