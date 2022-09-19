# Link Deploy:
https://tugas-pbp-dhafin.herokuapp.com/
<br>
<hr>

# Perbedaan HTML, JSON, XML
JSON digunakan untuk mengirimkan data yang berbentuk objek dan XML merupakan Markup Language yang menggunakan tag structure untuk merepresentasikan data karenanya memiliki kapabilitas untuk menampilkan data sedangkan JSON tidak memiliki kapabilitas itu. Dibutuhkan untuk mendefinisikan tags untuk merepresentasikan suatu datanya. Meski begitu, XML di desain untuk membawa dan menyalurkan data, berbeda dengan HTML yang di desain untuk menampilkan data. Walaupun XML dan HTML merupakan turunan dari SGML, XML tags tidak predefined seperti HTML. JSON juga lebih mudah dibaca dengan mata manusia dibandingkan XML dan HTML karena XML dan HTML membutuhkan tags di setiap datanya yang membuat lebih sulit untuk dibaca. JSON mendukung tipe data, dari numbers hingga integer, string, dan array. Tetapi dalam kasus XML dan HTML, karena keduanya merupakan cabang data format dari (SGML), maka tidak ada dukungan langsung untuk mengolah data bertipe array. Oleh karena itu, bantuan oleh struktur data lain diperlukan. JSON hanya support UTF-8 Encoding sedangkan XML support beragam encoding. Selain itu, XML lebih aman dibandingkan dengan JSON dan juga menyediakan namespace support dimana JSON tidak menyediakan.
<br>

# Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
Jawaban untuk pertanyaan ini sebenarnya sangatlah sederhana. Dalam prosesnya, sebuah platform pasti akan digunakan oleh seorang user. Untuk membuat sebuah platform yang baik, seharusnya interaksi berjalan dua arah dimana user bisa melakukan CRUD (Create, Read, Update, Delete) data sesuai keinginannya. Oleh karena itu, dibutuhkan data delivery untuk membuat platform yang dynamic. Selain itu, mengapa data delivery dibutuhkan, jawabannya adalah karena data delivery tools seperti XML dan JSON ini membantu kita menyimpan, mentransfer, dan bahkan mengambil atau membaca data dari database yang non-readable bagi manusia menjadi suatu bentuk lain yang mudah dibaca oleh manusia seperti contohnya HTML. XML dan JSON ini digunakan untuk mengirimkan data dari satu ke lain komputer sehingga data delivery ini bisa diibaratkan seperti "Jembatan" dari banyaknya platform yang berada di internet. Tanpa adanya data delivery ini, platform kita akan sulit untuk mengambil dan menyimpan data, dan juga tidak akan bisa "berkomonikasi" kepada banyak platform diluar sana.
<br>

# Implementasi
Pertama-tama, buat aplikasi baru bernama mywatchlist dengan menjalankan command ```python manage.py startapp mywatchlist``` <br>

Setelah itu tambahkan `mywatchlist` di INSTALLED_APPS pada settings.py project_django. Kemudian tambahkan path baru `path('mywatchlist/', include(mywatchlist.urls'))` yang mengarah ke mywatchlist.urls pada project_django/urls.py <br>

Setelah itu pada mywatchlist/models.py buat MyWishList model yang menyimpan attribute watched dengan boolean field, title dengan CharField, rating dengan FloatField, release_date dengan DateField dan review dengan TextField. Setelah itu buat data dengan format JSON di dalam folder fixtures. Setelah membuat model dan membuat datanya, jangan lupa untuk migrate data tersebut dengan command `python manage.py makemigrations` dan juga `python manage.py migrate` jangan lupa juga untuk loaddatanya dengan command `python manage.py loaddata <nama_file_json>`.

# Postman
## HTML Response
![html](https://user-images.githubusercontent.com/87629796/191050800-2b138b15-5feb-4c05-8da6-60cec6b62a69.jpg)

## JSON Response
![json](https://user-images.githubusercontent.com/87629796/191051050-355c2c75-1ff9-4f3b-a7f0-9d6644ba48c9.jpg)

## XML Response
![xml](https://user-images.githubusercontent.com/87629796/191051385-ebe986ac-e0bf-49f8-9d17-f8ca3a16876d.jpg)








