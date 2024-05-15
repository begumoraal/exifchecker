import PIL.Image
import PIL.ExifTags
from gmplot import gmplot
import webbrowser
from geopy.geocoders import Nominatim


class Bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'



def logo():
    print(Bcolors.RED + Bcolors.BOLD)
    logo = """
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,               ,,,     .,,,,,     ,,,,    ,,,,               ,,,,,,,,,
,,,,,,,,,,    ,,,,,,,,,,,,,,,,     ,,     ,,,,,,    ,,,,     ,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,    ,,,,,,,,,,,,,,,,,,        .,,,,,,,    ,,,,     ,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,              ,,,,,,,,,      ,,,,,,,,,    ,,,,              ,,,,,,,,,,
,,,,,,,,,,    ,*,*,*,*,*,,,,,,,,        ,,,,,,,,    ,,,,     ........,,,,,,,,,,,
,,,,,,,,,,    ,,,,,,,,,,,,,,,,     ,,     ,,,,,,    ,,,,     ,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,               .,,,     ,,,,      ,,,,    ,,,,     ,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,               .,     ,,,,,,,,     ,,,    ,,,,     ,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

    # v1.0.0 #
       >> EXIF TOOLS <<
       >> 20/12/2023 <<

    """
    print(logo)
    print(Bcolors.ENDC)



def exif_bilgilerini_incele(dosya_adi):
    try:
        img = PIL.Image.open(dosya_adi)

        exif = {
            PIL.ExifTags.TAGS[k]: v
            for k, v in img._getexif().items()
            if k in PIL.ExifTags.TAGS
        }

        tel_marka = exif.get("Make", "Bilinmiyor")
        tel_model = exif.get("Model", "Bilinmiyor")
        foto_tarih = exif.get("DateTime", "Bilinmiyor")

        konum = exif.get("GPSInfo")

        if konum:
            print(Bcolors.YELLOW + "Konum Bilgisi Bulundu. HTML Dosyasi İçerisine Yazdiriliyor....\n" + Bcolors.ENDC)

            north = konum[2]
            east = konum[4]
            lat = ((((north[0] * 60) + north[1]) * 60) + north[2]) / 60 / 60
            long = ((((east[0] * 60) + east[1]) * 60) + east[2]) / 60 / 60
            lat, long = float(lat), float(long)

            geo_locator = Nominatim(user_agent="GetLoc")

            location_info = geo_locator.reverse(f"{lat}, {long}", language="tr")

            print(f"Konum Adresi: {location_info.address}\n")

            webbrowser.open_new_tab(location_info.address)

        else:
            print(Bcolors.GREEN +"\nKonum Bilgisi Bulunamadi." + Bcolors.ENDC)

        print(Bcolors.GREEN + f"Telefon Markasi: {tel_marka}" + Bcolors.ENDC)
        print(Bcolors.GREEN + f"Telefon Modeli: {tel_model}" + Bcolors.ENDC)
        print(Bcolors.GREEN + f"Fotoğraf Çekilme Tarihi: {foto_tarih}\n" + Bcolors.ENDC)

    except FileNotFoundError:
        print(Bcolors.RED + "Dosya bulunamadi." + Bcolors.ENDC)
    except Exception as e:
        print(Bcolors.RED + f"Hata oluştu: {e}" + Bcolors.ENDC)

if __name__ == "__main__":
    logo()
    while True:
        dosya_adi = input(Bcolors.GREEN + "Lütfen görselin dosya adini girin (örneğin: test333.jpg, cikis icin 'q'): " + Bcolors.ENDC)

        if dosya_adi.lower() == 'q':
            break

        exif_bilgilerini_incele(dosya_adi)