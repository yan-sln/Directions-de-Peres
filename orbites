from math import *

# On importe nos listes, en valeur exactes grâce au programme convertisseur

D=[[1, 0, 1], [1, 1, 0], [1, -1/2*sqrt(2), -1/2*sqrt(2)], [1, 1/2*sqrt(2), -1/2*sqrt(2)], [1, -1/2*sqrt(2), 1/2*sqrt(2)], [1, 1/2*sqrt(2), 1/2*sqrt(2)], [1, -1/2*sqrt(2), 0], [1, 1/2*sqrt(2), 0], [1, 0, 0], [1, 0, -1/2*sqrt(2)], [1, 0, 1/2*sqrt(2)], [-1, 0, 1], [0, -1, 1], [0, 1, 1], [-1/2*sqrt(2), 0, 1], [1/2*sqrt(2), 0, 1], [0, 0, 1], [0, -1/2*sqrt(2), 1], [0, 1/2*sqrt(2), 1], [-1/2*sqrt(2), -1/2*sqrt(2), 1], [1/2*sqrt(2), -1/2*sqrt(2), 1], [-1/2*sqrt(2), 1/2*sqrt(2), 1], [1/2*sqrt(2), 1/2*sqrt(2), 1], [-1, 1, 0], [-1/2*sqrt(2), 1, 0], [1/2*sqrt(2), 1, 0], [0, 1, 0], [-1/2*sqrt(2), 1, 1/2*sqrt(2)], [-1/2*sqrt(2), 1, -1/2*sqrt(2)], [1/2*sqrt(2), 1, 1/2*sqrt(2)], [1/2*sqrt(2), 1, -1/2*sqrt(2)], [0, 1, -1/2*sqrt(2)], [0, 1, 1/2*sqrt(2)]]

