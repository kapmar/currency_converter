#ftiakse ena programma to opoio tha exei ena function me onoma convert_currency to opoio tha dexetai 2 arguments
# to proto argument tha nai to poso twn eurw kai to deutero to nomisma pou theleis na ginetai i allagi
#to function tha elegxei ean o xristis edwse 1 apo ta 3 nomismata UK USD,YEN, kai tha kanei tis antistoixes metatropes
# se alli periptosi tha anaferei oti to sygkekrimeno nomisma den upostirizetai.
#telos meta tin metatropi tha rotaei ton xristh ean thelei na kanei alli metatropi kai ean oxi tha termatizei
#alliws tha ksana zita apto xristi na dwsei poso kai nomisma

def convert_currency(euro, metatropi):
    if metatropi == "uk":
        print(euro / 1.25)
    elif metatropi == "usd":
        print(euro / 0.95)
    elif metatropi == "yen":
        print(euro / 0.46)
    else:
        print("to nomisma den upostirizetai")

x = 0
while x == 0:
    poso = input("posa thelete na metatrepsete?: ")
    nomisma = input("se ti nomisma tha thelate na metatrepsete?(uk/usd/yen): ")
    convert_currency(float(poso), nomisma)
    y = 0
    while y == 0: 
        pisw_eksodos = input("thelete na kanete allh metatroph?(nai/oxi): ")
        if pisw_eksodos == "oxi" or "OXI":
            y = 1
            x = 1
        elif pisw_eksodos == "nai" or "NAI":
            y = 1
        else:
            print("NAI H OXI RE MALAKA")
    
