from flask import Flask, request, render_template, session, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask('Agenda')
app.secret_key = 'turmaS3'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agenda.db'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    foto = db.Column(db.String(45), nullable=False, unique=True)
    jogo_id = db.Column(db.String(45), nullable=False, unique=True)
    status_id = db.Column(db.String(45), nullable=False, unique=True)

class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(45), nullable=False)
    link = db.Column(db.String(45), nullable=False)

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(45), nullable=False)

class GamerTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jogo_id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(45), nullable=False, unique=True)

@app.route('/')
def inicio():
    nome = ''
    email = ''
    foto = ''
    jogo_id = ''
    status_id = ''
    
    if 'contatoAdicionado-nome' in session:
        nome = session['contatoAdicionado-nome']
        email = session['contatoAdicionado-e-mail']
        foto = session['contatoAdicionado-foto']
        jogo_id = session['contatoAdicionado-jogo_id']
        status_id = session['contatoAdicionado-status_id']
        del session['contatoAdicionado-nome']
    return render_template('index.html', nome=nome, email=email, foto=foto, jogo_id=jogo_id, status_id=status_id)

@app.route('/')
def inicio():
    descricao = ''
    link = ''
    
    if 'contatoAdicionado-descricao' in session:
        descricao = session['contatoAdicionado-descricao']
        link = session['contatoAdicionado-link']
        return render_template('index.html', descricao=descricao, link=link) 

@app.route('/')
def inicio():
    descricao = ''
    
    if 'contatoAdicionado-descricao' in session:
        descricao = session['contatoAdicionado-descricao']
    return render_template('index.html', descricao=descricao)

@app.route('/')
def inicio():
    jogo_id = ''
    usuario_id = ''
    username = ''
            
    if 'contatoAdicionado-jogo_id' in session:
        jogo_id = session['contatoAdicionado-jogo_id']
        usuario_id = session['contatoAdicionado-usuario_id']
        username = session['contatoAdicionado-username']
        del session['contatoAdicionado-nome']
    return render_template('index.html', jogo_id=jogo_id, usuario_id=usuario_id,
    username=username)

@app.route('/inserir')
def inserir():
    return render_template('inserir.html')

@app.route('/add-contato', methods=['POST'])
def addcontato():
    u = Usuario()
    u.nome = request.form['nome']
    u.email = request.form['e-mail']
    u.foto = request.form['foto']
    u.jogo_id = request.form['jogo_id']
    u.status_id = request.form['status']

    db.session.add(u)
    db.session.commit()

    session['contatoAdicionado-nome'] = u.nome
    session['contatoAdicionado-e-mail'] = u.email
    session['contatoAdicionado-nome'] = u.foto
    session['contatoAdicionado-telefone'] = u.jogo_id
    session['contatoAdicionado-nome'] = u.status_id

    return redirect('/')

@app.route('/inserir')
def inserir():
    return render_template('inserir.html')

@app.route('/add-contato', methods=['POST'])
def addcontato():
    j = Jogo()
    j.descricao = request.form['descricao']
    j.link = request.form['link']

    db.session.add(j)
    db.session.commit()

    session['contatoAdicionado-descricao'] = j.descricao
    session['contatoAdicionado-link'] = j.link

    return redirect('/')

@app.route('/inserir')
def inserir():
    return render_template('inserir.html')

@app.route('/add-contato', methods=['POST'])
def addcontato():
    s = Status()
    s.descricao = request.form['descricao']

    db.session.add(s)
    db.session.commit()

    session['contatoAdicionado-descricao'] = s.descricao

    return redirect('/')

@app.route('/inserir')
def inserir():
    return render_template('inserir.html')

@app.route('/add-contato', methods=['POST'])
def addcontato():
    g = GamerTag()
    g.usuario_id = request.form['usuario_id']
    g.username = request.form['username']

    db.session.add(g)
    db.session.commit()

    session['contatoAdicionado-usuario_id'] = g.usuario_id
    session['contatoAdicionado-username'] = g.username
    return redirect('/')

@app.route('/lista')
def lista():
    Usuario = Usuario.query.order_by(Usuario.nome)
    return render_template('lista.html', usuario=usuario)

