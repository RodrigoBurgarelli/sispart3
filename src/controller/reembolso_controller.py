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

@bp_reembolso.route('/todos-reembolsos', methods=['GET'])
def pegar_todos_reembolsos():

    reembolsos = db.session.execute(
        db.select(Reembolso)
    ).scalars().all()

#                       expressão                   item              iteravel  
    reembolsos = [reembolso.all_data() for reembolso in reembolsos]
    return jsonify(reembolsos), 200

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
    
    db.session.add(novo_reembolso)
    db.session.commit()
    
    colaborador = dados_requisicao.get('colaborador')
    empresa = dados_requisicao.get('empresa')
    senha = dados_requisicao.get('senha')
    data = dados_requisicao.get('data')
    tipo_reembolso = dados_requisicao.get('tipo_reembolso')
    centro_custo = dados_requisicao.get('centro_custo')
    moeda = dados_requisicao.get('moeda')
    valor_faturado = dados_requisicao.get('valor_faturado')

    if not colaborador or not empresa or not senha or not data or not tipo_reembolso or not centro_custo or not moeda or not valor_faturado:
        return jsonify ({'mensagem': 'Os campos necessarios nao foram todos preenchidos'}), 400
    
    return jsonify( {'mensagem': 'Reembolso cadastrado com sucesso'} ), 201
