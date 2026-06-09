from flask import Flask, request, jsonify, render_template, redirect
from models import db, Chamado
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpdesk.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()
@app.route("/")
def home():
    chamados = Chamado.query.order_by(
        Chamado.id.desc()
    ).all()
    return render_template(
        "index.html",
        chamados=chamados
    )
@app.route("/novo", methods=["POST"])
def novo_chamado():
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    chamado = Chamado(
        titulo=titulo,
        descricao=descricao
    )
    db.session.add(chamado)
    db.session.commit()
    return redirect("/")
@app.route("/resolver/<int:id>")
def resolver(id):
    chamado = Chamado.query.get_or_404(id)
    chamado.status = "Resolvido"
    db.session.commit()
    return redirect("/")
@app.route("/excluir/<int:id>")
def excluir(id):
    chamado = Chamado.query.get_or_404(id)
    db.session.delete(chamado)
    db.session.commit()
    return redirect("/")
@app.route("/api/chamados", methods=["POST"])
def criar_chamado():
    dados = request.json
    chamado = Chamado(
        titulo=dados["titulo"],
        descricao=dados["descricao"]
    )
    db.session.add(chamado)
    db.session.commit()
    return jsonify(chamado.to_dict()), 201
@app.route("/api/chamados", methods=["GET"])
def listar_chamados():
    chamados = Chamado.query.all()
    return jsonify(
        [c.to_dict() for c in chamados]
    )
@app.route("/api/chamados/<int:id>", methods=["GET"])
def obter_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    return jsonify(chamado.to_dict())
@app.route("/api/chamados/<int:id>", methods=["PUT"])
def atualizar_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    dados = request.json
    chamado.status = dados.get(
        "status",
        chamado.status
    )
    db.session.commit()
    return jsonify(chamado.to_dict())
@app.route("/api/chamados/<int:id>", methods=["DELETE"])
def deletar_chamado(id):
    chamado = Chamado.query.get_or_404(id)
    db.session.delete(chamado)
    db.session.commit()
    return "", 204
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )