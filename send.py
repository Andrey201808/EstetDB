import json
import requests
from server import Server


class Sender1(Server):

    def handle(self, message):
        try:
            print("Отправлено сообщение {}".format(message))
            url = json.loads(str(message, 'ascii'))["url"]
            response = requests.get(url)
        except Exception as e:
            print("Ошибка: {}".format(e))
        else:
            result = {}
            result['status_code'] = response.status_code
            self.send('localhost', 8889, json.dumps(result))


if __name__ == "__main__":
    print("Отправка сообщений начата.")

    getter = Sender1('localhost', 8887)
    getter.start_server()
    getter.loop()
    getter.stop_server()
