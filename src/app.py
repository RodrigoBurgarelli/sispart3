#RESPONSÁVEL PELA CRIAÇÃO DA APLICAÇÃO
# CREATE_APP() -> QUE VAI CONFIGURAR A INSTÂNCIA DO FLASK
from flask import Flask
from src.controller.colaborador_controller import bp_colaborador
from src.controller.reembolso_controller import bp_reembolso
from src.model import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec", # <-- Da um nome de referencia para a documentacao
            "route": "/apispec.json/", # <-- Define a rota do arquivo JSON para a construção da documentação
            "rule_filter": lambda rule: True, # <-- Indica que todas as rotas/endpoints serão documentadas
            "model_filter": lambda tag: True, # <-- Vai especificar quais modelos da entidade serão documentados
        }
    ],
    "static_url_path": "/flasgger_static", # estamos pegando a estilização padrão da biblioteca flagger
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

def create_app():
    app = Flask(__name__) # <-- instância do Flask
    CORS(app, origins="*") # <--- A política de CORS seja implementada em TODA A APLICAÇÃO
    app.register_blueprint(bp_colaborador)
    app.register_blueprint(bp_reembolso)
    
    app.config.from_object(Config) #nessa linha trouxemos a configuração do abiente de desenvolvimento
    db.init_app(app) # inicia-se a conexão com o banco de dados
    
    Swagger(app, config=swagger_config)
    
    with app.app_context():
        db.create_all() # cria as tabelas caso elas não existam
        
    return app