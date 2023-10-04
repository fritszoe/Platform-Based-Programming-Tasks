Nama    : Fatih Raditya Pratama

NPM     : 2206083520

Kelas   : PBP A
#
<details>
<summary>TUGAS-2</summary>
1.  
Membuat proyek baru di Django:  

-pertama bikin directory baru  

-nyalakan virtual environment di directory dan masukkan requirements.txt yang berisi
requirements yang dibutuhkan  

-install semua lewat pip install  

-menjalankan command "python manage.py startapp ('app name')"di directory  

-tambahkan 'app name'(disini namanya 'main') di installed_apps dalam settings.py direktori project  

-Setelah itu kita akan mmebuat directory templates dalam directory 'main' dan akan menambahkan
main.html ke dalamnya  

-Untuk membuat models, kita bisa melakukan:  
```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```


untuk name, amount, dan description, pakai field yang sesuai, untuk
models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
Tidak lupa setelah ini kita perlu migrasi model data ini  untuk mengubah struktur tabel basis data 
sesuai dengan perubahan model yang didefinisikan dalam kode, kita bisa melakukan migrasi dengan cara:

python manage.py makemigrations ---> makemigrations menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data

diikuti dengan

python manage.py migrate ---> migrate mengaplikasikan perubahan model yang ada di basis data

-Setelah pembuatan model dan migrasi model selesai, kita bisa membuat function di views untuk di return ke html kita dengan cara:
```python
def show_main(request):
    context = {
        'name': 'Fatih Raditya Pratama',
        'class': 'PBP A',
    }

    return render(request, "main.html", context)

```

-Kita bisa melakukan routing ke main.html dengan cara:
```python
from django.urls import path, include
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('main/',include('main.urls'))
]
```
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
Venv(Virtual Environment), berguna untuk menjalankan project dengan dependencies yang berbeda-beda dalam
satu sistem operasi yang sama.


4. 
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
</details>

#
<details>
<summary>TUGAS-3</summary>


1.
Perbedaan form POST dan form GET pada Django:

POST
Metode POST mengirimkan data sebagai bagian dari permintaan HTTP, yang tidak terlihat di URL

GET
Metode GET bundling data menjadi string yang nantinya akan ditampilkan pada URL.

Sumber:
https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=GET%20and%20POST%20are%20typically,the%20state%20of%20the%20system.

2.
HTML vs XML vs Json

HTML: HTML memiliki elemen khusus dan atribut yang digunakan untuk menentukan struktur dan tampilan konten web, jadi biasanya digunakan untuk halaman web, html juga bisa diubah tampilannya dengan menggunakan CSS dan Javascript.

XML: Dokumen XML membentuk struktur seperti tree yang dimulai dari root, lalu branch, hingga berakhir pada leaves. Dokumen XML harus mengandung sebuah root element yang merupakan parent dari elemen lainnya. XML memungkinkan penggunaan karakteristik khusus dan definisi dari dokumen karena XML didesain menjadi self-descriptive, kita bisa paham apa yang ada di XML dengan membaca XML nya. XML lebih mudah dibaca bagi orang awam.

Json: Json merupakan pasangan *key* *value* pair seperti dictionary pada Python dan map di Java, Json akan lebih sulit dipahami bagi orang awam yang melihat tapi pasti akan lebih mudah dipahami bagi pengembang karena Json merupakan turunan dari Javascript.

3.
Kenapa Json sering digunakan?

Json adalah turunan dari Javascript sehingga orang-orang yang berpangalaman dengan Javascript tentunya akan lebih suka menggunakan Json, dan karena Javascript juga banyak yang pakai, pasti yang pakai Json juga banyak. Selain itu, Json dinilai *lightweight*.

4.
-Making Forms

Untuk membuat forms pertama kita buat file forms.py di main aplikasi, kita bisa menggunakan
ModelForm dari Django dan import Product dari models yang ada di main, setelah itu, kita bisa
assign model=Product untuk menyimpan objek yang dibuat di form menjadi objek Product. Setelah itu
kita akan menambahkan fields yang telah kita buat di models yaitu name,price, dan description.

