from flask import render_template, request, redirect, url_for, flash
from models.database import db, Galeria, Imagem
import urllib
from markupsafe import Markup 
import os
import uuid

padrao = [
    {'filename': 'arte_1.jpg'},
    {'filename': 'arte_4.webp'},
    {'filename': 'arte_3.webp'}
]
def init_app(app):
    #arquivos permitidos
    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif'])
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES
    
    @app.route('/', methods=['GET', 'POST'])
    def home():
        imagens = Imagem.query.all()
        if request.method == 'POST':
            file = request.files['file']
            if not arquivos_permitidos(file.filename):
                flash('Utilie apenas arquivos de imagem!', 'danger')
                return redirect(url_for('home'))
            filename = str(uuid.uuid4())
            
            #nome arquivo no banco
            img = Imagem(filename)
            db.session.add(img)
            db.session.commit()
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Imagem enviada com sucesso!', 'success')
            return redirect(url_for('home'))
            
        return render_template('index.html', imagens=imagens, padrao=padrao)