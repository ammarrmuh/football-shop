link PWS = https://ammar-muhammad41-footballshop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step : 
    - pertama saya membuat direktori pada file lokal dengan nama 'footbal-shop' 
    - buka CMD lalu kemudian mengaktifkan python environment dalam direktori 'football-shop' tersebut dengan baris kode yang ada di dalam tutorial 0
    - setelah mengaktifkan environment saya kemudian membuat requirements.txt di dalam direktori untuk kemudian di lakukan instalasi dalam CMD
    - setelah kebutuhan saya terinstall dengan baik saya kemudian start project django tersebut untuk memulai project football-shop
    - setelah project di start saya kemudian membuat direktori '.env'  dan '.env.prod' untuk mengkonfigurasi production serta database milik saya
    - setelah konfigurasi berhasil saya kemudian melakukan modifikasi pada settings yakni melakukan 'load_dotenv' serta mengubah isi dari 'ALLOWED_HOST' supaya saya dapat mengecek hasil dari kerja saya
    - di dalam settings saya juga kemudian menambahkan konfigurasi PRODUCTION serta menggati DATABASES 
    - kemudian saya melakukan migrasi database supaya server dapat dijalankan dengan aman
    - setelah semua hal tersebut selesai saya kemudian menambahkan repository ke git hub serta menambahkan berkas '.gitignore'
    - kemudian saya menghubungkan repo github saya dengan file lokal yang sudah saya buat serta membaut branch master untuk menjaga konsistensi dari editing kode saya
    - setelah terup di github saya kemudian melakukan konfigurasi pada PWS dan menambahkan link PWS dalam allowed host
    - setelah semua persiapan project berjalan dengan baik saya kemudian melakukan aplikasi MTV
    - MTV dilakukan dengan mendaftarkan aplikasi main ke dalam proyek di bagian INSTALLED APPS
    - kemudian di dalam main saya membuat direktori 'templates' untuk bisa saya isi
    - saya kemudian melakukan implementasi models PRODUCT dan melengkapi fitur fitur yang diwajibkan oleh soal
    - setelah melakukan beberapa perubahan pada models, saya melakukan migrasi 
    - setelah model diterapkan say kemudian melakukan konfigurasi pada 'views' untuk dapat menerapkan database yang saya siapkan
    - setelah views berhasil di konfigurasi, saya melanjutlan dengan melakukan konfigurasi pada routing URL yang pertama pada aplikasi main untuk dapat menampilkan show_main
    - setelah mengkonfigurasi hal tersebut saya berlanjut untuk melakukan konfigurasi dalam skala proyek
    - setelah hal tersebut di konfigurasi saya melakukan git commit pada kode saya dan program telah berhasil.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    pertama Client (browser) mengirimkan HTTP Request ke server Django. --> urls.py mencocokkan URL yang diminta dengan pola yang sudah didefinisikan. --> views.py berisi fungsi/class view yang akan dipanggil jika URL cocok. --> Jika butuh data dari database, view akan memanggil models.py. --> models.py mengambil/menyimpan data dari/ke database dan mengembalikannya ke view. --> 
    views.py menyiapkan context (data) lalu merender HTML template. --> Template (HTML) menggabungkan data dari view dengan struktur tampilan. --> Django mengirimkan HTTP Response (HTML yang sudah jadi) kembali ke client.

    urls.py berfungsi seperti pintu masuk yang dapat memberi akses pada URL kepada views.py
    kemudian views.py berperan sebagai sebuah operasi yang mengatur apa yang perlu dilakukan ketika URL diakses
    selanjutnya untuk dapat mengolah data yang ada dalam database models.py berperan sebagai penjembatan untuk megelola data tersebut
    erkas HTML yang tersedia menjadi tampilan bagi pengguna untuk dapat melihat data yang disediakan dengan lebih rapi

3. Jelaskan peran settings.py dalam proyek Django!
    settings.py berfungsi sebagai tempat utama untuk kita dapat melakukan konfigurasi pada proyek kita karena di dalamnya menyimpan banyak informasi seperti informasi dasar, aplikasi yang kita buat, database dan lain lain sehingga perannya sangat penting untuk keberlangsungan berjalannya suatu project berlandaskan django


4. Bagaimana cara kerja migrasi database di Django?
    pertama migrasi dilakukan bila sedang membuat model atau telah membuat model yang baru yang dimana nantinya berfungsi untuk jalannya projek kita, setelah kita membuat model yang kita inginkan kita perlu untuk membuat catatan terkait perubahan yang kia lakukan dengan 'makemigrations' setelah hal itu dilaksanakan barulah kita melaksanakan 'migrate'

    secara cara kerja ketika tahap makemigrations, Django akan membaca perubahan yang kita lakukan pada models.py kemudian membuat file migrasi di folder migrations, file ini akan berisi instruksi python untuk membuat/mengubah tabel di database

    kemudian ketika migrate dilaksanakan, Django akan mengeksekusi file migrasi tersebut ke datase dengan membuat tabel baru, menambah/menghapus kolom, mengubah tipe data kolom, dll
    Django juga mencatat status dari migrasi dalam tabel khusus bernama 'django_migrations' supaya nantinya kita dapat mengetahui migrasi mana yang sudah diterapkan

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    menurut saya sebagai pemula yang dulu telah mencoba berbagai platform untuk mengembangkan suatu software ketika saya dalam ajang perlombaan, menurut saya django memiliki keunggulan untuk dapat dipelajari oleh pemula karena saya lebih mudah memahami alur dan "harus ngapainnya" dibandingkan ketika saya mempelajari framework lain seperti flutter dkk, ia juga meruapakan framework yang cukup lengkap, aman, serta banyak didukung oleh berbagai community dalam pengaplikasiannya, tak lupa juga karena saya telah lama tidak bertemu python menurut saya ini merupakan sebuah refreshing dalam bahas python sehingga mudah untuk dipahami.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    sejauh ini saya sangat senang dengan semua asdos yang menemani dan membantu saya dalam mata kuliah pbp ini, semua asdos yang saya tanyai sangat amat membatnu dan bisa menerangkan dengan jelas, tidak hanya membantu tapi juga mengerti bagaimana membuat saya paham sembari menerapkan "ini lho nanti kegunaannya untu kini kedepannya" sehingga saya lebih mengerti tentang apa yang penting dan yang harus dilakukan dalam mata kuliah ini. saya sangat berharap semoga kedepannya hal ini dapat dipertahankan dan semangattt untuk kakak kakak asdos <3.