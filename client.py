import socket  # Импортируем модуль socket для работы с сетевыми соединениями

# from time import sleep  # Импорт функции sleep (не используется в данном примере)

# -----------------------------------------------------------------------------
# 1. Создание TCP-сокета
# -----------------------------------------------------------------------------
# Создаём новый сокет, который по умолчанию работает по протоколу IPv4 (AF_INET) и
# использует протокол TCP (SOCK_STREAM). TCP обеспечивает надежную доставку данных.
sock = socket.socket()

# -----------------------------------------------------------------------------
# 2. Настройка режима работы сокета
# -----------------------------------------------------------------------------
# Устанавливаем сокет в блокирующий режим (значение 1). По умолчанию сокеты уже работают
# в блокирующем режиме, поэтому эта строка является избыточной, но полезна для наглядности.
sock.setblocking(1)

# -----------------------------------------------------------------------------
# 3. Установление соединения с сервером
# -----------------------------------------------------------------------------
# Метод connect() инициирует подключение к серверу. Здесь мы подключаемся к серверу,
# запущенному на локальном компьютере (localhost) и слушающему порт 9090.
sock.connect(('localhost', 9090))

# -----------------------------------------------------------------------------
# 4. Считывание строки со стандартного ввода
# -----------------------------------------------------------------------------
# Функция input() выводит сообщение в консоль и ожидает, пока пользователь введёт строку.
# Введённая строка сохраняется в переменной msg.
msg = input("Введите строку для отправки серверу: ")

# -----------------------------------------------------------------------------
# 5. Отправка данных на сервер
# -----------------------------------------------------------------------------
# Перед отправкой строку необходимо преобразовать в байты, поскольку метод send() принимает
# данные именно в байтовом виде. Для этого используется метод encode().
sock.send(msg.encode())

# -----------------------------------------------------------------------------
# 6. Получение ответа от сервера
# -----------------------------------------------------------------------------
# Метод recv() ожидает получения данных от сервера. Здесь мы запрашиваем до 1024 байт данных.
# Предполагается, что сервер возвращает ту же строку (эмуляция эхо-сервера).
data = sock.recv(1024)

# -----------------------------------------------------------------------------
# 7. Завершение работы с сокетом
# -----------------------------------------------------------------------------
# После завершения обмена данными закрываем сокет, чтобы освободить ресурсы.
sock.close()

# -----------------------------------------------------------------------------
# 8. Вывод полученного ответа
# -----------------------------------------------------------------------------
# Декодируем полученные байты обратно в строку (с помощью метода decode()) и выводим на экран.
print("Ответ от сервера:", data.decode())