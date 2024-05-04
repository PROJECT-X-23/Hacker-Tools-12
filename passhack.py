import random
from secrets import choice


print("ecco aperto aircrack cosa posso fare?")
print("digita '1' se vuoi hackerare un pass wifi '2' se vuoi i crediti")
sceltainiziale = input()
if sceltainiziale == '1':
    print("ecco qua le reti disponibili")
    retidispo = ('fast-RDOO9', 'VODAFONE-A9O00I', 'TIM', 'aircrack.crack')
    print(retidispo)
    print("ora per hackerare una pass di una rete wifi deve inserire la parola chiave qualè")
    sceltarete = input()
    if sceltarete == 'aircrack.crack':
        print("va bene qui trovi LISSD")
        LISSID = ('23y7', '45opt9', 'gegdeg647')
        print(random.choice(LISSID))
        print("inserisci LISSD per hackerare e trovare la password")
        LSSDin = input()
        if LSSDin == (LISSID):
            print("ok ecco la tua password")
        passkey = ('pass324978', 'DULX36QGCD', 'Pass9898')
        print(random.choice(passkey))
        print("premi esci per uscire")
        uscita1 = input()
    else:
        print("non è corretto")



else:
    print("creato da anonimus")
    print("inserire invio per uscir3")
    uscita = input()
        
        











   