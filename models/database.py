from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Galeria(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    date = db.Column(db.String(100))
    description = db.Column(db.String(100))

def __init__(self, title, path, author, date, description):
    self.title = title
    self.author = author
    self.date = date
    self.description = description
    self.path = path
    
class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)
    
    def __init__(self, filename):
        self.filename = filename
