
def CoutDelta(d):
    for x in d:
        print(x)
    print()

def CoutDrum(d,stare):
    for v in d:
        print(str(v[0])+v[1] + " : ", end=" ")
    print(str(stare)+"\n")


cin = open("graf.in","r")
nrStari= int(cin.readline())
StariFinale = set(int(x) for x in cin.readline().split()) #folosim set pentru nodurile de stari finale

#citim matricea pentru construirea modelului

delta = [{} for i in range(nrStari)]

for i in cin:
    i = i.split()
    i[0]=int(i[0])                  #|
    i[2]=int(i[2])                  #|
    if i[1] not in delta[i[0]]:     #| facem matricea delta cu 3 coloane
        delta[i[0]][i[1]]= i[2]     #|

cin.close()

fin = open("cuvant.in","r")
word= fin.readline().strip()
fin.close()

stare=0
ok=True
path = []
i=0
while i < len(word) and ok:
    c = word[i]
    if c in delta[stare]:
        path.append((stare,c))
        stare=delta[stare][c]
    i+=1

if ok == False or stare not in StariFinale:
    print("Neacceptat!")
else:
    print("Acceptat!Drumul este:")
    CoutDrum(path,stare)