@app.route('/lista')
def lista():
    Jogo = Jogo.query.order_by(Jogo.nome)
    return render_template('lista.html', jogo=jogo)

@app.route('/lista')
def lista():
    Status = Status.query.order_by(Status.nome)
    return render_template('lista.html', status=status)

@app.route('/lista')
def lista():
    GamerTag = GamerTag.query.order_by(GamerTag.nome)
    return render_template('lista.html', gamertag=gamertag)


@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'GET':
        return render_template('busca.html')
    elif request.method == 'POST':
        nomeABuscar = request.form['nome']
        usuario = Usuario.query.filter_by(nome=nomeABuscar).first()
        if contato is None:
            session['mensagem-busca'] = "Não encontrado"
        else:
            session['mensagem-busca'] = "{} tem o número {}".format(usuario.nome, usuario.email)
        
        return render_template('busca.html', msg=session['mensagem-busca'])

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'GET':
        return render_template('busca.html')
    elif request.method == 'POST':
        nomeABuscar = request.form['nome']
        jogo = Jogo.query.filter_by(nome=nomeABuscar).first()
        if jogo is None:
            session['mensagem-busca'] = "Não encontrado"
        else:
            session['mensagem-busca'] = "{} tem o número {}".format(jogo.nome, jogo.descricao)
        
        return render_template('busca.html', msg=session['mensagem-busca'])

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'GET':
        return render_template('busca.html')
    elif request.method == 'POST':
        nomeABuscar = request.form['nome']
        status = Status.query.filter_by(nome=nomeABuscar).first()
        if status is None:
            session['mensagem-busca'] = "Não encontrado"
        else:
            session['mensagem-busca'] = "{} tem o número {}".format(status.nome, status.descricao)
        
        return render_template('busca.html', msg=session['mensagem-busca'])

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'GET':
        return render_template('busca.html')
    elif request.method == 'POST':
        nomeABuscar = request.form['nome']
        gamertag = GamerTag.query.filter_by(nome=nomeABuscar).first()
        if gamertag is None:
            session['mensagem-busca'] = "Não encontrado"
        else:
            session['mensagem-busca'] = "{} tem o número {}".format(gamertag.nome, gamertag.usuario_id)
        
        return render_template('busca.html', msg=session['mensagem-busca'])


@app.route('/remover')
def remove():
    return render_template('remove.html')


@app.route('/rm-usuario', methods=['POST'])
def rmusuario():
    c = Usuario.query.filter_by(nome=request.form['nome']).first()
    
    db.session.delete(u)
    db.session.commit()
    return "Sucesso!"

@app.route('/rm-jogo', methods=['POST'])
def rmjogo():
    c = Jogo.query.filter_by(nome=request.form['nome']).first()
    
    db.session.delete(j)
    db.session.commit()
    return "Sucesso!"

@app.route('/rm-status', methods=['POST'])
def rmstatus():
    c = Status.query.filter_by(nome=request.form['nome']).first()
    
    db.session.delete(s)
    db.session.commit()
    return "Sucesso!"

@app.route('/rm-gamertag', methods=['POST'])
def rmgamertag():
    c = GamerTag.query.filter_by(nome=request.form['nome']).first()
    
    db.session.delete(g)
    db.session.commit()
    return "Sucesso!"


@app.route('/rm-rapido/<int:id>')
def rmrapido(id):
    remover = Usuario.query.filter_by(id=id).first()
    db.session.delete(remover)
    db.session.commit()
    return redirect('/lista')

@app.route('/rm-rapido/<int:id>')
def rmrapido(id):
    remover = Jogo.query.filter_by(id=id).first()
    db.session.delete(remover)
    db.session.commit()
    return redirect('/lista')

@app.route('/rm-rapido/<int:id>')
def rmrapido(id):
    remover = Status.query.filter_by(id=id).first()
    db.session.delete(remover)
    db.session.commit()
    return redirect('/lista')

@app.route('/rm-rapido/<int:id>')
def rmrapido(id):
    remover = GamerTag.query.filter_by(id=id).first()
    db.session.delete(remover)
    db.session.commit()
    return redirect('/lista')


if __name__ == '__main__':
    
    app.debug = True
    app.run()