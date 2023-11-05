import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# параметры для инициализации сервера
hostName = 'localhost'
serverPort = 8080


class Myserver(BaseHTTPRequestHandler):
    """
    Класс для обработки запросов с сайта
    """

    def __get_html_content__(self):
        """
        Метод для считывания данных из HTML-файла
        :return: строки из HTML-файла
        """
        with open("index.html", "r", encoding="utf-8") as f:
            page_content = f.read()
        return page_content

    def do_GET(self):
        """
        Метод для обработки GET-запросов с сайта
        """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content__()
        self.send_response(200)
        # тип данных, который будет передаваться в ответе
        self.send_header('Content-type', 'text/html')
        # завершение формирования заголовка ответа
        self.end_headers()
        # тело ответа
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера по заданным параметрам для работы класса Myserver
    webServer = HTTPServer((hostName, serverPort), Myserver)
    print('Server started http://%s:%s' % (hostName, serverPort))

    # запуск сервера в бесконечном цикле прослушивания входящих запросов
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    # остановка сервера
    webServer.server_close()
    print("Server stopped.")
