class NotForSending(Exception):
    """Не для пересылки в телеграм."""


class ProblemDescriptions(Exception):
    """Описания проблемы."""


class InvalidResponseCode(Exception):
    """Не верный код ответа."""


class ConnectionError(Exception):
    """Не верный код ответа."""


class EmptyResponseFromAPI(NotForSending):
    """Пустой ответ от API."""


class TelegramError(NotForSending):
    """Ошибка телеграма."""
