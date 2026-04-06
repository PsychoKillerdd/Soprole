from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/")
def inicio():
    return {"mensaje": "Redis API funcionando"}

@app.get("/get/{clave}")
def leer(clave: str):
    valor = r.get(clave)
    return {"clave": clave, "valor": valor} if valor else {"error": "No existe"}

@app.post("/set/{clave}/{valor}")
def guardar(clave: str, valor: str):
    r.set(clave, valor)
    return {"ok": True, "clave": clave, "valor": valor}

@app.get("/incr/{clave}")
def incrementar(clave: str):
    nuevo = r.incr(clave)
    return {"clave": clave, "valor": nuevo}

@app.get("/keys")
def listar():
    claves = r.keys("*")
    return {"claves": {c: r.get(c) for c in claves}}

@app.delete("/del/{clave}")
def eliminar(clave: str):
    eliminado = r.delete(clave)
    return {"eliminado": bool(eliminado)}