T=[[[1, 0, 1], [-1, 0, 1], [0, 1, 0]], [[1, 0, 1], [-1/2*sqrt(2), 1, 1/2*sqrt(2)], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[1, 1, 0], [0, 0, 1], [-1, 1, 0]], [[1, 1, 0], [1/2*sqrt(2), -1/2*sqrt(2), 1], [-1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [1, 1/2*sqrt(2), 1/2*sqrt(2)], [0, -1, 1]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [1, -1/2*sqrt(2), 1/2*sqrt(2)], [0, 1, 1]], [[1, -1/2*sqrt(2), 0], [0, 0, 1], [1/2*sqrt(2), 1, 0]], [[1, 1/2*sqrt(2), 0], [0, 0, 1], [-1/2*sqrt(2), 1, 0]], [[1, 0, 0], [0, -1, 1], [0, 1, 1]], [[1, 0, 0], [0, 0, 1], [0, 1, 0]], [[1, 0, 0], [0, -1/2*sqrt(2), 1], [0, 1, 1/2*sqrt(2)]], [[1, 0, 0], [0, 1/2*sqrt(2), 1], [0, 1, -1/2*sqrt(2)]], [[1, 0, -1/2*sqrt(2)], [1/2*sqrt(2), 0, 1], [0, 1, 0]], [[1, 0, 1/2*sqrt(2)], [-1/2*sqrt(2), 0, 1], [0, 1, 0]], [[-1, 0, 1], [-1/2*sqrt(2), 1, -1/2*sqrt(2)], [1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[-1/2*sqrt(2), -1/2*sqrt(2), 1], [1/2*sqrt(2), 1/2*sqrt(2), 1], [-1, 1, 0]]]

P=[[[1, 0, 1], [-1, 0, 1]], [[1, 0, 1], [0, 1, 0]], [[1, 0, 1], [-1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[1, 0, 1], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[1, 1, 0], [0, 0, 1]], [[1, 1, 0], [1/2*sqrt(2), -1/2*sqrt(2), 1]], [[1, 1, 0], [-1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1, 1, 0], [-1, 1, 0]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [1, 1/2*sqrt(2), 1/2*sqrt(2)]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [0, -1, 1]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [1/2*sqrt(2), 0, 1]], [[1, -1/2*sqrt(2), -1/2*sqrt(2)], [1/2*sqrt(2), 1, 0]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [1, -1/2*sqrt(2), 1/2*sqrt(2)]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [0, 1, 1]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [1/2*sqrt(2), 0, 1]], [[1, 1/2*sqrt(2), -1/2*sqrt(2)], [-1/2*sqrt(2), 1, 0]], [[1, -1/2*sqrt(2), 1/2*sqrt(2)], [0, 1, 1]], [[1, -1/2*sqrt(2), 1/2*sqrt(2)], [-1/2*sqrt(2), 0, 1]], [[1, -1/2*sqrt(2), 1/2*sqrt(2)], [1/2*sqrt(2), 1, 0]], [[1, 1/2*sqrt(2), 1/2*sqrt(2)], [0, -1, 1]], [[1, 1/2*sqrt(2), 1/2*sqrt(2)], [-1/2*sqrt(2), 0, 1]], [[1, 1/2*sqrt(2), 1/2*sqrt(2)], [-1/2*sqrt(2), 1, 0]], [[1, -1/2*sqrt(2), 0], [0, 0, 1]], [[1, -1/2*sqrt(2), 0], [1/2*sqrt(2), 1, 0]], [[1, -1/2*sqrt(2), 0], [1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[1, -1/2*sqrt(2), 0], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[1, 1/2*sqrt(2), 0], [0, 0, 1]], [[1, 1/2*sqrt(2), 0], [-1/2*sqrt(2), 1, 0]], [[1, 1/2*sqrt(2), 0], [-1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[1, 1/2*sqrt(2), 0], [-1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[1, 0, 0], [0, -1, 1]], [[1, 0, 0], [0, 1, 1]], [[1, 0, 0], [0, 0, 1]], [[1, 0, 0], [0, -1/2*sqrt(2), 1]], [[1, 0, 0], [0, 1/2*sqrt(2), 1]], [[1, 0, 0], [0, 1, 0]], [[1, 0, 0], [0, 1, -1/2*sqrt(2)]], [[1, 0, 0], [0, 1, 1/2*sqrt(2)]], [[1, 0, -1/2*sqrt(2)], [1/2*sqrt(2), 0, 1]], [[1, 0, -1/2*sqrt(2)], [1/2*sqrt(2), -1/2*sqrt(2), 1]], [[1, 0, -1/2*sqrt(2)], [1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1, 0, -1/2*sqrt(2)], [0, 1, 0]], [[1, 0, 1/2*sqrt(2)], [-1/2*sqrt(2), 0, 1]], [[1, 0, 1/2*sqrt(2)], [-1/2*sqrt(2), -1/2*sqrt(2), 1]], [[1, 0, 1/2*sqrt(2)], [-1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1, 0, 1/2*sqrt(2)], [0, 1, 0]], [[-1, 0, 1], [0, 1, 0]], [[-1, 0, 1], [-1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[-1, 0, 1], [1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[0, -1, 1], [0, 1, 1]], [[-1/2*sqrt(2), 0, 1], [0, 1, 0]], [[1/2*sqrt(2), 0, 1], [0, 1, 0]], [[0, 0, 1], [-1, 1, 0]], [[0, 0, 1], [-1/2*sqrt(2), 1, 0]], [[0, 0, 1], [1/2*sqrt(2), 1, 0]], [[0, 0, 1], [0, 1, 0]], [[0, -1/2*sqrt(2), 1], [-1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[0, -1/2*sqrt(2), 1], [1/2*sqrt(2), 1, 1/2*sqrt(2)]], [[0, -1/2*sqrt(2), 1], [0, 1, 1/2*sqrt(2)]], [[0, 1/2*sqrt(2), 1], [-1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[0, 1/2*sqrt(2), 1], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[0, 1/2*sqrt(2), 1], [0, 1, -1/2*sqrt(2)]], [[-1/2*sqrt(2), -1/2*sqrt(2), 1], [1/2*sqrt(2), 1/2*sqrt(2), 1]], [[-1/2*sqrt(2), -1/2*sqrt(2), 1], [-1, 1, 0]], [[-1/2*sqrt(2), -1/2*sqrt(2), 1], [0, 1, 1/2*sqrt(2)]], [[1/2*sqrt(2), -1/2*sqrt(2), 1], [-1/2*sqrt(2), 1/2*sqrt(2), 1]], [[1/2*sqrt(2), -1/2*sqrt(2), 1], [0, 1, 1/2*sqrt(2)]], [[-1/2*sqrt(2), 1/2*sqrt(2), 1], [0, 1, -1/2*sqrt(2)]], [[1/2*sqrt(2), 1/2*sqrt(2), 1], [-1, 1, 0]], [[1/2*sqrt(2), 1/2*sqrt(2), 1], [0, 1, -1/2*sqrt(2)]], [[-1/2*sqrt(2), 1, 1/2*sqrt(2)], [1/2*sqrt(2), 1, -1/2*sqrt(2)]], [[-1/2*sqrt(2), 1, -1/2*sqrt(2)], [1/2*sqrt(2), 1, 1/2*sqrt(2)]]]



# On code toutes les rotations possibles

rotations=[]
x=y=z=0 # Initialisation
while(x<4):
    y=0
    while(y<4):
        z=0
        while(z<4):
            rotations.append([x,y,z])
            z=z+1
        y=y+1
    x=x+1

# On crée maintenant l'ensemble des symétriques

Ds = []
for i in range (len(D)): # Et on crée Ds
    Ds.append([D[i],[-D[i][0],-D[i][1],-D[i][2]]])

# On définit les 3 rotations qui vont générer le groupe des rotations

DRz=[] # rotation de pi/4 selon l'axe z des d dans D
DRy=[] # rotation de pi/4 selon l'axe y des d dans D
DRx=[] # rotation de pi/4 selon l'axe x des d dans D
# On utilise ici la structure ensembliste d'une application
# Les éléments sont des couples [d, DRx(d)]

for i in range(len(D)):
    point=[-(D[i][1]),(D[i][0]),(D[i][2])] # Formules de rotations simples
    for ii in range(len(Ds)):
        if point in Ds[ii]:
            DRz.append([D[i],D[ii]]) # couple [d, DRz(d)]
    point=[(D[i][2]),(D[i][1]),-(D[i][0])] # Formules de rotations simples
    for ii in range(len(Ds)):
        if point in Ds[ii]:
            DRy.append([D[i],D[ii]]) # couple [d, DRy(d)]
    point=[(D[i][0]),(-D[i][2]),(D[i][1])] # Formules de rotations simples
    for ii in range(len(Ds)):
        if point in Ds[ii]:
            DRx.append([D[i],D[ii]]) # couple [d, DRx(d)]

def composition(ga, gb): # On définit l'opération du futur groupe G, ici ga et gb sont 2 éléments de G, on renvoie ga.gb (composition)
    composee=[]
    imagega=[]
    antecedantga=[]
    imagegb=[]
    antecedantgb=[]
    for i in range(len(gb)):
        imagegb.append(gb[i][1])
        antecedantgb.append(gb[i][0])
        imagega.append(ga[i][1])
        antecedantga.append(ga[i][0])
    for i in range(len(D)):
        if D[i] in antecedantgb:
            composee.append([D[i],imagega[antecedantga.index(imagegb[antecedantgb.index(D[i])])]]) # d'abord gb puis ga
    return(composee)

def rot(rotation): # On définit une fonction, qui a une rotation codée [x, y, z] associe un ensemble qui correspond à une application, élément du groupe G
    imD=[]
    for i in range(len(D)):
        imD.append([D[i],D[i]]) # ce qui deviendra notre element neutre
    for i in range(rotation[0]):
        imD=composition(DRx,imD)
    for i in range(rotation[1]):
        imD=composition(DRy,imD)
    for i in range(rotation[2]):
        imD=composition(DRz,imD)
    return(imD) # on retourne une application de D vers D, c'est à dire un ensemble de paires de p et p' dans D
    
G=[] # G sera le groupe des rotations qu'on s'efforce de construire
g=[] # g un élément de G, c'est à dire une application de D vers D, c'est-à-dire un ensemble de paires de p et p' dans D
for i in range(len(rotations)):
    g=rot(rotations[i])
    if not g in G : # On ne met dans G que les g qui n'y sont pas encore 
        G.append(g)
print("On a trouve ",len(G)," isometries positives") # Le programme retourne 24 ; on a bien trouvé l'ensemble des 24 isométries positives du cube.



# On cherche maintenant à trouver les orbites de D sous l'action de G:
def Phi(g, p):# On définit la fonction qui fait agir G sur D
    for i in range(len(g)):
        if g[i][0]==p:
            return(g[i][1])

for i in range(len(D)): # On teste la première condition
    if Phi(G[0],D[i])!=D[i]:
        print("OULALALALALALALA (i)",Phi(G[0],D[i]),"   ",D[i])
        

for i in range(len(G)): # On teste la deuxième condition
    for ii in range(len(G)):
        for iii in range(len(D)):
            if Phi(composition(G[i],G[ii]),D[iii])!=Phi(G[i],Phi(G[ii],D[iii])):
                print("OULALALALALALALA (ii)",Phi(composition(G[i],G[ii]),D[iii]),"   ",Phi(G[i],Phi(G[ii],D[iii])))
# Le programme n'affiche aucun 'OULALALALALALALA', notre fonction Phi définit bien une action de groupe !!!!

orbitesMultiples=[]
for i in range(len(D)):
    orbitesMultiples.append([])
for i in range(len(D)):
    for ii in range(len(D)):
        for iii in range(len(G)):
            if Phi(G[iii],D[ii])==D[i]:
                if not D[ii] in orbitesMultiples[i]:
                    orbitesMultiples[i].append(D[ii])

orbitesD=[]
for i in range(len(orbitesMultiples)):
    if not orbitesMultiples[i] in orbitesD:
        orbitesD.append(orbitesMultiples[i])

print("il y a ",len(orbitesD)," orbites")



# On cherche maintenant à trouver les orbites de T sous l'action de G:
def Xhi(g, t):# On définit la fonction qui fait agir G sur T
    imaget=[[],[],[]]
    for i in range(len(g)):
        if g[i][0]==t[0]:
            imaget[0]=g[i][1]
    for i in range(len(g)):
        if g[i][0]==t[1]:
            imaget[1]=g[i][1]
    for i in range(len(g)):
        if g[i][0]==t[2]:
            imaget[2]=g[i][1]
    return(imaget)
    
for i in range(len(T)):
    if Xhi(G[0],T[i])!=T[i]:
        print("OULULULULULULU (i)",Xhi(G[0],T[i]),"   ",T[i])
        
for i in range(len(G)):
    for ii in range(len(G)):
        for iii in range(len(T)):
            if Xhi(composition(G[i],G[ii]),T[iii])!=Xhi(G[i],Xhi(G[ii],T[iii])):
                print("OULULULULULULU (ii)",Xhi(composition(G[i],G[ii]),T[iii]),"   ",Xhi(G[i],Xhi(G[ii],T[iii])))
# Le programme n'affiche aucun 'OULULULULULULU', notre fonction Xhi définit bien une action de groupe !!!!
orbitesMultiples=[]
for i in range(len(T)):
    orbitesMultiples.append([])
for i in range(len(T)):
    for ii in range(len(T)):
        for iii in range(len(G)):
            if Xhi(G[iii],T[ii])==T[i]:
                if not T[ii] in orbitesMultiples[i]:
                    orbitesMultiples[i].append(T[ii])

orbitesT=[]
for i in range(len(orbitesMultiples)):
    if not orbitesMultiples[i] in orbitesT:
        orbitesT.append(orbitesMultiples[i])
print("il y a ",len(orbitesT)," orbites des triplets")



def Psi(g, d):# On définit la fonction qui fait agir G sur P
    imaged=[[],[]]
    for i in range(len(g)):
        if g[i][0]==d[0]:
            imaged[0]=g[i][1]
    for i in range(len(g)):
        if g[i][0]==d[1]:
            imaged[1]=g[i][1]
    return(imaged)
    
for i in range(len(P)):
    if Psi(G[0],P[i])!=P[i]:
        print("OULOLOLOLOLOLO (i)",Psi(G[0],P[i]),"   ",P[i])
        
for i in range(len(G)):
    for ii in range(len(G)):
        for iii in range(len(P)):
            if Psi(composition(G[i],G[ii]),P[iii])!=Psi(G[i],Psi(G[ii],P[iii])):
                print("OULOLOLOLOLOLO (ii)",Psi(composition(G[i],G[ii]),P[iii]),"   ",Psi(G[i],Psi(G[ii],P[iii])))
# Le programme n'affiche aucun 'OULOLOLOLOLOLO', notre fonction Psi définit bien une action de groupe !!!!
orbitesMultiples=[]
for i in range(len(P)):
    orbitesMultiples.append([])
for i in range(len(P)):
    for ii in range(len(P)):
        for iii in range(len(G)):
            if Psi(G[iii],P[ii])==P[i]:
                if not P[ii] in orbitesMultiples[i]:
                    orbitesMultiples[i].append(P[ii])

orbitesP=[]
for i in range(len(orbitesMultiples)):
    if not orbitesMultiples[i] in orbitesP:
        orbitesP.append(orbitesMultiples[i])
print("il y a ",len(orbitesP)," orbites des doublets")
