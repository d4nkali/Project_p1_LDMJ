# Importa as bibliotecas
import os
import csv
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Definindo a variável de ambiente
os.environ['FLASK_DEBUG'] = 'True'

# Configurando o modo de depuração com base na variável de ambiente
app.debug = os.environ.get('FLASK_DEBUG') == 'True'

# Definindo as rotas das paginas
@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/index_sobre.html')
def sobre():
    return render_template('index_sobre.html')

@app.route('/index_produtos.html')
def produtos():
    return render_template('index_produtos.html')

@app.route('/index_contato.html')
def contato():
    return render_template('index_contato.html')

@app.route('/index_avaliacoes.html')
def avaliacoes():
    return render_template('index_avaliacoes.html')

@app.route('/index_portifolios.html')
def portifolios():
    return render_template('index_portifolios.html')


@app.route('/glossario')
def glossario():

    glossario_de_notas = []

    with open(
            'avaliacoes.csv',
            newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for l in reader:
            glossario_de_notas.append(l)

    return render_template('glossario.html',
                           glossario=glossario_de_notas)


@app.route('/novo_nota')
def novo_nota():
    return render_template('adicionar_nota.html')


@app.route('/criar_nota', methods=['POST', ])
def criar_nota():
    nota = request.form['nota']
    definicao = request.form['definicao']

    with open(
            'avaliacoes.csv', 'a',
            newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([nota, definicao])

    return redirect(url_for('glossario'))


@app.route('/excluir_nota/<int:nota_id>', methods=['POST'])
def excluir_nota(nota_id):

    with open('avaliacoes.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        linhas = list(reader)

    # Encontrar e excluir o nota com base no ID
    for i, linha in enumerate(linhas):
        if i == nota_id:
            del linhas[i]
            break

    # Salvar as alterações de volta no arquivo
    with open('avaliacoes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(linhas)

    return redirect(url_for('glossario'))

# @app.route('/pesquisar_nota/<int:nota_id>')
# def pesquisar_nota(nota_id):
#
#     with open('avaliacoes.csv', 'r', newline='') as file:
#         reader = csv.reader(file)
#         linhas = list(reader)
#
#     # Encontrar e excluir o nota com base no ID
#     for i, linha in enumerate(linhas):
#         if i == nota_id:
#             del linhas[i]
#             break



if __name__ == "__main__":
    app.run()
