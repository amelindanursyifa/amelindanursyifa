import socket
import os

def tcp_server():
    # Mengatur alamat IP dan port untuk server
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 8080

    # Membuat socket TCP
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Mengaitkan socket dengan alamat IP dan port
    sock_server.bind((SERVER_HOST, SERVER_PORT))

    # Mendengarkan koneksi masuk dari klien
    sock_server.listen()

    print("Server is Ready")

    while True:
        # Menerima koneksi dari klien
        sock_client, client_address = sock_server.accept()

        # Menerima permintaan dari klien
        request = sock_client.recv(1024).decode()
        print("From client: " + request)

        # Memproses permintaan
        response = handle_request(request)

        # Mengirimkan respons ke klien
        sock_client.send(response.encode())

        # Menutup koneksi dengan klien
        sock_client.close()
    

def handle_request(request):
    # Memecah permintaan HTTP menjadi baris-baris terpisah
    request_lines = request.split("\r\n")

    # Mendapatkan jalur dari permintaan GET
    path = request_lines[0].split(" ")[1]

    # Menentukan file yang diminta oleh klien
    file_path = os.path.join(os.getcwd(), "TubesJarkom", path.lstrip("/"))

    # Membuka file yang diminta oleh klien
    try:
        with open(file_path, "rb") as file:
            # Membaca isi file
            file_content = file.read()
            # Membuat respons HTTP dengan status 200 OK dan isi file yang diminta
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type: text/html\r\n\r\n"
            response = response.encode() + file_content
    except FileNotFoundError:
        # Jika file tidak ditemukan, membuat respons HTTP dengan status 404 Not Found
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type: text/html\r\n\r\n"
        response += "<h1>404 Not Found</h1>".encode()

    return response

if __name__ == "__main__":
    tcp_server()
