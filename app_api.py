from flask import Flask, jsonify, request #Importa as classes necessárias do Flask para criar e executar a aplicação web.

app = Flask(__name__) # Cria uma instância do Flask chamada app.

#Lista filmes
filmes = [ #A lista filmes contém dicionários que representam informações sobre filmes, incluindo id, título e autor.
    {
        'id' : 1,
        'título': 'exemplo titulo 1',
        'autor': 'exemplo autor 1'
    },
    {
        'id' : 2,
        'título': 'exemplo titulo 2',
        'autor': 'exemplo autor 2'
    },
    {
        'id' : 3,
        'título': 'exemplo titulo 3',
        'autor': 'exemplo autor 3'
    },

]
#APIs - A aplicação define várias rotas para manipular os dados de filmes.

#consultar (todos)
@app.route('/filmes', methods=['GET'])#Esta rota permite consultar todos os filmes na lista filmes. Ela responde a requisições HTTP GET e retorna uma lista de todos os filmes em formato JSON.
def obter_filmes():
    return jsonify(filmes)

#consultar (id)
@app.route('/filmes/<int:id>', methods = ['GET']) # Esta rota permite consultar um filme específico com base em seu ID. Ela responde a requisições HTTP GET e retorna as informações do filme correspondente ao ID especificado.
def obter_filme_por_id(id):
    for filme in filmes:
        if filme.get ('id') == id:
             return jsonify(filme)

#editar
@app.route('/filmes/<int:id>', methods = ['PUT']) #  Esta rota permite editar um filme com base em seu ID. Ela responde a requisições HTTP PUT e atualiza as informações do filme correspondente ao ID especificado com os dados fornecidos no corpo da requisição
def editar_filme_por_id(id):
    filme_alterado = request.get_json()
    for indice,filme in enumerate(filmes):
        if filme.get('id') == id:
            filmes[indice].update(filme_alterado)
            return jsonify(filmes[indice])
        

#Criar
@app.route('/filmes', methods = ['POST']) #Esta rota permite criar um novo filme. Ela responde a requisições HTTP POST e adiciona um novo filme à lista filmes com base nos dados fornecidos no corpo da requisição.
def incluir_novo_filme():
    novo_filme = request.get_json()
    filmes.append(novo_filme)

    return jsonify(filmes)
  
        
#excluir
@app.route('/filmes/<int:id>', methods = ['DELETE']) #Esta rota permite excluir um filme com base em seu ID. Ela responde a requisições HTTP DELETE e remove o filme correspondente ao ID especificado da lista filmes.
def excluir_filme(id):
    for indice,filme in enumerate(filmes):
        if filme.get('id') ==id:
            del filmes[indice]

    return jsonify(filmes)


#Cada rota é associada a uma função que define o comportamento da rota. Por exemplo, a função obter_filmes 
# é chamada quando a rota /filmes é acessada com um método HTTP GET. Essas funções geralmente respondem às 
# requisições HTTP e manipulam os dados com base nas operações desejadas (consulta, edição, criação ou exclusão).



app.run(port=5000, host='localhost', debug=True) #Inicia a aplicação Flask na porta 5000 e no host 'localhost'. A opção debug=True ativa o modo de depuração, que é útil durante o desenvolvimento para detectar erros facilmente.