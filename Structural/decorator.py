from abc import ABC, abstractmethod


# Simple components
class Notifier(ABC):
    @abstractmethod
    def send(self, message) -> str: pass


class EmailNotifier(Notifier):
    def send(self, message) -> str:
        return f'\nMessage:\n"{message}"\nwas sent by E-mail'


# Decorators
class BaseDecorator(Notifier):
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    @property
    def notifier(self) -> Notifier:
        return self._notifier

    def send(self, message: str) -> str:
        return self.notifier.send(message)


class TelegramDecorator(BaseDecorator):
    def send(self, message) -> str:
        return f'{self.notifier.send(message)} + Telegram'


class SlackDecorator(BaseDecorator):
    def send(self, message) -> str:
        return f'{self.notifier.send(message)} + Slack'


class SMSDecorator(BaseDecorator):
    def send(self, message) -> str:
        return f'{self.notifier.send(message)} + SMS'


# Client code
if __name__ == '__main__':
    email = EmailNotifier()
    email_plus_telegram = TelegramDecorator(email)
    email_plus_telegram_plus_sms = SMSDecorator(email_plus_telegram)
    email_plus_telegram_plus_sms_slack = SlackDecorator(SMSDecorator(email_plus_telegram))

    notifiersList = [email,
                     email_plus_telegram,
                     email_plus_telegram_plus_sms,
                     email_plus_telegram_plus_sms_slack, ]

    def client_code(notifiers: list):
        for notifier_combination in notifiers:
            yield notifier_combination.send('Notification')

        print(SMSDecorator(TelegramDecorator(SlackDecorator(EmailNotifier()))).send('Another decorator order'))

    for notify in client_code(notifiersList): print(notify)
