Nama    : Fatih Raditya Pratama

NPM     : 2206083520

Kelas   : PBP A

1. 
Membuat proyek baru di Django,
-pertama bikin directory baru

-nyalakan virtual environment di directory dan masukkan requirements.txt yang berisi
requirements yang dibutuhkan

-install semua lewat pip install

-menjalankan command "python manage.py startapp ('app name')"di directory

-tambahkan 'app name'(disini namanya 'main') di installed_apps dalam settings.py direktori project

-Setelah itu kita akan mmebuat directory templates dalam directory 'main' dan akan menambahkan 
main.html ke dalamnya

-Untuk membuat models, kita bisa melakukan:
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

untuk name, amount, dan description, pakai field yang sesuai, untuk
models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
Tidak lupa setelah ini kita perlu migrasi model data ini  untuk mengubah struktur tabel basis data 
sesuai dengan perubahan model yang didefinisikan dalam kode, kita bisa melakukan migrasi dengan cara:

python manage.py makemigrations ---> makemigrations menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data

diikuti dengan

python manage.py migrate ---> migrate mengaplikasikan perubahan model yang ada di basis data

-Setelah pembuatan model dan migrasi model selesai, kita bisa membuat function di views untuk di return ke html kita dengan cara:

def show_main(request):
    context = {
        'name': 'Fatih Raditya Pratama',
        'class': 'PBP A',
    }

    return render(request, "main.html", context)

-Kita bisa melakukan routing ke main.html dengan cara:

from django.urls import path, include
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('main/',include('main.urls'))
]

path 'main/' akan mengarahkan ke urls.py di directory main

-Setelah semua ini selesai, kita tinggal commit dan push ke repository github dan hubungkan ke adaptable

2.
![BAGAN-WebBasedDjangoApp!](PBP-Tugas2.png)

-Jadi, saat client melakukan request, dan jika valid diterima oleh web server, dan
diturunkan ke Django
-Django menentukan URL
-URL akan menentukan view mana yang dipilih
-view akan mengambil model
-models tersebut digunakan view untuk diteruskan ke template(html)
-template(html) diteruskan dan ditampilkan ke pengguna

3. 
Perbedaan MVC, MVT, dan MVVM
-MVC(Model-View-Controller)
-MVT(Model-View-Template)
-MVVM(Model-View-Viewmodel)
Pada ketiga ini, model dan view itu sama, model untuk mengelola data aplikasi dan
view adalah bagian yang mengatur bagaimana data dari model ditampilkan ke user.

-Pada MVC, Controller bertanggung jawab untuk menerima input dari user dan mengupdate
view dan model
-Pada MVT, Template bertanggung jawab untuk menampilkan hasil kepada user (biasanya html)
-Pada MVVM, ViewModel bertanggung jawab untuk menghubungkan view dan model, jadi kayak
semacam gabungan antara view dan model

P.S
Selain 2 tes di tests.py saya menambahkan satu test lagi