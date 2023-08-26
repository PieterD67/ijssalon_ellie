mijn_dict = {
    "vis" : 10,
    "vlees" : 25,
    "overig" : 15,
}

def presenteer(a,totaal):
    totaal = sum(a.values())
    for k, v in a.items():
        print (k,": ", v, "euro")
    is_gelijk = 26
    print(is_gelijk * "=")
    print ("totaal : ", totaal,"euro")

    

