from flask import Flask, render_template, request, redirect

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

@app.route('/') #para toda rota devemos criar uma função
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']
    jogo=Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

# trecho da app para mudar a porta
#app.run(host='0.0.0.0', port=8080)
app.run(debug=True)