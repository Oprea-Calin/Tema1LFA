
def CoutDelta(d):
    for x in d:
        print(x)
    print()

def CoutDrum(d,stare):
    for v in d:
        print(str(v[0])+v[1] + " : ", end=" ")
    print(str(stare)+"\n")
    print()


cin = open("graf.in","r")

#Citim numarul total de noduri de stari

nrStari= int(cin.readline())

#folosim set pentru nodurile de stari finale

StariFinale = set(int(x) for x in cin.readline().split())

#citim matricea pentru construirea modelului

delta = [{} for i in range(nrStari)]

for i in cin:
    i = i.split()
    i[0]=int(i[0])                                              #|
    i[2]=int(i[2])                                              #|
    if i[1] not in delta[i[0]]:                                 #| completa matricea delta cu 3 coloane cu informatiile corespunzatoare muchiilor dintre nodurile de stari
        delta[i[0]][i[1]]= i[2]                                 #|

cin.close()


#Citim cuvantul pentru verificare

fin = open("cuvant.in","r")
word= fin.readline().strip()
fin.close()

#Verificam daca cuvantul este acceptat, caracter cu caracter si construim drumul pentru a-l afisa daca este acceptat

stare=0
ok=True
path = []
i=0
while i < len(word) and ok:
    c = word[i]
    if c in delta[stare]:
        path.append((stare,c))
        stare=delta[stare][c]
    else:
        ok=False                                                #folosim ok sa verificam daca la fiecare pas, caracterul luat se afla sau nu in delta (matricea de cu muchiile dintre nodurile de stari)
        i=len(word)+1
    i+=1

#Daca cuvantul este acceptat, afisam drumul parcurs

if ok == False or stare not in StariFinale:
    print("Neacceptat!")
else:
    print("Acceptat! Drumul este:")
    CoutDrum(path,stare)

#Pentru afisarea AFD:

print("AFD: ")
CoutDelta(delta)