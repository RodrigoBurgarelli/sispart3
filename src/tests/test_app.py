# para que a biblioteca encontre o arquivo de teste, o nome desse arquivo deve começar com test

import pytest # traz a biblioteca de testes
import time # manipular o tempo
from src.model.colaborador_model import Colaborador
from src.app import create_app

#------------------------CONFIGURAÇÕES DOS TESTES------------

@pytest.fixture
def app():
    app = create_app()
    yield app   # yield vai guardar os valores em memória
    
@pytest.fixture
def client(app):
    return app.test_client()

#-------------------------------------------------

def test_desempenho_requisicao_get(client):
    
    comeco = time.time() # vai pegar a hora atual e transformar em segundos
    
    for _ in range(100):
        resposta = client.get('/colaborador/todos-colaboradores')
    
    fim = time.time() - comeco
    assert fim < 1.0