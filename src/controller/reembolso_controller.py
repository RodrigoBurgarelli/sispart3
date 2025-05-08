# Tarefa -->

# 2 rotas:
#visualização de TODOS OS REEMBOLSOS -> metodo GET
# solicitacao de reembolso -> metodo POST
#id_colaborador = padrao 298


from flask import Blueprint, request, jsonify
from src.model.reembolso_model import Reembolso
from src.model import db
from flasgger import swag_from

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/reembolso')

@bp_reembolso.route('/pegar-dados', methods=['GET'])
def pegar_dados():

    return jsonify(dados), 200

@bp_reembolso.route('/cadastrar', methods=['POST'])
@swag_from('../docs/reembolso/cadastrar_reembolso.yml')
def cadastrar_novo_reembolso():
    
    dados_requisicao = request.get_json()
    
    novo_reembolso = Reembolso(
        colaborador = dados_requisicao['colaborador'],
        empresa = dados_requisicao['empresa'],
        num_prestacao = dados_requisicao['num_prestacao'],
        descricao = dados_requisicao['descricao'],
        data = dados_requisicao['data'],
        tipo_reembolso = dados_requisicao['tipo_reembolso'],
        centro_custo = dados_requisicao['centro_custo'],
        ordem_interna = dados_requisicao['ordem_interna'],
        divisao = dados_requisicao['divisao'],
        pep = dados_requisicao['pep'],
        moeda = dados_requisicao['moeda'],
        distancia_km = dados_requisicao['distancia_km'],
        valor_km = dados_requisicao['valor_km'],
        valor_faturado = dados_requisicao['valor_faturado'],
        despesa = dados_requisicao['despesa']
        
    )
    
    db.session.add(novo_reembolso) # é como se no banco de dados tivesse sido colocado INSERT INTO tb_colaborador (nome, email, senha, cargo, salario) VALUES ('samuel', 'samueltigrao@gmail.com', '1234', 'clientes', 120)
    db.session.commit() # CLique no raio do workbench
    
    return jsonify( {'mensagem': 'Reembolso cadastrado com sucesso'} ), 201

