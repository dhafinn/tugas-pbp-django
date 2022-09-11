# Tugas 2
### LINK DEPLOY
https://tugas-pbp-dhafin.herokuapp.com/

### Diagram Flow
![Bagan](https://user-images.githubusercontent.com/87629796/189527134-db461640-dc8d-49ef-a47c-86b4e52c041c.png) 
<br>
Cara aplikasi bekerja adalah user pertama-tama akan melakukan request dan akan diproses oleh middlewares yang akan diteruskan ke URL router. Kemudian, URLs mengecek apakah request dari user ada handler-nya pada program atau tidak, jika ada maka function pada views akan terpanggil. Setelah function terpanggil, aplikasi akan mengirimkan query request ke model dan model akan mengirimkan query request ke database. Kemudian, database akan mereturn data ke model dan model akan memberikannya ke views. Setelah itu, views akan menggunakan datanya pada template dan kemudian aplikasi akan mengirimkan response dengan data yang di request oleh user dalam bentuk html yang sudah dibuat di template.
<br>
<hr>

### Virtual Environment
**Apa itu virtual environment?** 
<br>
Virtual environment adalah semacam tools yang membuat sebuah space terpisah untuk suatu proyek memasang sebuah depedensi, packages, dan versi yang hanya dibutuhkan oleh proyek tersebut sehingga kita bisa mengeliminasi kemungkinan adanya konflik package di global environment. 

**Mengapa virtual environment penting?**
<br>
Seperti yang sudah di mention sebelumnya, menggunakan virtual environment penting agar proyek kita "terisolasi" dan bisa menginstall package, version, dan depedency tanpa harus takut ada konflik. Virtualenv juga membantu agar proyek kita lebih mudah dikerjakan oleh orang lain karena package yang dibutuhkan oleh proyek kita sudah tersimpan di virtual environment

**Apakah bisa kita mengerjakan suatu proyek tanpa menggunakan virtual environment?**
<br>
Jawabannya adalah bisa! Namun, jika anda ingin menginstall sebuah package, package tersebut akan tersebut terinstall pada global environment.
<br>
<hr>

### Implementasi
**Creating views.py function**
<br>
Setelah memahami soal, ternyata yang kita perlukan adalah menampilkan /katalog dengan data yang sudah diberikan pada initial_catalog_data.json. Dikarenakan html nya sudah disediakan pada template, maka kita hanya perlu membuat function yang menerima request dan mereturn html yang sudah di render dengan data yang sudah di query. Oleh karena itu, kita memerlukan method render sebagai return dari function ini. Kemudian, karena kita memerlukan data dari initial_catalog_data.json, import CatalogItem dan pakai dictionary context untuk menyimpan data yang sudah kita query menggunakan CatalogItem.objects.all(). Setelah itu, simpan dictionary context pada argumen ketiga method render.
<br>

**Creating a route**
<br>
Pertama buat route di urls.py pada folder project_django. Tambahkan method path baru pada urlpatterns dengan argumen pertama "katalog" sebagai app_name dan argumen kedua katalog.urls yang merujuk kepada route urls pada katalog app
<br>

Selanjutnya, setelah mengatur routing pada project_django, kita harus mengatur routing pada katalog app. Tambahkan urlpatterns dan path yang berisikan string kosong pada argumen pertama, fungsi yang kita buat sebelumnya pada argumen kedua, dan app name pada argumen ketiga. Finally you're set!
<br>

**Mapping the data into HTML**
<br>
Manfaatkan dictionary context yang sudah kita buat sebelumnya pada views sesuai dengan variable yang kita inginkan, misal untuk menggunakan name pada dict, kita bisa gunakan syntax {{name}}. Untuk mengisi tabel, kita manfaatkan iterasi agar bisa menampilkan semua nilai pada tabel.
<br>

**Deployment to Heroku**
<br>
Cara mendeploy ke heroku sama saja seperti yang pernah dipelajari pada Lab 0, pertama kita harus mendapatkan API_KEY terlebih pada account settings heroku. Kemudian, buat app baru pada heroku dan pergi ke bagian settings. Pada bagian settings, buka Convig Vars dan masukkan HEROKU_API_KEY sebagai key dan heroku account key yang tadi kita dapatkan sebagai value. Tambahkan lagi HEROKU_APP_NAME dan nama app nya sebagai key dan value. Setelah itu, pergi ke github > settings > secrets > action dan lakukan hal yang sama seperti pada config vars. Jika sudah, pergi ke github > actions dan coba run job. Aplikasi anda seharusnya sudah berhasil ter-deploy di HEROKU.
