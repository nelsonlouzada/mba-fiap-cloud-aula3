import os

# function_app.py lê STORAGE_ACCOUNT_CATALOGO no nível do módulo (import time).
# Para testes que não dependem de acesso real ao Blob (ex.: health), definimos
# um valor fake aqui, carregado pelo pytest antes da coleta dos testes.
os.environ.setdefault("STORAGE_ACCOUNT_CATALOGO", "fake-storage-for-tests")
