from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Chamado(db.Model):
    __tablename__ = "chamados"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default="Aberto")
    data_abertura = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status,
            "data_abertura": self.data_abertura.isoformat()
        }