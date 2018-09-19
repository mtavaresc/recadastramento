# -*- coding: UTF-8 -*-
from flask import render_template, request
from base import app, db
from model import Pegaso, Trabalhador

# Creating new database of model "Worker"
db.create_all(bind="out")


@app.route("/<int:matricula>", methods=["GET", "POST"])
def recadastrar(matricula):
    pegaso = Pegaso.query.filter_by(matricula=matricula).first()

    if request.method == "POST":
        cpf = request.form.get("cpf")
        nis = request.form.get("nis")
        nome = request.form.get("nome")
        sexo = request.form.get("sexo")
        raca = request.form.get("raca")
        estciv = request.form.get("estciv")
        dtnascto = request.form.get("dtnascto")

        c = Trabalhador(cpf, nis, nome, sexo, raca, estciv, dtnascto)
        db.session.merge(c)
        db.session.commit()

        return render_template("submit.html")
    return render_template("index.html", pegaso=pegaso)


if __name__ == "__main__":
    app.run(debug=True)
