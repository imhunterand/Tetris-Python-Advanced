# Tetris-Python-Advanced

Tetris-Python-Advanced adalah proyek game Tetris yang dikembangkan menggunakan Python dan Pygame. Game ini dilengkapi dengan berbagai fitur menarik dan tambahan untuk memberikan pengalaman bermain yang lebih baik dan menyenangkan. Proyek ini cocok untuk pemula yang ingin belajar tentang pengembangan game dengan Python serta bagi mereka yang ingin mengembangkan game Tetris lebih lanjut.

## Fitur Utama

1. **Layar Splash/Intro**: Menampilkan layar pembuka sebelum masuk ke menu utama.
2. **Menu Utama**: Terdiri dari opsi untuk memulai permainan dan keluar.
3. **Level dan Kesulitan**: Sistem level yang meningkat seiring bertambahnya garis yang dihapus.
4. **Sistem Poin dan High Score**: Menyimpan dan menampilkan skor tertinggi pemain.
5. **Pause dan Resume**: Kemampuan untuk menghentikan sementara dan melanjutkan permainan.
6. **Power-ups**: Fitur tambahan untuk memberikan variasi dalam permainan.
7. **Efek Suara dan Musik Latar**: Menambahkan suasana permainan dengan efek suara dan musik latar.
8. **Animasi Penghapusan Garis**: Animasi menarik saat garis dihapus.
9. **Tampilan Next Tetromino**: Menampilkan tetromino berikutnya yang akan muncul.
10. **Sistem Penyimpanan dan Pemulihan Permainan**: Menyimpan status permainan dan melanjutkan dari titik terakhir.
11. **Kontrol yang Dapat Disesuaikan**: Pemain dapat mengatur kontrol sesuai keinginan.
12. **Tampilan Multiplayer (Lokal)**: Opsi untuk bermain bersama teman di satu perangkat.
13. **Panduan dan Tutorial Permainan**: Panduan dan tutorial bagi pemain baru.

## Instalasi

1. Clone repository ini:
    ```bash
    git clone https://github.com/username/Tetris-Python-Advanced.git
    cd Tetris-Python-Advanced
    ```

2. Install Pygame:
    ```bash
    pip install pygame
    ```

3. Pastikan semua file suara dan gambar ada di folder yang sesuai.

## Menjalankan Game

Jalankan game dengan perintah berikut di terminal:
```bash
python main.py
```

## Struktur Proyek
```
Tetris-Python-Advanced/
│
├── sounds/
│   ├── rotate.wav
│   ├── move.wav
│   ├── line_clear.wav
│   ├── game_over.wav
│   └── background_music.mp3
│
├── settings.py
├── tetris.py
├── main.py
├── menu.py
├── sound.py
└── score.py
```
## Kontrol Permainan
 * **Panah** Kiri: Menggerakkan tetromino ke kiri
 * **Panah** Kanan: Menggerakkan tetromino ke kanan
 * **Panah** Atas: Memutar tetromino
 * **Panah** Bawah: Mempercepat jatuhnya tetromino
 * **P:** Pause dan Resume permainan


## Kontribusi
Kontribusi sangat diterima! Anda dapat melakukan fork repository ini dan mengirim pull request dengan perubahan atau fitur tambahan yang Anda tambahkan.

