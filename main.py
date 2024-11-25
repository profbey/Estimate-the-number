'''
1 - 100 arasinda rastgele uretebilecek bir sayiyi asagi yukari ifadeleri ile buldurmaya calisin.

** 'random' modulu icin 'python random' seklinde arama yapin.
** 100 uzerinden puanlama yapin. her soru 20 puan.
** hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi uzerinden hesaplansin.

**** zorluk seviyesi eklenmeli
**** oyundan out etmek mi yoksa tekrar oynamak isteyip istmedigi sorulmali

***** arayuz eklenmeli. arayuzde yeni oyun, devam et, skor tablosu, cikis yap ekranlari olmali. 
***** yeni oyun ekraninda isim sormali. sonraki ekranda zorluk seviyesi secilmeli
***** secilen zorluk seviyesi, hak bilgisi ve puan bilgisi ile ekranda yazmali.
***** kutucuga yanlis bir sayi girildiginde ufak bir can kayip animasyonu donmeli.(kalp ikonunu kesen bir kilic ve yanda animasyon bittiginde -x puan yazmali.)
***** secilen sayilar ekranda yazmali. dogru bilindiginde congrat yazisi ile ufak bir animasyon ve ufak bir tebrik sesi girmeli. score tablosuna kaydedilmeli.
***** 'https://freesound.org/search/?q=congrat&f=grouping_pack%3A%2232486_Orchestral+Stings+and+Stabs%22' ornek bir ses olabilir. 
***** kaybettiginde de benzer bir muhabbet ile tekrar oynamak ister misin diye sorulmali. 

****** zorluk seviyesinde kolay modda 1 ile 50 arasinda sayilari icericek ve 5 hak verilecek.
 orta modda 1 ile 75 arasindaki sayilar icin 4 hak verilecek. 
 zor modda ise 1 ile 100 arsindaki sayilar icin 4 hak verilecek sekilde zorluk seviyesi ayarlanacak. 
 puanlama kisminda ise tahminle dogru sayi arasindaki farka göre puanlama yapilacak/
***** 
'''
import random

randomNumber = random.randint(1, 10)

try:                                            # Its for input of right.
    health = int(input('How many right you want?: '))
    right = health
except ValueError:
    right = 5 
print(f"You have {right} right.")

counter = 0 
score = 100

while right > 0:
    try:
        print(randomNumber, right, counter)     # To control numbers and debug
        estimate = int(input('Your Estimate : '))
        right -= 1

        if randomNumber == estimate:
            print(f'Congratulations, You got it right the {counter + 1 }. time.\nYour score is {score} ')
            break
        elif randomNumber > estimate:
            print('up')
        else:
            print('down')

        
        if randomNumber != estimate:            # Deduct points only for incorrect guesses
            counter += 1
            score -= (100/health) * counter 

        if right == 0:
            print(f'You LOSE. The Number is {randomNumber}')
            break
    except ValueError:
        print('Try again with numbers!')

