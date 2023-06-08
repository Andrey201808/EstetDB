from server import Server


class Output(Server):

    def handle(self, message):
        try:
            print("Получено сообщение : {}".format(message))
        except Exception as e:
            print("Ошибка: {}".format(e))


if __name__ == "__main__":
    print("Вывод сообщений начат.")

    app = Output("localhost", 8889)
    app.start_server()
    app.loop()
    app.stop_server()
