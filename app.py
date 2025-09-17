from flask import Flask, jsonify, abort
from flask import request

days = [
    {"id": 1, "name": "Lunes"},
    {"id": 2, "name": "Martes"},
    {"id": 3, "name": "Miercoles"},
    {"id": 4, "name": "Jueves"},
    {"id": 5, "name": "Viernes"},
    {"id": 6, "name": "Sabado"},
    {"id": 7, "name": "Domingo"},
]

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_days():
    return jsonify(days)


@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in days if day["id"] == day_id]
    if len(day) == 0:
        abort(404)
    return jsonify({"day": day[0]})


@app.route("/", methods=["POST"])
def post_days():
    return jsonify({"success": True}), 201

#Medoto POST
@app.route("/saludo", methods=["POST"])
def saludo():
    data = request.get_json()
    nombre = data.get("nombre", "amigo")
    return jsonify({"mensaje": f"Hola, {nombre}!"})


#Metodo GET
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hola, mundo!"})

if __name__ == "__main__":
    app.run(debug=True)
