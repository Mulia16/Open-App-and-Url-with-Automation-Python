import sys
import os
import shelve
from time import sleep as wait
try :
    echo = "@echo off\n"
    chrome = 'start C:/"Program Files (x86)"/Google/Chrome/Application/chrome.exe '
    ex = "\nexit"
    link = ""
    if sys.argv[1] == "set" and type(sys.argv[2]) == type("") :
        print("Membaca daftar link")
        wait(1)
        daftarLink = shelve.open("DaftarLink/link", writeback = True)
        if sys.argv[2] in daftarLink["Link"] :
            print("Link ini sudah terdaftar")
        else :
            daftarLink["Link"].append(sys.argv[2])
            for i in daftarLink["Link"] :
                link += i + " "
            print("Memasukkan link ke dalam daftar")
            wait(1)
            browser = open("WindowsBatch/browser.bat", "w")
            browser.write(echo + chrome + link + ex)
            browser.close()
            print("Berhasil memasukkan link ke daftar")
        daftarLink.close()
    elif sys.argv[1] == "del" :
        print("Membaca daftar link")
        wait(1)
        daftarLink = shelve.open("DaftarLink/link", writeback = True)
        num = 1
        for i in daftarLink["Link"] :
            print(str(num) + ". " + i)
            num += 1
        hapus = int(input("Pilih nomer berapa yang akan di hapus :\n> "))
        wait(1)
        del daftarLink["Link"][hapus]
        for i in daftarLink["Link"] :
            link += i
        browser = open("WindowsBatch/browser.bat", "w")
        browser.write(echo + chrome + link + ex)
        browser.close()
        daftarLink.close()
        print("Berhasil menghapus link dari daftar")
except IndexError as e :
    user = input("Pilih Task : \n1. coding \n2. desain \n3. microsoft_office \n> ")
    os.system(r'start WindowsBatch\browser.bat')
    if user == "1" or user == "coding" :
        os.system(r'start WindowsBatch\coding.bat')
    elif user == "2" or user == "desain" :
        os.system(r"start WindowsBatch\desain.bat")
    else :
        os.system(r"start WindowsBatch\microsoft_office.bat")
    wait(5)
    print("========== SUKSES ==========")