Setelah membuat forms.py kita bisa menambahkan method create_product di views untuk menambahkan
product yang kita buat di form ketika kita submit form-nya. kita declare form = ProductForm(request.POST or None) 
untuk membuat ProductForm berdasarkan input user di request.POST. Setelah itu, kita bisa cek apakah form nya
sudah valid atau belum dan kita simpan. Kita juga bisa gunakan HTTPResponseRedirect untuk redirect setelah data form
berhasil di simpan. 

Setelah itu, kita bisa menambahkan products nya di fungsi show_main yang ada di views untuk menampilkannya. Dan juga
kita harus menambahkan fungsi create_product di urls.py dan menambahkan path untuk menuju halaman form pembuatan product.
Setelah itu barulah kita buat halaman html nya.

2&3.  

-Menambahkan fungsi di views untuk Show HTML, XML, JSON, XML by ID, dan JSON by ID  

-Menambahkan routing  

-HTML:  

fungsi untuk show HTML sudah ada dari tugas sebelumnya yaitu show_main yang akan menggunakan fungsi render untuk mengambil 3 argumen yaitu context, request, dan main.html yang nantinya akan di render di satu main.html

-XML:  

Untuk mengembalikan data dalam bentuk XML kita bisa menggunakan serializer dan HTTPResponse, serializer digunakan untuk
mengubah/transalasi objek menjadi XML, lalu kita akan membuat fungsi show_xml yang akan return HTTPResponse untuk menampilkan
objek dalam bentuk xml
```python
return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
HTTPResponse berguna untuk mengembalikan menjadi laman yang bisa dilihat, setelah ini tidak lupa kita akan menambahkan path di
urls.py untuk menampilkan laman dalam fomat xml
```python
path('xml/', show_xml, name='show_xml'),
```
-JSON:  

Untuk JSon juga sama, menggunakan serializer dan HTTPResponse dan tidak lupa menambahkan path di urls.py untuk show dalam format
json, bentuk return dan path nya hanya tinggal diganti dengan json
```python
return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
ini routing nya
```python
path('json/', show_json, name='show_json'),
```
-XML & Json by ID:  

Sekarang untuk return data berdasarkan ID dalam XML dan Json kita bisa menambahkan variabel baru seperti ini.
```python
data = Product.objects.filter(pk=id)
```
Yang akan menyimpan hasil query dari data dengan id tertentu. Setelah itu barulah kita return seperti biasa
menggunakan HTTPResponse dan juga serializer, xml untuk format xml dan json untuk format json(sama seperti sebelum-sebelumnya). Tidak lupa kita akan menambahkan routing di urls.py, sama seperti sebelumnya:
```python
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),

path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
```

Seperti di atas.

Screenshot Postman

![ScreenshotPostmanHTML!](PBP-Tugas3-1.png)
![ScreenshotPostmanXML!](PBP-Tugas3-2.png)
![ScreenshotPostmanJSON!](PBP-Tugas3-3.png)
![ScreenshotPostmanXMLByID!](PBP-Tugas3-4.png)
![ScreenshotPostmanJsonByID!](PBP-Tugas3-5.png)

Function untuk show jumlah barang yang ada:

Kita bisa import fungsi sum yang ada dari library django dan aggregate, fungsi sum berguna untuk
menjumlahkan numericalField, integer, float, dsb. Aggregate sendiri adalah method yang diperlukan
jika ingin menggunakan fungsi-fungsi seperti Sum, Avg, Count, Max, Min, dll. Ini semua karena
Sum, Avg, Count, Max, Min, dll itu adalah bagian dari aggregate functions yang membutuhkan aggregate
method. Berikut adalah code nya:
```python
def show_main(request):
    ...
    total_amount = products.aggregate(Sum('amount'))['amount__sum']

    context = {
        ....
        'totalAmount': total_amount,
    }

    return render(request, "main.html", context)
```
#
</details>

<details>
<summary>TUGAS-4</summary>

##
Register:

Dengan memanfaatkan UserCreationForm bawaan, kita bisa membuat tampilan html baru dan akan lakukan routing ke page tersebut, lalu dengan fungsi register di views.py dengan query berdasarkan input user di {request.POST} dan pada akhirnya akan return kembali ke main

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
###
Login:

