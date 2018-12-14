import random
import itertools
def comb():        
    liste=list()    #boş bir liste oluşturdum
    for i in range(20,42):   #20 ile 42 arasında bir öge oluşturdum 
        #i=int(i)
        liste.append(i)  #bu ögeleri bir liste yaptım        
    if(len(liste))==22:    
        #print("liste\t:",liste)
        alt_liste=list(itertools.combinations(liste,4)) #1646 adet kombinasyon var
    #print(alt_liste)
    w=random.choice(alt_liste) # bir tanesini aldık
    print(w)        
    soru=random.choice(w)   
    print(soru)
    return soru;    
#Buraya kadar bir fonksiyon oluşturdum.
comb()
sayaç=1
sual=input("{}- Plakası {} olan ilimiz hangisidir?".format(sayaç,soru))
    
    





  
