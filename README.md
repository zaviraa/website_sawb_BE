# SAWB (Sedulur Aspirasi Warga Banyumas)
SAWB adalah sebuah website yang bertujuan untuk memberikan informasi dan platform bagi warga Banyumas untuk berbagi aspirasi dan berita terkini. Website ini dibangun menggunakan Django dan Bootstrap.

## Fitur
- **Beranda**: Menampilkan informasi umum dan berita terbaru.
- **Blog**: Menampilkan daftar artikel dengan gambar, judul, penulis dan ringkasan.
- **Detail Artikel**: Pengguna dapat mengklik artikel untuk membaca lebih lanjut.
- **Pencarian**: Fitur pencarian untuk menemukan artikel berdasarkan kata kunci.
- **Kategori Artikel**: Menampilkan kategori artikel yang tersedia.
- **Login**: Admin dapat login  untuk mengakses fitur
- **Dashboard**: Admin dapat mengakses dashboard untuk melihat artikel
- **Tambah Artikel**: Admin dapat menambahkan artikel baru
- **Edit Artikel**: Admin dapat mengedit artikel yang sudah ada
- **Hapus Artikel**: Admin dapat menghapus artikel yang sudah ada


## Teknologi yang Digunakan
- **Django**: Framework web untuk membangun aplikasi web.
- **Bootstrap**: Framework CSS untuk desain responsif.
- **MySQL**: Database untuk menyimpan data artikel dan pengguna.
- **HTML/CSS/JS**: Untuk struktur dan gaya halaman web.

## Instalasi

1. **Clone Repository**:
   ```bash
   git clone https://github.com/zaviraa/website_sawb_BE.git
   cd repo-name

2. **Buat Virtual Environment**:
    python -m venv venv
    source venv/bin/activate  # Untuk Linux/Mac
    venv\Scripts\activate  # Untuk Windows

3. **Instal Dependensi**:
    pip install -r requirements.txt

4. **Konfigurasi Database**:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nama_database',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5. **Buat dan Terapkan Migrasi**:
    python manage.py makemigrations
    python manage.py migrate

6. **Jalankan Server**:
    python manage.py runserver
