import random


print("benevenuto nell sqlcracker cosa vuoi fare?")
print("digita '1' se vuoi craccare server")
sceltainiziale = input()
if sceltainiziale == '1':
    print("ok iniziamo")
    print("ora se vuole hackerare un server deve prendere un ip iniziamo?")
    print("iniziamo allora il suo ip è")
    ip = ('153.244.203.133', '9.20.119.221', '253.253.222.190', '240.164.137.137', '93.68.211.46')
    print(random.choice(ip))
    print("allora per hackerare il sql deve inserire la parola?")
    sceltaip = input()
    if sceltaip == 'h4ck.exe':
        print("ok corretto")
        print("la pass del server ip sql è:")
        squlpass = ('passhhdhhd', '52477cachetube5171childrenthirdwho')
        print(random.choice(squlpass))
        print("ora ha craccato anche la password del server")
        print("premi esci per usc1r3")
        uscita = input()

else:
    print("non è corretto")
