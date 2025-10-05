Консоль (DEBUG=True):

DEBUG+ сообщения: время + уровень + сообщение

WARNING+ сообщения: + путь к источнику

ERROR+ сообщения: + стек ошибки

Все из логгера django

general.log (DEBUG=False):

INFO+ сообщения

Формат: время + уровень + модуль + сообщение

Из логгера django

errors.log:

ERROR+ сообщения

Формат: время + уровень + сообщение + путь + стек ошибки

Только из: django.request, django.server, django.template, django.db.backends

security.log:

Сообщения безопасности

Формат: время + уровень + модуль + сообщение

Только из django.security

Почта (DEBUG=False):

ERROR+ сообщения

Формат как errors.log но без стека

Только из django.request и django.server

Фильтры:

Консоль → только при DEBUG=True

general.log и почта → только при DEBUG=False

