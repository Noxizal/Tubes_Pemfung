import pandas as pd
import numpy as np
import itertools
import operator
from traceback import print_tb

#load Data
dataku = pd.read_csv('data-rekap-kasus-covid19-per-kelurahan-di-provinsi-dki-jakarta-tanggal-1-mei-2020-pukul-0900.csv', index_col='id_kel')

#Sorting Data
dataku1 = pd.read_csv('data-rekap-kasus-covid19-per-kelurahan-di-provinsi-dki-jakarta-tanggal-1-mei-2020-pukul-0900.csv', index_col='id_kel').loc[:,'nama_kelurahan': 'meninggal':]


#Sorting Berdasarkan Meninggal Tertinggi
sorting_meninggal = dataku1.sort_values(by='meninggal', ascending=False)

#Sorting Berdasarkan Sembuh Tertinggi
sorting_sembuh = dataku1.sort_values(by="sembuh", ascending=False)

#Filter Data
dataku2 = pd.read_csv('data-rekap-kasus-covid19-per-kelurahan-di-provinsi-dki-jakarta-tanggal-1-mei-2020-pukul-0900.csv', index_col='id_kel').loc[:,'nama_kelurahan': 'meninggal':]

#Filter Banyaknya ODP
def filterODP():
    banyakodp = int(input('Filter Berdasarkan Banyaknya ODP : '))
    filter_data = (dataku2['odp'] >= banyakodp)
    filter_data1 = dataku2[filter_data]
    print(filter_data1.head(10))

#Filter Banyaknya Masih di rawat
def filterDirawat():
    banyakdirawat = int(input('Filter Berdasarkan Banyaknya Orang Yang Dirawat : '))
    filter_data = (dataku2['masih_dirawat'] >= banyakdirawat)
    filter_data1 = dataku2[filter_data]
    print(filter_data1.head(10))

#MAP
mapbysembuh = pd.read_csv('data-rekap-kasus-covid19-per-kelurahan-di-provinsi-dki-jakarta-tanggal-1-mei-2020-pukul-0900.csv', index_col='nama_kelurahan').loc[:,'sembuh':]
mapbymeninggal = pd.read_csv('data-rekap-kasus-covid19-per-kelurahan-di-provinsi-dki-jakarta-tanggal-1-mei-2020-pukul-0900.csv', index_col='nama_kelurahan').loc[:,'meninggal':]

#Map Sembuh
def mymap(x):
    if x > 20:
        return ("Tinggi")
    elif x > 10:
        return ("Sedang")
    return ("Sedikit")
kategori = mapbysembuh['sembuh'].map(mymap)

#Map Meninggal
def mymap1(x):
    if x > 20:
        return ("Tinggi")
    elif x > 10:
        return ("Sedang")
    return ("Sedikit")
kategori1 = mapbymeninggal['meninggal'].map(mymap)

#Count
def jumlahsembuh():
    jumlah_sembuh = dataku.groupby(['nama_kelurahan'])['sembuh'].sum()
    print("Jumlah data Berdasarkan Kelurahan : ")
    print(jumlah_sembuh)
    print("Jumlah ", jumlah_sembuh.sum())

#Compress Data
def compressdata():
    inputdata = input("Masukkan data yang ingin di kompresi melalui Kecamatan : ")
    hasil = dataku.nama_kecamatan == inputdata
    data1 = dataku['nama_kecamatan']
    selector = hasil
    hasil1 = itertools.compress(data1, selector)
    tolist = list(hasil1)
    print(tolist)
    print("Jumlah Kecamatan "+inputdata+ "ada : ", tolist.count(inputdata))