Membuat login page, kita perlu membuat suatu fungsi lagi di views.py dan akan memanfaatkan {authenticate} dan {login} dari library django, authenticate(request, username=username, password=password) digunakan untuk melakukan autentikasi pengguna berdasarkan username dan password yang diterima dari permintaan (request) yang dikirim oleh pengguna saat login. Setelah itu, kita akan buat page login.html tidak lupa dengan routing, login.html adalah sarana untuk user login dan kita akan restriksi page main dengan cara menambahkan 
```python
@login_required(login_url='/login')
```
pada fungsi show_main agar mengarahkan page ke login.html, jadi user harus login untuk melihat page main.
###
Logout:

Untuk logout, kita bisa memanfaatkan logout dari django, user akan logout berdasarkan input user dan jika logout akan kembali ke page login.
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Untuk input dari user sendiri kita bisa menambahkan button logout di main.html
###
Dummy Account:

Membuat dummy account, kita bisa menggunakan fitur register yang sudah dibuat sebelumnya, saya akan membuat dua dummy account masing-masing bernama bader dan franku. Masing-masing dengan tiga data unique.
####
bader:

Akun bader berisi tiga item: HG 1/144 MS-06s Char's Zaku-II, HG 1/144 MS-05s Char's Zaku-I, dan 1/100 Full-Mechanics Gundam Aerial 

franku:

Akun franku berisi tiga item: PG RX 0 1/60 Unicorn Gundam, PG 1/60 GN-001 Gundam Exia, dan PG MS-06 F 1/60 Zaku II
###
Menghubungkan model item dengan user:

Hal ini dilakukan supaya setiap account punya item-item unik tersendiri yang berbeda dengan akun lain. Untuk melakukan ini, kita bisa menambahkan model user di models.py directory main, lalu tambahkan di class product,
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
Jadi, sebuah product akan terasosiasi dengan seorang user dengan suatu ForeignKey. Setelah itu, pada fungsi create_product di views.py bisa kita edit menjadi;
```python
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
param commit=false berguna untuk mencegah Django untuk tidak langsung menyimpan objek yang dibuat ke dalam database, jadi objek tersebut bisa dimodifikasi dahulu sebelum disimpan. Pada kasus ini, kita akan mengisi field user dengan objek User dari return value request.user yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.
###
User details and cookies:

Untuk menambahkan detail seperti siapa yang sedang login, kita bisa menambahkan di context fungsi show_main seperti ini:
```python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
...
```
Dimana request.user.username akan me return username dari user yang sedang login. Untuk cookies sendiri, seperti last login nya kapan, kita bisa menambahkan di login_user;
```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```
Jadi dengan penambahan cookie last login, kita akan menyimpan string berupa datetime dari saat user tersebut login, dan untuk menampilkannya di main, kita tinggal menambahkan seperti di context views.py dan tampilkan di main di bawah tombol logout seperti ini;
```python
context = {
    'name': 'Pak Bepe',
    'class': 'PBP A',
    'products': products,
    'last_login': request.COOKIES['last_login'],
}
```
```html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```
Oh iya, tidak lupa, kita juga akan delete cookie last_login saat logout, kita bisa menambahkan seperti ini di fungsi logout_user;
```python
response.delete_cookie('last_login')
```
##
###
Apa itu Django UserCreationForm?

Django UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal. Tapi kekurangan dari UserCreationForm ini adalah adanya keterbatasan dalam kustomisasi UI dan tidak suitable untuk penggunaan yang lebih kompleks.
###
Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Authentication adalah proses untuk mengetahui siapa ini, siapa yang sedang menggunakan, contoh dari authentication adalah login. Tujuan dari adanya authentication adalah untuk memastikan sang pengguna adalah orang yang di klaim.

Authorization adalah proses verifikasi untuk memastikan apakah kita punya akses terhadap sesuatu. Jika tidak ada authorization, maka pengguna random bisa saja menghapus sesuatu yang penting milik pengguna tertentu.

Keduanya ini sangatlah penting karena dua ini adalah dasar konsep keamanan aplikasi web.
###
Cookies?

Cookies adalah data kecil yang disimpan pada perangkat pengguna oleh browser web sebagai respons atas permintaan dari server web. Data ini dapat berupa informasi singkat, seperti pengenal sesi, preferensi pengguna, atau informasi lainnya yang diperlukan oleh aplikasi web. Cookies memungkinkan aplikasi web untuk menyimpan informasi di perangkat pengguna dan mengaksesnya kembali di masa mendatang. Cookies pada django pada dasarnya juga melakukan hal yang sama.
###
Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Walaupun cookies adalah hal yang umum dalam sebuah aplikasi web, tapi kita harus tetap waspada karena cookies bisa saja melanggar hak privasi kita dan mengambil data-data pribadi tanpa izin.
</details>

#
<details>
<summary>TUGAS-5</summary>

##
Pertama kita menambahkan bootstrap, CSS, dan JS,setelah itu, saya menambahkan navbar pada main
```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Welcome, {{name}}</a>
            <a style = "border-color: darkgrey; border-style: solid; padding: 0.01 rem; border-width: 5px;" href="{% url 'main:logout' %}">
                <button>
                    Logout
                </button>
            </a>
        </div>
    </nav>
