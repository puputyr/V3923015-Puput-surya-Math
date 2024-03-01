import math as D2
import math as D3

while True:
    print("\n======== Menu ========")
    print("Pilih bangun 2D, 3D, atau other:")
    pilihan = input("2D, 3D, atau other? ")

    if pilihan == "2D":
        print("Pilih bangun 2D:")
        print("1. Persegi")
        print("2. Persegi panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Jajar genjang")
        print("6. Trapesium")
        print("7. Keluar")
        bangun = input("Pilih bangun: ")

        if bangun == "1":
            sisi = float(input("Masukkan panjang sisi: "))
            print("Luas persegi adalah:", D2.persegi(sisi))
        elif bangun == "2":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            print("Luas persegi panjang adalah:", D2.persegi_panjang(panjang, lebar))
        elif bangun == "3":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            print("Luas segitiga adalah:", D2.segitiga(alas, tinggi))
        elif bangun == "4":
            jari_jari = float(input("Masukkan jari-jari: "))
            print("Luas lingkaran adalah:", D2.lingkaran(jari_jari))
        elif bangun == "5":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            print("Luas jajar genjang adalah:", D2.jajar_genjang(alas, tinggi))
        elif bangun == "6":
            sisi_a = float(input("Masukkan sisi a: "))
            sisi_b = float(input("Masukkan sisi b: "))
            tinggi = float(input("Masukkan tinggi: "))
            print("Luas Trapesium adalah:", D2.trapesium(sisi_a, sisi_b, tinggi))
        elif bangun == "7":
            kembali = input("Anda yakin ingin end dari program ini? (yes/no) ")
            if kembali == "yes":
                break
            elif kembali == "no":
                continue


    elif pilihan == "3D":
        # tambahkan kode untuk menghitung bangun 3D di sini
        print("Pilih bangun 3D:")
        print("1. Kubus")
        print("2. Balok")
        print("3. Tabung")
        print("4. Kerucut")
        print("5. Limas")
        print("6. Prisma")
        print("7. Keluar")
        bangun1 = input("Pilih bangun: ")
        
        if bangun1 == "1":
            sisi = float(input("Masukkan panjang sisi: "))
            print("Volume kubus adalah:", D3.kubus(sisi))
        elif bangun1 == "2":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            tinggi = float(input("Masukkan tinggi: "))
            print("Volume balok adalah:", D3.balok(panjang, lebar, tinggi))
        elif bangun1 == "3":
            jari_jari = float(input("Masukkan jari-jari: "))
            tinggi = float(input("Masukkan tinggi:  "))
            print("Volume tabung adalah:", D3.tabung(jari_jari, tinggi))
        elif bangun1 == "4":
            jari_jari = float(input("Masukkan jari-jari: "))
            tinggi = float(input("Masukkan tinggi: "))
            print("Volume kerucut adalah:", D3.kerucut(jari_jari, tinggi))
        elif bangun1 == "5":
            alas = float(input("Masukkan alas: "))
            tinggi = float(input("Masukkan tinggi: "))
            print("Volume limas adalah:", D3.limas(alas, tinggi))
        elif bangun1 == "6":
            alas = float(input("Masukkan alas: "))
            tinggi_prisma = float(input("Masukkan tinggi: "))
            print("Volume prisma adalah:", D3.prisma(alas, tinggi_prisma))
        elif bangun1 == "7":
            kembali = input("Anda yakin ingin keluar end program ini? (yes/no) ")
            if kembali == "yes":
                break
            elif kembali == "no":
                continue
        
        else:
            print("Pilihan tidak valid. Silahkan pilih lagi")
            
    elif pilihan == "other":
        break
    else:
        print("Pilihan tidak valid. Silahkan pilih lagi")
print("Terima kasih telah menggunakan program ini.")