def menu_HighOrderFunction():
        print("\n")
        print(" ________________________________________________________________")
        print("|                   High Order Function                          |")
        print("|----------------------------------------------------------------|")
        print("|1. Map                                                          |")
        print("|2. Filter                                                       |")
        print("|3. Sorted                                                       |")
        print("|________________________________________________________________|")
        highorderfunction = int(input("Masukkan Pilihan : "))

        if highorderfunction == 1:
            print(menuMap())
            back_menu_highorderfunction = int(input("press 99 back menu\n"))
            if back_menu_highorderfunction == 99:
                print(menu_HighOrderFunction)
            else:
                print("Input tidak tersedia")
        elif highorderfunction==2:
            print(menuFilter())
            back_menu_highorderfunction1 = int(input("press 99 back menu \n"))
            if back_menu_highorderfunction1 == 99:
                print(menu_HighOrderFunction)
            else:
                print("Input tidak tersedia")
        elif highorderfunction==3:
            print
            print(menuSorted())
            back_menu_highorderfunction2 = int(input("press 99 back menu \n"))
            if back_menu_highorderfunction2 == 99:
                print(menu_HighOrderFunction)
            else:
                print("Input tidak tersedia")
        elif highorderfunction==4:
            print()
        else:
            print("Input tidak sesuai")

def menu_theitertools():
        print("\n")
        print(" ________________________________________________________________")
        print("|                   THE ITERTOOLS MODULE                         |")
        print("|----------------------------------------------------------------|")
        print("|1. Count                                                        |")
        print("|2. Compress                                                     |")
        print("|________________________________________________________________|")
        theitertools = int(input("Masukkan Pilihan : "))
        if theitertools == 1:
            print(menuCount())
            back_menu_theitertools = int(input("press 99 back menu\n"))
            if back_menu_theitertools == 99:
                print(menu_theitertools)
            else:
                print("Input tidak tersedia")
        if theitertools == 2:
            print(menuCompress())
            back_menu_theitertools1 = int(input("press 99 back menu\n"))
            if back_menu_theitertools1 == 99:
                print(menu_theitertools)
            else:
                print("Input tidak tersedia")
        if theitertools == 3:
            print()
            back_menu_theitertools2 = int(input("press 99 back menu\n"))
            if back_menu_theitertools2 == 99:
                print(menu_theitertools)
            else:
                print("Input tidak tersedia")
        elif theitertools==4:
            print()
        else:
            print("Input tidak sesuai")

def menuMap():
    print("\n")
    print(" ________________________________________________________________")
    print("|                            MAP                                 |")
    print("|----------------------------------------------------------------|")
    print("|1. Map By Sembuh                                                |")
    print("|2. Map By Meninggal                                             |")
    print("|3. back                                                         |")
    print("|________________________________________________________________|")
    menu_map = int(input("Masukkan Pilihan  : "))
    if menu_map == 1:
        print(kategori.head(10))
        back_menu_map1=int(input("Press 99 back menu\n"))
        if back_menu_map1 == 99:
            print(menuMap())
        else:
            print("Input tidak sesuai")
    elif menu_map == 2:
        print(kategori1.head(10))
        back_menu_map2=int(input("Press 99 back menu\n"))
        if back_menu_map2 == 99:
            print(menuMap())
        else:
            print("Input tidak sesuai")
    elif menu_map == 3:
        print(menu_HighOrderFunction())
    else:
        print("Input tidak sesuai")

def menuFilter():
    print("\n")
    print(" ________________________________________________________________")
    print("|                            FILTER                              |")
    print("|----------------------------------------------------------------|")
    print("|1. Orang dengan status ODP                                      |")
    print("|2. Orang dengan status Dirawat                                  |")
    print("|3. back                                                         |")
    print("|________________________________________________________________|")
    menu_filter = int(input("Masukkan Pilihan  : "))
    if menu_filter == 1:
        print(filterODP())
        back_menu_filter1=int(input("Press 99 back menu\n"))
        if back_menu_filter1 == 99:
            print(menuFilter())
        else:
            print("Input tidak sesuai")
    elif menu_filter == 2:
        print(filterDirawat())
        back_menu_filter2=int(input("Press 99 back menu\n"))
        if back_menu_filter2 == 99:
            print(menuFilter())
        else:
            print("Input tidak sesuai")
    elif menu_filter == 3:
        print(menu_HighOrderFunction())
    else:
        print("Input tidak sesuai")

