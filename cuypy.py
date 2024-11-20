import random
import main 

def start(): 
    
    nama_user = input("Masukan nama Kamu : ")
    if nama_user == "":
        input("Masukan nama Kamu : ")
    
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4 #INI TETEP HARUS KOSONG

        cuypy_position = random.randint(1, 4)

        goa = goa_kosong.copy() #INI TEMPAT BARU BUAT CUYPY 
        goa[cuypy_position - 1] = "|0_0|"

        goa_kosong = " ".join(goa_kosong)
        goa = " ".join(goa)
            
        print(f'''
        Hallo {nama_user} Coba perhatikan goa dibawah ini
        {goa_kosong}
        ''')

        pilihan_user = int(input('Menurut kamu di goa nomor berapa CUYPY berada [1 / 2 / 3 / 4 ]: '))

        while pilihan_user >= 5:
            pilihan_user = int(input('Masukan angka yang benar!! [1 / 2 / 3 / 4] : '))

        if int(pilihan_user) == cuypy_position:
            print(f'\n\t{goa}\n\tSELAMAT KAMU MENANG! CUYPY memujimu dia berkata : JAGOO!!')
        else:
            print(f'\n\t{goa}\n\tKAMU KALAH! CUYPY mengejekmu dia berkata : CUPUU!!')
                
        play_again = input('\n\nApakah kamu ingin melanjutkan gamenya lagi? [y/n]')
            
        if play_again == 'n':
            print(f'''
        Terima kasih sudah bermain game ini! {nama_user} 
                
        Sampai jumpa lagi!!
                
            ''')
            
            main.menu()
        
if __name__ == '__main__':
    start()

        