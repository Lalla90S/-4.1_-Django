# logging_config.py
# Конфигурация логирования для Django

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose_console': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'verbose_console_warning': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s'
        },
        'verbose_console_error': {
            'format': '%(asctime)s %(levelname)s %(pathname)s %(message)s\n%(exc_info)s'
        },
        'general_formatter': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'error_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s\n%(exc_info)s'
        },
        'security_formatter': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        'mail_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose_console'
        },
        'console_warning': {
            'level': 'WARNING', 
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose_console_warning'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose_console_error'
        },
        'general_file': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'general_formatter',
        },
        'errors_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler', 
            'filename': 'errors.log',
            'formatter': 'error_formatter',
        },
        'security_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'security_formatter',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mail_formatter',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'general_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR', 
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
