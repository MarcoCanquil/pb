from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com']

# Base de datos para producción
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_base_datos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',  # O dirección del servidor de base de datos
        'PORT': '5432',
    }
}

# Configuración para servir archivos estáticos en producción
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

# Configuración adicional para seguridad
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
