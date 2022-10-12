# Week 6
[Link Deploy](https://tugas-pbp-dhafin.herokuapp.com/todolist)

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming adalah model pemrograman yang melakukan tugasnya banyak sekaligus secara paralel. Sedangkan, synchronous programming adalah model pemrograman yang mengharuskan program menyelesaikan suatu tugas terlebih dahulu baru melanjutkan ke tugas berikutnya. Asynchronous adalah arsitektur non-blocking, yang berarti tidak memblokir eksekusi lebih lanjut saat satu atau lebih operasi sedang berlangsung dan synchronous merupakan kebalikannya

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming adalah sebuah paradigma pemrograman di mana aliran program ditentukan oleh peristiwa seperti tindakan pengguna, seperti sebuah function yang terpanggil setelah user menekan tombol. Pada tugas 6 ini, saya menerapkan event-driven programming salah satunya pada menerapkan bonus, dimana ketika user klik button delete, `onClick="deleteCard(${data.pk})"` fungsi deleteCard pada id akan terpanggil.

## Jelaskan penerapan asynchronous programming pada AJAX.
AJAX memiliki kepanjangan Asynchronous JavaScript and XMLHTTP. Sehingga sebuah kode yang menerapkan AJAX akan berjalan secara asynchronous. Penerapannya adalah ketika user memberikan request, AJAX akan mengambil request tersebut dan mengirimkannya ke server agar datanya diubah secara asynchronous. AJAX akan memanfaatkan AJAX POST dan AJAX GET untuk melakukan proses tersebut secara asynchronous.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Import Jquery Ajax dengan tag `<script>` pada `todolist.html`
2. Buat views yang mengambil data json dan atur routenya
3. Membuat document.ready function agar ketika website tampil, untuk pertama kalinya ia akan merender data data task yang sudah ada pada server
4. Buat constant card pada ajax dan buat fungsi yang memasukkan data ke card tersebut. Kemudian dengan memanfaatkan ajax get, mengambil data dari todolist/json dan memasukkannya ke dalam card
5. Membuat modal menggunakan bootstrap dan mengimport bootstrap pada `base.html`
6. Mengatur isi modal dan memanfaatkan form yang kita buat ke dalam modal tersebut. Set id dari modal tersebut
7. Bikin function yang akan dijalankan apabila id tersebut di klik, kita bisa memanfaatkan function addCard yang kita sudah buat sebelumnya untuk post