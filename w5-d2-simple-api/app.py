import os
from bottle import route, run, get, error
import random


@get("/")
def index():
    return {
        "nombre": random.choice(["Pepe", "Juan", "Fran", "Luis"])
    }


@get("/chiste/<tipo>")
def demo2(tipo):
    print(f"un chiste de {tipo}")
    if tipo == "chiquito":
        return {
            "chiste": "Van dos soldados en una moto y no se cae ninguno porque van soldados"
        }
    elif tipo == "eugenio":
        return {
            "chiste": "Saben aquell que diu...."
        }
    else:
        return {
            "chiste": "No puedorrr!!"
        }


@error(404)
def error404(error):
    return {'error': 'oops'}


port = int(os.getenv("PORT", 8080))
print(f"Running server {port}....")

run(host="0.0.0.0", port=port, debug=True)
