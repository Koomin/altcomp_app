from .base import *

DATABASES = {
    'default': {
        'ENGINE': get_env_variable('DB_ENGINE'),
        'NAME': get_env_variable('DB_NAME'),
        'HOST': get_env_variable('DB_HOST'),
        'USER': get_env_variable('DB_USER'),
        'PASSWORD': get_env_variable('DB_PASSWORD'),
        'PORT': get_env_variable('DB_PORT')
    }
}
CRONJOBS = [
    ('*/5 * * * *', 'altcomp_app.devices.crontab.update_devices'),
]
