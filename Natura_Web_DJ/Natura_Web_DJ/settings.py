import os

from decouple import config


ENVIRONMENT = os.getenv('DJANGO_ENV', 'local')

if ENVIRONMENT == 'production':
    from .prod import *
else:
    from .local import *

