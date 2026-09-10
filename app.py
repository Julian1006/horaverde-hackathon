"""La web de HoraVerde.

Aqui solo esta la parte de la pagina. Los datos los pide carbon_api.py.
"""

from flask import Flask, render_template

import carbon_api

app = Flask(__name__)


@app.route("/")
def inicio():
    """La pagina principal: cuanto contamina la luz ahora mismo."""
    ahora = carbon_api.intensidad_actual()
    mezcla = carbon_api.mezcla_actual()
    return render_template("inicio.html", ahora=ahora, mezcla=mezcla)


if __name__ == "__main__":
    app.run(debug=True)
