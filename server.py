import socket
print("СЕРВЕР: Запуск сервера...")
sock = socket.socket()
sock.bind(('', 9090))
print("СЕРВЕР: Сокет привязан к порту 9090.")
sock.listen(0)
print("СЕРВЕР: Начало прослушивания входящих подключений.")
shutdown_requested = False
while not shutdown_requested:
    conn, addr = sock.accept()
    print(f"СЕРВЕР: Подключился клиент с адресом {addr}.")
    msg = ''
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print("СЕРВЕР: Клиент прекратил отправку данных или отключился.")
                break
            decoded_data = data.decode().strip().lower()
            print(f"СЕРВЕР: Получена порция данных: {decoded_data}")
            if decoded_data == "shutdown":
                conn.send(b"Server shutting down...")
                shutdown_requested = True
                break
            msg += decoded_data
            conn.send(data)
        print(f"СЕРВЕР: Полное сообщение от клиента: {msg}")
    except ConnectionResetError:
        print(f"СЕРВЕР: Клиент {addr} отключился неожиданно.")
    finally:
        conn.close()
        print(f"СЕРВЕР: Соединение с {addr} закрыто.")

sock.close()
print("СЕРВЕР: Остановка сервера. Работа завершена.")