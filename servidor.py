from flask import Flask, request, render_template, redirect, url_for, session

import dao

app = Flask(__name__)
app.secret_key = 'gw4ab##@'

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return  render_template('cadastro.html')
    elif request.method == 'POST':

        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        senha = request.form.get('senha')
        dao.inserir_user(nome, telefone, email, senha)
        session['longin'] = email
        msg= 'Usuário inserido com sucesso!'

        return render_template('login.html' ,texto=msg)
    else:
        tex = 'Erro ao inserir usuário.'
        return render_template('cadastro.html', texto=tex)

@app.route('/home')
def index():
     return render_template('principal.html')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST','GET'])
def ir_principal():
    email_user = request.form.get('email')
    senha_user = request.form.get('senha')
    saida = dao.login(email_user, senha_user)

    if len(saida) > 0:
        session['login'] = email_user
        nome_user = saida[0][0]
        return render_template('principal.html', nome=nome_user)
    else:
        texto = 'O login que você fez não existe, tente novamente!'
        return render_template('login.html', texto = texto )

@app.route('/principal', methods= ['GET', 'POST'])
def doar():
    return render_template('Croupas.html')

@app.route('/pagcadastroroupas')
def mostrar_pag_cadatro_roupas():

    if 'login' in session:
        roupas = dao.inserir_roupa('tipo', 'tamanho', 'estado', 'descricao', 'email')
        return render_template('Croupas.html', lista=roupas)
    else:
        return render_template('login.html')


@app.route('/Croupas', methods=['POST', 'GET'])
def doar_roupas():
    tipo = request.form.get('tipo')
    tamanho = request.form.get('tamanho')
    estado = request.form.get('estado')
    descricao = request.form.get('descricao')
    email = request.form.get('email')
    dao.inserir_roupa(tipo, tamanho, estado, descricao, email)
    return render_template('Croupas.html')

@app.route('/listar_roupas', methods=['GET','POST'])
def listar_roupas():
    roupas = dao.listar_roupas()
    print(roupas)
    return render_template('QueroReceber.html', lista=roupas)

@app.route('/logout', methods=['GET'])
def sair():
    return render_template('login.html')

@app.route('/voltar', methods=['GET'])
def volta():
    return render_template('principal.html')

if __name__ == '__main__':
    app.run(debug=True)