def menuSorted():
    print("\n")
    print(" ________________________________________________________________")
    print("|                            SORTED                              |")
    print("|----------------------------------------------------------------|")
    print("|1. Sorting banyaknya sembuh                                     |")
    print("|2. Sorting banyaknya meninggal                                  |")
    print("|3. back                                                         |")
    print("|________________________________________________________________|")
    menu_sorted = int(input("Masukkan Pilihan  : "))
    if menu_sorted == 1:
        print(sorting_sembuh.head(10))
        back_menu_sorted1=int(input("Press 99 back menu\n"))
        if back_menu_sorted1 == 99:
            print(menuSorted())
        else:
            print("Input tidak sesuai")
    elif menu_sorted == 2:
        print(sorting_meninggal.head(10))
        back_menu_sorted2=int(input("Press 99 back menu\n"))
        if back_menu_sorted2 == 99:
            print(menuSorted())
        else:
            print("Input tidak sesuai")
    elif menu_sorted == 3:
        print(menu_HighOrderFunction())
    else:
        print("Input tidak sesuai")

def menuCount():
    print("\n")
    print(" ________________________________________________________________")
    print("|                            COUNT                               |")
    print("|----------------------------------------------------------------|")
    print("|1. Count jumlah sembuh                                          |")
    print("|2. back                                                         |")
    print("|________________________________________________________________|")
    menu_count = int(input("Masukkan Pilihan : "))
    if menu_count == 1:
        print(jumlahsembuh())
        back_menu_count1=int(input("Press 99 back menu\n"))
        if back_menu_count1 == 99:
            print(menuCount())
        else:
            print("Input tidak sesuai")
    elif menu_count == 2:
        print(menu_theitertools())
    else:
        print("Input tidak sesuai")
def menuCompress():
    print("\n")
    print(" ________________________________________________________________")
    print("|                           COMPRESS                             |")
    print("|----------------------------------------------------------------|")
    print("|1. Compress Nama Kelurahan                                      |")
    print("|2. back                                                         |")
    print("|________________________________________________________________|")
    menu_compress = int(input("Masukkan Pilihan : "))
    if menu_compress == 1:
        print(compressdata())
        back_menu_compress1=int(input("Press 99 back menu\n"))
        if back_menu_compress1 == 99:
            print(menuCompress())
        else:
            print("Input tidak sesuai")
    elif menu_compress == 2:
        print(menu_theitertools())
    else:
        print("Input tidak sesuai")

def mainMenu():
    print("\n")
    print(" ________________________________________________________________")
    print("|                            MENU                                |")
    print("|----------------------------------------------------------------|")
    print("|1. Tampil Data                                                  |")
    print("|2. High Order Function                                          |")
    print("|3. The Itertools Module                                         |")
    print("|99. EXIT                                                        |")
    print("|________________________________________________________________|")
    main_menu = int(input("Masukkan Pilihan : "))
    if main_menu == 1:
        print(dataku.head(10))
        back_main_menu = int(input("Press 99 back menu\n"))
        if back_main_menu == 99:
            print(mainMenu())
        else:
            print("Input tidak sesuai")
    elif main_menu == 2:
        print(menu_HighOrderFunction())
        back_main_menu1 = int(input("Press 99 back menu\n"))
        if back_main_menu1 == 99:
            print(mainMenu())
        else:
            print("Input tidak sesuai")
    elif main_menu == 3:
        print(menu_theitertools())
        back_main_menu2 = int(input("Press 99 back menu\n"))
        if back_main_menu2 == 99:
            print(mainMenu())
        else:
            print("Input tidak sesuai")
    elif main_menu == 4:
        exit()
    else:
        print("Input tidak sesuai")

#MAIN MENU
print(" ________________________________________________________________")
print("|                 Program DataBase Python                        |")
print("|           Matakuliah Pemrograman Fungsional                    |")
print("|      Dosen Pengampu : Agus Priyanto, S.Kom., M.Kom.            |")
print("|----------------------------------------------------------------|")
print("| Anggota                                                        |")
print("| 1. Rizal Wahyudianto   - 19102142                              |")
print("|________________________________________________________________|")
print(mainMenu())