```
di sini navbar saya memiliki brand yang berisi sapaan pada username, lalu ada button 'Logout' yang akan menggiring user ke fungsi logout.

Selanjutnya, saya mengubah tampilan pada main.html menggunakan card, dan utk objek terakhir, akan diberi warna berbeda dari card sebelumnya
```html
 <div class="row">
        {% for product in products %}
            <div class="col-md-4 mb-3{% if forloop.last %} last-card{% endif %}">
                <div class="card custom-card{% if forloop.last %} last-product-card{% endif %}">
                    <div class="card-body">
                        <h5 class="card-title">{{ product.name }}</h5>
                        <p class="card-text">Amount: {{ product.amount }}</p>
                        <p class="card-text"> Description:<br>
                            {{ product.description|linebreaks }}</p>
                        <p class="card-text">Price: ${{ product.price }}</p>
                        <a href="{% url 'main:edit_product' product.pk %}" class="btn btn-primary btn-sm">Edit</a>
                        <a href="{% url 'main:delete_product' product.pk %}" class="btn btn-danger btn-sm">Delete</a>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
    <style>
        .last-product-card {
            background-color: khaki; /* Specify the desired background color */
        }
    </style>
```
Pada saat melakukan looping, saya menambahkan kondisi if loop.last maka last nya menjadi last-product-card yang saya atur background color nya jadi berbeda

Selain di main, saya juga menambahkan navbar pada create_product
```html
{% extends 'base.html' %} 

{% block content %}
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="{% url 'main:show_main' %}">Back to main</a>
        <a href="{% url 'main:logout' %}">
            <button>
                Logout
            </button>
        </a>
    </div>
</nav>
<h1>What would you like to add today?</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Pada brand navbar yang isinya 'back to main' saya menambahkan url utk kembali ke main, jadi tidak hanya sekedar label, jika user click navbar brand, mereka akan dikembalikan ke main. Satu lagi, saya menambahkan 'price' di models karena sepertinya diperlukan.
<br>
PERTANYAAN
1. Selectors

-Element selector:
Memungkinkan utk mengubah properti utk semua elemen yang memiliki tag HTML yang sama
Ini biasanya digunakan kalau kita ingin apply style yang sama utk satu elemen di website kita

-ID selector:
Selector menggunakan id, id unique utk satu halaman web, id dapat ditambahkan pada template HTML
Id selector digunakan jika kita ingin apply suatu style spesifik ke satu halaman

-Class selector:
Class selector memungkinkan utk mengelompokkan elemen dengan karakteristik sama
Jadinya class selector digunakan jika kita ingin apply suatu style utk sekelompok elemen dengan karakteristik sama

2. Margin and Padding

Margin: ruang di luar elemen, digunakan utk mengatur jarak di luar, jadi ga keliatan numpuk atau terlalu berdempetan

Padding: padding digunakan untuk membatasi konten dalam elemen, seperti batas ujung paragraf di word, ga sampai di pinggir kertas nya

3. Bootstrap vs Tailwind

Bootstrap sudah memiliki elemen siap pakai, jadi utk komponen-komponen sudah di pre-design oleh bootstrap, 

Tailwind adalah framework utility-first, yang berarti itu memberikan banyak utility classes yang dapat langsung digunakan di HTML untuk membangun desain. Lebih banyak fokus pada penggunaan kelas yang menggambarkan apa yang ingin dicapai, bukan penggunaan komponen

Jadi, bootstrap digunakan jika kita perlu bekerja cepat, karena komponen-komponen sudah di pre-design oleh bootstrap, sedangkan utk Tailwind, itu bagus jika kita ingin benar2 kustomisasi secara bebas dan tidak terikat pada suatu hal spesifik.
</details>

#
..