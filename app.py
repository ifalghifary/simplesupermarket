# import jsons
from tabulate import tabulate

global menu_item
menu_item=["Lihat Barang Promo","Lihat Semua Barang","Kembali Ke Menu Utama","Exit Program"]
global all_items
global promo_items
all_items= [
   {
      "item":"susu",
      "harga":50000
   },
   {
      "item":"daging",
      "harga":20000
   },
   {
      "item":"lampu",
      "harga":15000
   },
   {
      "item":"masker",
      "harga":25000
   },
   {
      "item":"apel",
      "harga":30000
   }
]
promo_items = [
   {
      "item":"susu",
      "harga":50000
   },
   {
      "item":"masker",
      "harga":25000
   }
]

global itemkeranjang
itemkeranjang=[]
def rupiah_format(uang):
    y = str(uang)
    if(len(y)<=3):
        return 'Rp ' + y     
    else:
        p = y[-3:]
        q = y[:-3]
        return   rupiah_format(q) + '.' + p
        print('Rp ' +  rupiah_format(q) + '.' + p)
def promoitemlist():
    table=[['No.', 'Item Name', 'Harga']]
    for x,y in enumerate(promo_items):
        data=[x+1,y['item'],y['harga']]
        table.append(data)
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
def allitemlist():
    table=[['No.', 'Item Name', 'Harga']]
    for x,y in enumerate(all_items):
        data=[x+1,y['item'],y['harga']]
        table.append(data)
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
def allorpromo():
    menuitem=["Lihat Barang Promo","Lihat Semua Barang"]
    print("*Tekan '0' Jika Ingin ke Menu Utama \n*Tekan '99' Jika Ingin ke Melihat Keranjang Belanja")
    print("\n")
    menu_itemlist=input("Pilih Menu: ")
    for x,y in enumerate(menu_item):
        print(x+1,y)
    if(x<(len(menuitem)-1)):
        print("\n")
    getinput=input("Pilih Menu: ")
    
    
    if(getinput=="0"):
        main_function()
    elif(getinput=="99"):
        keranjangbelanja()
    elif(getinput=="1"):
        allitemlist()
    elif(getinput=="2"):
        allitemlist()
    else:
        errormenu()
        
        


def keranjangbelanja():
    global itemkeranjang
    x = len(itemkeranjang)
    if(x==0):
        print("\n\n")
        print("Keranjang Kosong!")
        print("\n\n")
        main_menu()
    else:
        totalharga=0
#         print(itemkeranjang)
        for x,y in enumerate(itemkeranjang):
            totalharga=totalharga+((itemkeranjang[x]["harga"])*int(itemkeranjang[x]["jumlah"]))
        print("===================================================")
        print("Total Harga:",rupiah_format(totalharga))
        print("\n")
        print("Detil Item: \n")
        for x,y in enumerate(itemkeranjang):
            print(itemkeranjang[x]["jumlah"],itemkeranjang[x]["nama"],"->",rupiah_format((itemkeranjang[x]["harga"]*itemkeranjang[x]["jumlah"])))
        print("===================================================")
        print("===================================================")
        print("*Ketik 0 untuk melanjutkan belanja")
        getinput=input("Ketik '99' untuk kembali ke menu utama (Data Keranjang Akan Terhapus): ")
        
        if(getinput=='99'):
            itemkeranjang=[]
            main_function()
        elif(getinput=="0"):
            main_function()
        else:
            itemkeranjang=[]
            main_function()

