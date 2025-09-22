1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

AuthenticationForm adalah form bawaan dari Django yang disediakan oleh django.contrib.auth.forms. ia berfungsi untuk melakukan verifikasi kredensial user dimana ia mengecek apakah username ada di database, apakah passwordnya cocok dengan user tersebut, serta menyimpan informasi user yang sudah di verifikasi

Kelebihan :
- tidak perlu menulis logika validasi manual
- terintegrasi dengan sistem auth Django sehingga bisa langsung digunakan dengan login view
- mudah untuk di custom 

Kekurangan: 
- terbatas pada username dan password jadi kalo aplikasi kita butuh login via email dll perlu di custom lagi
- kurang felsibel buat interface moderen sekarang

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

autentikasi adalah proses memverifikasi identitas user, otorisasi adalah proses menentukan hak akses user setelah identitasnya diverifikasi

implementasi:
pertama django menggunakan django.contrib.auth kemudian user akan login via authentication form, middleware authenticationmiddleware akan menambahkan atribut request user, kemudian django akan menggunakan sistem permission dan groups untuk melakukan otorisasi 

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

COOKIES
Kelebihan:
- disimpan di sisi client (browser)
- tidak membebani server, cocok untuk data yang kecil
- bisa dipakai lintas request tanpa server-side session.

kekurangan: 
- mudah dimanipulasi oleh user jika menimpan data penting
- ukurannya terbatas
- menambar overhead pada request karena dikirim di tiap http request

SESSION
Kelebihan:
- Disimpan di server-side → lebih aman untuk data sensitif (misalnya user_id).
- Lebih fleksibel, bisa simpan data kompleks.
- Hanya menyimpan session ID di cookie (sessionid).

Kekurangan:
- Membebani server (butuh storage untuk setiap session).
- Butuh mekanisme expired / cleanup session.
- Tidak cocok untuk aplikasi berskala besar tanpa manajemen session yang baik (misalnya pakai Redis).

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

penggunaan cookies tidak sepenuhnya aman secara default karena cookie bisa dicuri via XXS, ia juga bisa disadap via man-in-the-middle, cookies juga bisa dimodifikasi di browser. resiko potensial yang harus diwaspadai adalah session hijacking dimana hacker mencuri sesion id, session fixation dimana hacker memaksa user memakai session id tertentu, serta CSRF 

Django menangani hal tersebut dengan :
- Secure flag (SESSION_COOKIE_SECURE=True) → hanya terkirim lewat HTTPS.
- HttpOnly flag (SESSION_COOKIE_HTTPONLY=True) → tidak bisa diakses lewat JavaScript.
- SameSite flag (SESSION_COOKIE_SAMESITE='Lax' / 'Strict') → mencegah CSRF.
- CSRF Token → Django otomatis menambahkan proteksi CSRF pada form POST.
- Signed cookies (django.core.signing) → Django bisa menandatangani cookie agar tidak bisa dimodifikasi sembarangan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

pertama saya mengimport usercreationform serta message yang terdapat di django untuk dapat mengimplementasikan login dan logout yang nantinya di buat, kemudian lanjut untuk mengimplementasikan function function yang dibutuhkan seperti register, login, dan logout setelah function diimplementasikan saya kemudian membuat html baru untuk memberi page pada register serta login, kemudian menambahkan kedua hal tersebut dalam urls, kemudian setelah mengimplementasikan hal teersebut kita kemudian menambahkan dekorator untuk dapat memberitahu bahwa sebelum dilakukan kode berikutnya, memerlukan login terlebih dahulu. setelah function selesai kemudian kita melakukan update pada login user untuk bisa menggunakan cookies serta melakukan update pada context. setelah semua hal tersebut selesai kita mengubah model supaya user dapat di deteksi kemudian melakukan migrate supaya model terupdate.
