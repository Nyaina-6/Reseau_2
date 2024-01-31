
import matplotlib.pyplot as plt
import random

Cx = 0
Cy = 0

def getTab(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(0, 1))
    return tab

#Fonction qui trace les cercles
#IN : Tableau d'entier
#OUT : Protocole compose de cercles
def printTab(tab):
    t = ''
    ct = 0
    for i in tab:
        t = t + ' '+str(i)
        if ct == 4:
            t = t + '\n'
    print(t)

#Fonction qui affiche un tableau
#IN : Tableau d'entier
#OUT : tous les entier de ce tableau
def trace(tab,P):
    global Cx
    global Cy
    pixel = 0.1
    v = 1
    un = 0 # pour calculer l'efficacitee graphique
    figure, axes = plt.subplots()
    draw_circle = plt.Circle((Cx, Cy), pixel,fill=False,  color='green') #  le cercle de depart
    axes.add_artist(draw_circle)
    draw_circle = plt.Circle((Cx, Cy), pixel+v*0.1,fill=False, color='red') # les cercles qui montrent le decalage
    axes.add_artist(draw_circle)
    v = 2

    for i in tab:
        if(i > 0):
            un +=1
            draw_circle = plt.Circle((Cx, Cy), pixel+v*0.1,fill=False)
            axes.add_artist(draw_circle)
        v = v + 1


    plt.xlim(-0.5-0.1*v,  0.5+v*0.1)
    plt.ylim(-0.5-0.1*v,  0.5+v*0.1)
    axes.set_aspect(1)
    axes.add_artist(draw_circle)
    a = (un/(v + 0.5)) *100
    plt.title('program effectiveness : '+str(   P    )+' %'  )
    plt.show()
    return () 

#Fonction pour la conversion d'une chaine de caractere en son nombre ascii
#IN : caractere
#OUT : entier
def charToAscii(char):
    return ord(char)

#Fonction pour la conversion un entier en un tableau contenant les bits de cet entier
#IN : entier
#OUT : tableau d'entiers correspodant aux bits
def intToBit(n,b=2,verbose=False):
    """retourne sous forme du tableau l'écriture en base b de  l'entier n écrit en base 10"""
    t = []
    if n==0:
        return [0]
    while n>0:
        quotient, reste = n//b,n%b
        if verbose:
            print("%s=%s*%s+%s"%(n,quotient,b,reste))
        t.append(reste)
        n = quotient
    #on renverse le tableau des restes successifs
    t.reverse()
    return t


        
#Fonction pour la conversion une chaine en un tableau contenant les bits de cette chaine
#IN : str
#OUT : tableau d'entier correspodant aux bits
def strToBit(string):
    tableau = []
    for char in string:
        tableau.extend( intToBit( charToAscii(char) ) )
    
    return tableau


#Fonction qui genere le code de hamming
#IN : tab
#OUT : str
def hamming(tab):
    q = listToString(tab)
    data=list(q)
    data.reverse()
    z,ch,l,r,u=0,0,0,0,[]

    while ((len(q)+r+1)>(pow(2,r))):
        r=r+1

    for i in range(0,(r+len(data))):
        p=(2**z)

        if(p==(i+1)):
            u.append(0)
            z=z+1

        else:
            u.append(int(data[l]))
            l=l+1

    for parity in range(0,(len(u))):
        ph=(2**ch)
        if(ph==(parity+1)):
            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(u)):
                block=u[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                u[startIndex]=u[startIndex]^toXor[z]
            ch+=1

    u.reverse()
    print('Hamming code generated would be:- ', end="")
    print(stringToList(u))
    return u


#Fonction qui transforme une liste en string
#IN : tableau
#OUT : string
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += str(ele)  
    
    # return string  
    return str1 

#Fonction qui transforme une str en liste
#IN : str
#OUT : tab
def stringToList(list1):
    str1 = ''.join(str(e) for e in list1)
    return str1
                

    
info = input("please enter the information to code: ")
tab = strToBit(info)

H = hamming(tab)
print("Code Hamming : ",H)

efficiency = ( len(tab)/len(H) ) * 100
effigraphic= trace(H,efficiency)


print('protocol efficiency : ',efficiency,'%')
