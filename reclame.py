from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-(prijs*korting)} euro."
    return uitvoer

def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for i in inkomsten:
        totaal += i
    return (f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal*btw} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    return laag,hoog

def gemiddelde(mijn_lijst):
    import statistics
    return (f"De gemiddelde inkomsten van deze week zijn {statistics.mean(mijn_lijst)} euro.")

def meervoudig(invoer_lijst):
    hoog = max(invoer_lijst)
    laag = min(invoer_lijst)
    return laag,hoog

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer
