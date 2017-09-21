## Nama Program : baca_buku1d.py
##buku=open("THE PHILOSOPHY OF PUNISHMENTS.txt")  #bab5  tes1 THE PHILOSOPHY OF PUNISHMENTS
##buku=open("bab5.txt")
print("Nama Program : baca_bukuM1.py")
buku=open("Malfuzat14.txt")  # IPAI31
baris=buku.readline()

baris=baris[:-1]
cetak=""
awal="T"
jmlbrs=0
ret=0
while baris:
    jmlbrs +=1
    lb=len(baris)
    
    # ciri ciri judul dan sub judul :
    # huruf kapital semua, atau
    # awal huruf kapital,
    # tidak ada titik,
    # pj < 51 char
    
    if lb<=35 and baris.rfind(".")==-1 and (baris[:2].istitle() or baris.isupper()): # mencari judul
##        if ret==1:
        cetak=cetak+baris+"\r"
        ret=1

        
    # jika ada . ? ! : ) tapi pendek maka selanjutnya paragraf baru
    elif (baris[-1:]=="." or baris[-1:]=="?" or baris[-1:]=="!" or baris[-1:]==":" or baris[-1:]==")" ) and lb<68:  #chr(182)
        cetak=cetak+" "+baris+"\r"
        ret=1
    # jika tidak ada ada . ? ! : ) tapi lebih dari 35
    else:     # jika bukan judul                   
        if lb<8 and baris.strip()!="* * *" and baris.replace("-","").strip().isdigit(): # HALAMAN
            cetak=cetak.strip()+"\r"
        elif baris.strip()=="* * *":    # pemisah baris
            cetak=cetak.lstrip()+baris+"\r"
            ret=1
        elif lb>35 :
            if ret==1:
                cetak=cetak+baris
                ret=0
            else:
                cetak=cetak+" "+baris
                ret=0
        else:
            if ret==1:
                cetak=cetak+baris
                ret=0
            else:
                cetak=cetak+" "+baris
                ret=0
        if awal=="T":
            cetak=cetak.lstrip()
            awal="F"

##    buffered_size+=len(baris+"  ")
        
    baris=buku.readline()
    # hapus spasi di awal baris
    if baris[:1]==' ':
        baris="<>"+baris[1:]
    if baris[:1]==" " or baris[:2]=="  ":
        if baris[:2]=="  ":
            baris=baris[2:]
        else:
            baris="*"+baris[1:]
    baris=baris[:-1]

    if jmlbrs==63 or baris.rstrip()=="":
        print (cetak)
        cetak=""
        jmlbrs=0
##print(buffered_size)   

buku.close()                       
##buffered_size=0
