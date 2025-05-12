from os import environ # essa linha vai trazer para o arquivo o acesso as variáveis de ambiente
from dotenv import load_dotenv # essa linha traz a função para carregar as variáveis de ambiente nesse arquivo

load_dotenv() # Carrega as variáveis de ambiente para este arquivo

class Config():
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_PROD') # Puxa a variável e utiliza para a conexão
    SQLALCHEMY_TRACK_MODIFICATION = False #Otimiza as querys no banco de dados
    