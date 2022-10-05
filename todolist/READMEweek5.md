# Week 5

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline CSS: Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML dengan cara menambahkan `style=""` pada tag HTML. <br>
Internal CSS: Internal CSS adalah kode CSS yang ditulis di dalam tag `<style>` dan kode HTML dituliskan di bagian atas (header) file HTML <br>
External CSS: Eksternal CSS adalah kode CSS yang ditulis terpisah pada sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian `<head>` HTML <br>
<br>
Kelebihan dan kekurangan: <br>
Inline CSS: Lebih cepat loadtime nya, mudah digunakan untuk tracing permasalahan css yang tidak sesuai dengan keinginan kita, tetapi melelahkan karena harus menambahkan pada setiap elemen.<br>
Internal CSS: Berlaku untuk satu halaman, tidak menggunakan file tambahan sehingga tidak perlu linkan file. Tetapi tidak efisien jika ingin dipakai pada file HTML lain dengan css yang sama.<br>
External CSS: Kode HTML menjadi lebih rapih karena terpisah, File css bisa dipakai di banyak halaman sekaligus, tetapi akan sulit di trace permasalahan dan terdapat kemungkinan file css gagal dipanggil.

##  Jelaskan tag HTML5 yang kamu ketahui.
`<h1> - <h6>` merupakan heading, `<p>` digunakan untuk menulis paragraf, `<a>` untuk menggunakan hyperlink, biasanya digunakan dengan `href=""`, `<button>` untuk membuat button, `<ul>` untuk membuat list tanpa angka `<ol>` dengan angka dan `<li>` adalah isi dari listnya. `<img>` untuk menambahkan image. `<form>` untuk membuat form. `<div>` sebagai tempat untuk menaruh elemen html dalam suatu "container".

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Class selector dengan implementasinya `.classname` yang berfungsi untuk memilih class yang memiliki nama yang sesuai. Id selector untuk memilih id yang sesuai dengan cara mengimplementasikan kode `#idname`. Child selector `>` untuk memilih semua element yang ada di dalam atau child sebuah komponen

## Checkpoint
Pertama-tama saya menggunakan tailwind dengan cara menambahkan `<script src="https://cdn.tailwindcss.com"></script>` pada `<head>` base.html. Kemudian saya melakukan styling pada login dengan cara membuat sebuah login card pada tengah halaman. Begitupula pada halaman register.html, tambahan yang saya lakukan pada saat ini adalah melepas form dari table dan menspesifikasikan form nya secara satu satu. Setelah itu saya memperindah page todolist.html dan menambahkan card 1 per satu sesuai task. Dengan bantuan tailwind, saya memanfaatkan `grid lg:grid-cols-4 md:grid-cols-2` untuk menciptakan page todolist yang responsive dan tidak terjadi overflow. Selanjutnya untuk page create-task saya mengimplementasikan hal yang kurang lebih sama dengan apa yang saya gunakan pada register.html dan login.html