def executemenu(menu):
    try:
        if(menu=="0"):
            main_function()
        elif(menu=="3"):
            main_function()
        elif(menu=="99"):
            keranjangbelanja()
        elif(menu=="4"):
            print("===============================================================")
            print("Terimakasih telah menggunakan Program Supermarket Tito :)")
            print("===============================================================")
            return

        elif(menu=="1"):
            global promo_items
            promoitemlist()
            print("*Tekan '0' Jika Ingin ke Menu Utama \n*Tekan '99' Jika Ingin ke Melihat Keranjang Belanja")
            print("Untuk Memilih Barang, Masukkan nomor dan jumlah barang dengan pemisah ';', Misal memilih Barang Nomor 1 dengan Jumlah 4 Buah maka input dengan format '1;4' \n")
            menu_itemlist=input("Pilih Barang: ")
            
            praparsing=menu_itemlist.split(';')
            praparsing=int(praparsing[0])
            if(menu_itemlist=="0"):
                main_function()
            elif(menu_itemlist=="99"):
                keranjangbelanja()  
            elif(praparsing>len(promo_items)):
                return errormenu()
            elif(praparsing<=len(promo_items)):
                try:
                    parsing2=menu_itemlist.split(';')
                    parsing2=int(parsing2[1])
                    if(parsing2<1):
                        return errormenu()
                    else:
                        pilihandata=praparsing-1
                        jumlahdata=parsing2
                        if(pilihandata<=len(promo_items)):
                            try:
                                masukkeranjang(promo_items,int(pilihandata),int(jumlahdata),menu)
                                return executemenu(2)
                            except:
                                return errormenu()
                except:
                    return errormenu()
            else:
                return errormenu()

            

            
        elif(menu=="2"):
            global all_items
            allitemlist()
            print("*Tekan '0' Jika Ingin ke Menu Utama \n*Tekan '99' Jika Ingin ke Melihat Keranjang Belanja")
            print("Untuk Memilih Barang, Masukkan nomor dan jumlah barang dengan pemisah ';', Misal memilih Barang Nomor 1 dengan Jumlah 4 Buah maka input dengan format '1;4' \n")
            menu_itemlist=input("Pilih Barang: ")
            
            praparsing=menu_itemlist.split(';')
            praparsing=int(praparsing[0])
            if(menu_itemlist=="0"):
                main_function()
            elif(menu_itemlist=="99"):
                keranjangbelanja()  
            elif(praparsing>len(all_items)):
                return errormenu()
            elif(praparsing<=len(all_items)):
                try:
                    parsing2=menu_itemlist.split(';')
                    parsing2=int(parsing2[1])
                    if(parsing2<1):
                        return errormenu()
                    else:
                        pilihandata=praparsing-1
                        jumlahdata=parsing2
                        if(pilihandata<=len(all_items)):
                            try:
                                masukkeranjang(all_items,int(pilihandata),int(jumlahdata),menu)
                                return executemenu(2)
                            except:
                                return errormenu()
                except:
                    return errormenu()
            else:
                return errormenu()
        else:
            return errormenu()
    except:
        return errormenu()
def errormenu():
    print("Pilihan Menu Tidak Tersedia. \n")
    print("==================================================================")
    print("Silahkan Pilih Menu Berikut (Pilih dengan mengetik angka):\n ")
    print("*Tekan '0' Jika Ingin ke Menu Utama \n*Tekan '99' Jika Ingin ke Melihat Keranjang Belanja")
    for x,y in enumerate(menu_item):
        print(x+1,y)
        if(x==3):
            print("\n")
    getinput=input("Pilih Menu: ")
    executemenu(getinput)

def main_menu():
    print("Silahkan Pilih Menu Berikut (Pilih dengan mengetik angka):\n ")
    for x,y in enumerate(menu_item):
        print(x+1,y)
        if(x==3):
            print("\n")
    print("*Tekan '0' Jika Ingin ke Menu Utama \n*Tekan '99' Jika Ingin ke Melihat Keranjang Belanja")
    getinput=input("Pilih Menu: ")
    executemenu(getinput)
    
def masukkeranjang(jenisitem,data,jumlah,menu):
    global itemkeranjang

    itemkeranjangtemp=itemkeranjang
    try:
        filterdata = [x for x in itemkeranjangtemp if x['nama'] == jenisitem[data]["item"]]
        filterdata=len(filterdata)
        if(filterdata>0):
            datasisa = [x for x in itemkeranjangtemp if x['nama'] != jenisitem[data]["item"]]
            dataupdate=[x for x in itemkeranjangtemp if x['nama'] == jenisitem[data]["item"]]
            dataupdate[0]["jumlah"]=int(dataupdate[0]["jumlah"])+jumlah
            itemkeranjangtemp=[]
            if(len(datasisa)>0):
                itemkeranjangtemp.append(datasisa[0])
            itemkeranjangtemp.append(dataupdate[0])
            itemkeranjang=itemkeranjangtemp
            print("Data ",dataupdate[0]["nama"]," berhasil Ditambahkan ke Keranjang!")
            print("\n")
            return executemenu(menu)
        elif(filterdata==0):
            itemkeranjangtemp=[]
            pradata={
            "nama":jenisitem[int(data)]["item"],
            "harga":jenisitem[int(data)]["harga"],
            "jumlah":jumlah
            }
            itemkeranjang.append(pradata)
            print("Data",pradata["nama"]," berhasil Ditambahkan ke Keranjang!")
            print("\n")
            return executemenu(menu)
    except:
        try:
            executemenu(menu)
        except:
            errormenu()

        

    
    
    
def main_function():
    print("=============================================")
    print("--Selamat Datang di Program Supermarket Tito--")
    print("=============================================")
    print("Berikut Adalah Barang yang sedang Promo:")
    promoitemlist()
    print("=============================================")
    print("Silahkan Pilih Menu Berikut (Pilih dengan mengetik angka):\n ")
    for x,y in enumerate(menu_item):
        print(x+1,y)
        if(x==3):
            print("\n")
    print("*Tekan '99' Jika Ingin ke Melihat Keranjang Belanja")
    getinput=input("Pilih Menu: ")
    
    executemenu(getinput)
    


main_function()



  