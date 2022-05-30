from flask import Flask, render_template, request, redirect, session, flash



class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console


jogo1=Jogo('Tetris', 'Puzze', 'Atari')
jogo2=Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3=Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]


app = Flask(__name__)  #este name faz referencia ao próprio arquivo
app.secret_key = 'alura'#senha necessária para evitar que alguém má intencionado acesse dados do cookie, usado pela função session, que retém a informação de que o usuário está logado

@app.route('/') #para toda rota devemos criar uma função
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])#o método get é padrão
def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']
    jogo=Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)
    



@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '123' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']#o session usa cookie (até 4kB disponível) para informar que está logado.
        flash('Seja bem vindo(a) ' + session['usuario_logado'] + '. Você efetuou login com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário não logado.')#exibe uma mensagem rápida no html. Olhe no arquivo de login e template que tem um código jinja usado para exibir esta mensagem no html
        return redirect('/login')#note que o redirect serve para 

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')



# trecho da app para mudar a porta
#app.run(host='0.0.0.0', port=8080)
app.run(debug=True)