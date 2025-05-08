
from flask import Blueprint, request, jsonify
from src.model.colaborador_model import Colaborador
from src.model import db
from src.security.security import hash_senha, checar_senha
from flasgger import swag_from

#request -> vai trabalhar com todo o corpo da função. TRABALHA COM AS REQUISIÇÕES. pEGA O CONTEÚDO DA REQUISIÇÃO
#jsonify -> TRABALHA COM AS RESPOSTAS. CONVERTE UM DADO EM Json.

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')


@bp_colaborador.route('/pegar-dados', methods=['GET'])
def pegar_dados():

    return jsonify(dados), 200

@bp_colaborador.route('/cadastrar', methods=['POST'])
@swag_from('../docs/colaborador/cadastrar_colaborador.yml')
def cadastrar_novo_colaborador():
    
    dados_requisicao = request.get_json()
    
    novo_colaborador = Colaborador(
        nome=dados_requisicao['nome'],
        email=dados_requisicao['email'],
        senha=hash_senha(dados_requisicao['senha']),
        cargo=dados_requisicao['cargo'],
        salario=dados_requisicao['salario']
    )
    
    db.session.add(novo_colaborador) # é como se no banco de dados tivesse sido colocado INSERT INTO tb_colaborador (nome, email, senha, cargo, salario) VALUES ('samuel', 'samueltigrao@gmail.com', '1234', 'clientes', 120)
    db.session.commit() # CLique no raio do workbench
    
    return jsonify( {'mensagem': 'Dado cadastrado com sucesso'} ), 201

# Endereco/colaborador/atualizar/2
@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
def atualizar_dados_do_colaborador(id_colaborador):
    dados_requisicao = request.get_json()
    
    for colaborador in dados:
        if colaborador['id'] == id_colaborador:
            colaborador_encontrado = colaborador
            break
    
    if 'nome' in dados_requisicao:
        colaborador_encontrado['nome'] = dados_requisicao['nome']
    if 'cargo' in dados_requisicao['cargo']:
        colaborador_encontrado['cargo'] = dados_requisicao['cargo']
    
    return jsonify( {'mensagem': 'Dados de colabora atualizado com sucesso'}), 200

@bp_colaborador.route('/login', methods=['POST'])
def login():
    dados_requisicao = request.get_json()
    email = dados_requisicao.get('email')
    senha = dados_requisicao.get('senha')
    
    if not email or not senha:
        return jsonify({'mensagem': 'Todos os campos devem ser preenchidos'}), 400
                                    #Query para o banco de dados
    colaborador = db.session.execute(db.select(Colaborador).where(Colaborador.email == dados_requisicao['email'])).scalar() # Pedir para retornar um único resultado ou None se não tiver nada
    
    
    
    if not colaborador:
        return jsonify({'mensagem': 'O usuário não foi encontrado'}), 404
    
    colaborador = colaborador.to_dict()
       

    if colaborador.get('email') == email and checar_senha(senha, colaborador.get('senha')):
        return jsonify({'mensagem': 'Login realizado com sucesso'}), 200
    
    