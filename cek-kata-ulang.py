
def cekkataulang(kata):
    lkata=len(kata)
    print("lkata=",lkata)
    if lkata%2==0:
        sl=int(lkata/2)
        tengah=kata[:sl]
        kata=tengah+"-"+tengah
    else:
        kata=kata

    return(kata)


kata="orangorang"
hasil=cekkataulang(kata)
print(hasil)

kata="bendabenda"
hasil=cekkataulang(kata)
print(hasil)
