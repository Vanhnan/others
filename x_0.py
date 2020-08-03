doska = {"ust_sol":"", "ust_orto":"", "ust_on":"",
        "orto_sol":"", "orto_orto":"", "orto_on":"",
         "pas_sol":"", "pas_orto":"", "pas_on":""
         }

def doska_tart():
    print(doska["ust_sol"]+" | "+doska["ust_orto"]+" | "+doska["ust_on"])
    print("===========")
    print(doska["orto_sol"]+" | "+doska["orto_orto"]+" | "+doska["orto_on"])
    print("===========")
    print(doska["pas_sol"]+" | "+doska["pas_orto"]+" | "+doska["pas_on"])


doska_tart()

for i in range(9):
    x = input("X твой ход ")
    doska[x]="X"
    o = input("0 твой ход ")
    doska[o]="O"
    doska_tart()
