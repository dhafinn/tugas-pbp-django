# Assignment 4 

## Apa itu CSRF Token dan mengapa penting pada form
CSRF adalah cross-site request forgery. Sesuai dengan namanya, CSRF adalah salah satu cara metode penyerangan yang dilakukan oleh sites yang berbahaya. Kadang kali, kita menginput data credential ke sebuah website yang kita percayai. Browser kita menyimpan cookies dari website yang kita kunjungi tersebut. Kemudian, kita mengunjungi website berbahaya dimana terdapat request berbahaya untuk mengambil data credential dari user. Selanjutnya karena web penyimpan data nya hanya memerlukan cookie session yang tersimpan pada browser user, maka web tersebut tidak bisa membedakan dan mengira bahwa request tadi adalah request sungguhan. Oleh karna itu, Django menyediakan **CSRF Token** yang merupakan kode rahasia acak yang unik untuk setiap situs tertentu. Setiap form yang dikirimkan oleh web kepada user, akan dikirimkan bersama CSRF Token sebagai proteksi dari serangan web berbahaya yang memimik behavior request.
Semua request yang masuk harus memiliki cookie CSRF, CSRF Token juga harus ada dan benar yang membuat sulit bagi penyerang untuk meniru request yang sama karena CSRF Token sangat panjang. Tanpa CSRF Token, user akan mendapatkan 403 error.

## Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})
Tentunya bisa, kita bisa membuat manual form dengan manual tanpa menggunakan. Caranya adalah diantara start tag dan end tag form, kita mengisi dengan `<input><\input>` sesuai dengan isi form yang kita inginkan. Setelah itu tambahkan `<input>` yang memiliki type submit untuk mensubmit form tersebut

## Alur data dari submisi form
Pertama user akan memencet button yang sudah di link dengan suatu function pada views.py, di mana akan di route ke sebuah function yang menerima request dan render forms.html dan menerima input user. Kemudian data yang diberikan user pada forms diambil pada function dan ditampilkan pada show_todolist

## Pengerjaan Checklist
* Pertama-tama buat aplikasi baru pada django kemudian masukkan nama apps pada settings.py project_django. Kemudian add path baru pada urls.py project_django agar bisa mengakses http://localhost:8000/todolist.
* Membuat model yang bernama Task dan attribute yang sesuai dengan yang diminta oleh soal.
* Mengimplementasikan form registrasi, login, logout dengan cara memanfaatkan form dan menyimpan hasilnya.
* Membuat templates untuk menampilkan todolist dan menambahkan berbagai kebutuhan yang diminta oleh soal.
* Membuat forms.py untuk mengambil data mengenai penambahan task user dan menampilkannya pada user dengan bantuan function pada views.
* Menambahkan urlpatterns baru pada urls.py untuk setiap function yang dibuat.
* Melakukan deployment ke heroku dan menambahkan 2 akun pengguna dan 3 model task.<br>
Akun 1: username = inidummy, password = gokillll <br>
Akun 2: username = inidummy2, password = kerennnn
