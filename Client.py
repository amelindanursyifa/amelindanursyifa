# Mengimport modul socket
from socket import *

# Menentukan port server dan alamat server
ServerPort = 8080
ServerName = '127.0.0.1'

# Membuat objek socket client
ClientSocket = socket(AF_INET, SOCK_STREAM)

# Menghubungi server dengan alamat dan port yang ditentukan
try:
    ClientSocket.connect((ServerName, ServerPort))

# Untuk menangkap dan menangani exception yang mungkin terjadi ketika client gagal melakukan koneksi ke server karena server tidak tersedia atau tidak dapat diakses
except ConnectionRefusedError:
    print("Error: Connection refused")

# Menerima input dari pengguna
Sentence = input('Input : ')

# Mengirim data ke server
ClientSocket.send(Sentence.encode())

# Menerima balasan dari server dengan buffer size 1024 byte
ModifiedSentence = ClientSocket.recv(1024)

# Menampilkan pesan dari server
print('From Server : ', ModifiedSentence.decode())

# Menutup koneksi dengan server
ClientSocket.close()
