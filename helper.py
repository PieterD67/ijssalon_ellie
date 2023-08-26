def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()


def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen
    bedrag_pp = "??"
    return f"Het bedrag per persoon is {bedrag_pp} euro"


def onderstreep(tekst=""):
    uit=[]
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

# Les 10 vraag 3

def som(ink):
    totaal= sum(ink.values())
    return(totaal)





