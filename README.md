# Algeo02-21043
Tubes 2 Algeo 22/23

# Pembagian Tugas
1. Nigel Sahl (13521043)                : Fungsi mean, fungsi selisih, fungsi identifikasi wajah dengan dataset, dan program utama dalam GUI, menambah file-file dalam dataset menjadi list  
2. Muhammad Naufal Nalendra (13521152)  : Fungsi Resize image, konversi RGB menjadi Greyscale, dan penyusunan flatvector matriks citra, fungsi crop wajah, dan change background
3. Hanif Muhammad Zhafran (13521157)    : Fungsi Eigenvalue, fungsi Eigenvector, dan fungsi Eigenface, mengoptimalisasi deteksi wajah  

# Cara menjalankan program 
1. Buka terminal pada direktori folder src yang berisi main.py 
2. Jalankan program dengan command "py -3.7 -m  main.py" (program ini meggunakan versi python 3.7 untuk menjalankannya, kecuali jika terdapat library mediapipe pada python versi yang lebih tinggi)
3. Terdapat beberapa opsi-opsi yang dapat dilakukan untuk deteksi wajah yaitu :
    a. Jika pengguna hanya ingin mendeteksi wajah satu kali dengan dataset yang siberikan maka, pengguna dapat memasukkan dataset dan test image yang ingin dideteksi wajahnya. Kemudian menekan tombol execute untuk memulai pendeteksian. Hasil gambar akan keluar pada bagian result image dan nama hasil wajah akan tampil pada bagian result di pojok kiri bawah. 

    b. Jika pengguna ingin melakukan tes uji untuk banyak test image dengan dataset yang sama. Memasukkan dataset terlebih dahulu kemudian menekan train image agar hasil pre-processing dari dataset dapat tersimpan selama tidak ada dataset baru yang ingin diuji. Setelah itu pengguna dapat memasukkan test image - tes image yang ingin diuji lalu menekan execute. Program akan dengan cepat melakukan identifikasi dan menampilkan hasilnya. 

    c. Jika pengguna ingin langsung menggunakan kamera untuk pendeteksian wajah, maka pengguna dapat menggunakan fitur tambahan yaitu terdapat tombol camera untuk memasukkan test image secara real time dengan kamera laptop atau komputer pengguna. Untuk selebihnya seperti train dataset terlebih dahulu atau tidak tetap bisa dilakukan seperti pada poin a dan b hanya berbeda di bagian input gambar yang digantikan dengan penangkapan gambar secara langsung dengan kamera. Ketika tombol kamera ditekan, tombol input test image berupa file akan langsung dimatikan (tidak bisa ditekan)  selama kamera menyala. 