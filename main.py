class Notification:
    sent_messages = []  # общая история всех уведомлений

    def __init__(self, title, message):
        self.title = title
        self.message = message

    def send_message(self):
        print(f'Title: {self.title}, Message: {self.message}')
        Notification.sent_messages.append(f'{self.title}: {self.message}')


class EmailNotification(Notification):
    def send_message(self):
        print(f'EMAIL -> Title: {self.title}, Message: {self.message}')
        Notification.sent_messages.append(f'EMAIL -> {self.title}: {self.message}')


class SMSNotification(Notification):
    def send_message(self):
        print(f'SMS -> Title: {self.title}, Message: {self.message}')
        Notification.sent_messages.append(f'SMS -> {self.title}: {self.message}')


class PushNotification(Notification):
    def send_message(self):
        print(f'PUSH -> Title: {self.title}, Message: {self.message}')
        Notification.sent_messages.append(f'PUSH -> {self.title}: {self.message}')


# Создание объектов
message0 = Notification('Общее', 'Это просто уведомление')
message1 = PushNotification('Avito', 'Акция 50% на товары')
message2 = SMSNotification('Samsung', 'SMS отправлено')
message3 = EmailNotification('GMail', 'Ваш резюме рассмотрено, Вы приняты!')

# Отправка уведомлений
message0.send_message()
message1.send_message()
message2.send_message()
message3.send_message()

# Проверка истории отправленных сообщений
print("\nИстория отправки:")
print(Notification.sent_messages)
