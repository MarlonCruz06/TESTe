# Conteúdo do arquivo /igreja_gestor/igreja_gestor/settings.py

import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Configurações de segurança
# IMPORTANTE: A SECRET_KEY não deve ser mantida em texto plano no código.
# Em produção, carregue-a de uma variável de ambiente ou de um cofre de segredos.
SECRET_KEY = 'sua-chave-secreta-aqui'
DEBUG = True

ALLOWED_HOSTS = []

# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usuarios',
    'membros',
    'igrejas',
    'eventos',
    'financeiro',
    'inscricoes',
    'dashboard',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configurações de URL
ROOT_URLCONF = 'igreja_gestor.urls'

# Configurações de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configurações de WSGI
WSGI_APPLICATION = 'igreja_gestor.wsgi.application'

# Configurações de banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'usuarios.Usuario'

# Configurações de autenticação
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurações de idioma
LANGUAGE_CODE = 'pt-br'

# Configurações de fuso horário
TIME_ZONE = 'America/Sao_Paulo'

# Configurações de internacionalização
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configurações de arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Configurações de arquivos de mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')