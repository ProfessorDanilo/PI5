from pickle import FALSE
from flask import Flask, render_template, request, url_for, flash, redirect
import os, datetime
import sqlite3
from time import sleep
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort



def salvando(nome, pontuacao):
    if nome == '':
        return None
    connection = sqlite3.connect('meusTestesDanilo.db')

    with open('meusTestesDanilo.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO ranking ('apelido', 'pontuacao') VALUES ('{}', {});".format(nome, pontuacao))

    connection.commit()
    connection.close()


def ranking():    
    connection = sqlite3.connect('meusTestesDanilo.db')
    with open('meusTestesDanilo.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    cur.execute("SELECT * FROM ranking ORDER BY pontuacao DESC;")
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows



pontos=0
apelido=''

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "meusTestesDanilo.db"))

app = Flask('__name__')  
app.config['SECRET_KEY'] = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)





@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/index.html')
def index2():
    global pontos
    pontos = 0
    return index()

@app.route('/post.html')
def postpage():
    posts = Posts.query.all()
    return render_template('post.html', posts=posts)

@app.route('/about.html')
def about():
    return render_template('about.html')
    
@app.route('/jogos.html')
def jogos():
    return render_template('jogos.html')

def get_post(post_id):
   post = Posts.query.filter_by(id=post_id).first()
   if post is None:
      abort(404)
   return post

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)



##################################
#apresentação do jogo #
@app.route('/Apresentacao', methods=('GET', 'POST'))
def apresentacao():
    global apelido
    if request.method == 'POST':
        apelido = request.form['nick']
        return redirect(url_for('aula1'))
    return render_template('Apresentacao.html')



##################################
#adicionando rotas para as aulas #
@app.route('/aula1', methods=('GET', 'POST'))#cachorros têm asas.
def aula1():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos = 0
            return render_template('errado.html')

        elif title == "F":
            pontos=10
            return render_template('correto.html')

        elif title == "proximo":
            return redirect(url_for('aula2'))
    return render_template('aula1.html', pontuacao=pontos)


@app.route('/aula2', methods=('GET', 'POST'))#Cachorros têm pelos.
def aula2():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "F":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula3'))
    return render_template('aula2.html', pontuacao=pontos)



@app.route('/aula3', methods=('GET', 'POST'))#Peixes vivem na água.
def aula3():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "F":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula4'))
    return render_template('aula3.html', pontuacao=pontos)

@app.route('/aula4', methods=('GET', 'POST'))#Árvores correm.
def aula4():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula5'))
    return render_template('aula4.html', pontuacao=pontos)


@app.route('/aula5', methods=('GET', 'POST'))#Borboletas comem peixes.
def aula5():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula6'))
    return render_template('aula5.html', pontuacao=pontos)

#NÍVEL 2
@app.route('/aula6', methods=('GET', 'POST'))#Cachorros não tem asas.
def aula6():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "F":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula7'))
    return render_template('aula6.html', pontuacao=pontos)


@app.route('/aula7', methods=('GET', 'POST'))#Cachorros não tem penas.
def aula7():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula8'))
    return render_template('aula7.html', pontuacao=pontos)


@app.route('/aula8', methods=('GET', 'POST'))#Peixes não vivem na água.
def aula8():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula9'))
    return render_template('aula8.html', pontuacao=pontos)



@app.route('/aula9', methods=('GET', 'POST'))#Borboletas não voam.
def aula9():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula10'))
    return render_template('aula9.html', pontuacao=pontos)



@app.route('/aula10', methods=('GET', 'POST'))#Borboletas não comem peixes.
def aula10():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "F":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula11'))
    return render_template('aula10.html', pontuacao=pontos)



@app.route('/aula11', methods=('GET', 'POST'))#Peixes vivem na água E dinossauros foram extintos.
def aula11():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "F":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula12'))
    return render_template('aula11.html', pontuacao=pontos)
    


@app.route('/aula12', methods=('GET', 'POST'))#Cachorros não tem pernas E borboletas voam.
def aula12():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula13'))
    return render_template('aula12.html', pontuacao=pontos)
    


@app.route('/aula13', methods=('GET', 'POST'))#Dinossauros foram extintos E cachorros tem asas.
def aula13():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula14'))
    return render_template('aula13.html', pontuacao=pontos)
    


@app.route('/aula14', methods=('GET', 'POST'))#Cachorros não tem pernas E árvores não correm.
def aula14():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula15'))
    return render_template('aula14.html', pontuacao=pontos)
    


@app.route('/aula15', methods=('GET', 'POST'))#Cachorros não tem pernas E árvores correm.
def aula15():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula16'))
    return render_template('aula15.html', pontuacao=pontos)
    


@app.route('/aula16', methods=('GET', 'POST'))#Dinossauros foram extintos OU cachorros tem asas..
def aula16():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "F":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula17'))
    return render_template('aula16.html', pontuacao=pontos)    




@app.route('/aula17', methods=('GET', 'POST'))#Borboletas voam OU peixes vivem na água.
def aula17():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "F":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula18'))
    return render_template('aula17.html', pontuacao=pontos)  





@app.route('/aula18', methods=('GET', 'POST'))#Cachorros tem patas OU árvores não correm.
def aula18():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "F":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula19'))
    return render_template('aula18.html', pontuacao=pontos)  





@app.route('/aula19', methods=('GET', 'POST'))#Árvores correm OU sapos voam..
def aula19():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "F":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "V":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula20'))
    return render_template('aula19.html', pontuacao=pontos)  





    

@app.route('/aula20', methods=('GET', 'POST'))#Cachorros não tem asas OU borboletas não comem peixes.
def aula20():
    global pontos
    if request.method == 'POST':
        title = request.form['resposta']

        if title == "V":
            pontos=pontos+10
            return render_template('correto.html')

        if title == "F":
            return render_template('errado.html')

        elif title == "proximo":
            return redirect(url_for('aula21'))
    return render_template('aula20.html', pontuacao=pontos)  




@app.route('/aula21', methods=('GET', 'POST'))
def aula21():
    global pontos
    global apelido    
    if request.method == 'POST':
        title = request.form['resposta']
        if title == "Ranking":
            salvando(apelido, pontos)
            return redirect(url_for('resultados'))
        else:
            return redirect(url_for('resultados'))   
    return render_template('aula21.html', pontuacao=pontos, resultado=pontos*100/200, nome=apelido)



@app.route('/resultados', methods=('GET', 'POST'))
def resultados():  
    if request.method == 'POST':
        title = request.form['resposta']
        if title == "Fim":            
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))    
    rows = ranking()
    return render_template('resultados.html', rows = rows)


app.run(host='0.0.0.0', debug=True)