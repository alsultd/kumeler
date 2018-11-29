import itertools
x1=input("Küs arkadaşların isimini giriniz(1 ie 2 küs)(1. küs isim):\t")
x2=input("Küs arkadaşların isimini giriniz(1 ile 2 küs)(2. küs isim):\t")
x3=input("Küs arkadaşların isimini giriniz(3 il 4 küs)(3. küs isim):\t")
x4=input("Küs arkadaşların isimini giriniz(3 ile 4 küs)(4. küs isim):\t")
x5=input("Küs arkadaşların isimini giriniz(5 ile 6 küs)(5. küs isim):\t")
x6=input("Küs arkadaşların isimini giriniz(5 ile 6 küs)(6. küs isim):\t")
arkadaslar=["erol","ercan","ali","sami","mehmet","talat","tamer","kemal","barlas","başar","galip","haldun","erdoğan","atilla","yavuz"]
masalar=list(itertools.combinations(arkadaslar,5))       
def kesisimleri_bos(kumeA,kumeB):
    return(set(kumeA)&set(kumeB))==set()   
for i,j,k in itertools.combinations(masalar,3):
    if(kesisimleri_bos(i,j)&kesisimleri_bos(i,k)&kesisimleri_bos(j,k)):
        #print("bu kümelerin kesişimleri boş"+str(i)+str(j)+str(k))
        i=list(i)
        j=list(j)
        k=list(k)
        if x1 in i and x2 in i:
            del i[:]
        if x3 in i and x4 in i:
            del i[:]
        if x5 in i and x6 in i:
            del i[:]
        if x1 in j and x2 in j:
            del j[:]
        if x3 in j and x4 in j:
            del j[:]
        if x5 in j and x6 in j:
            del j[:]
        if x1 in k and x2 in k:
            del k[:]
        if x3 in k and x5 in k:
            del k[:]
        if x5 in k and x6 in k:
            del k[:]
        print(len(str(i)+str(j)+str(k)))
        print(str(i)+str(j)+str(k))
