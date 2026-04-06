import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# String básico
r.set("nombre", "Vicente")
print(r.get("nombre"))          # Vicente

# Contador
r.set("visitas", 0)
r.incr("visitas")
r.incr("visitas")
print(r.get("visitas"))         # 2

# Con expiración
r.set("temporal", "chao!", ex=10)
print(r.ttl("temporal"))        # ~10 segundos

# Lista
r.rpush("frutas", "manzana", "pera", "uva")
print(r.lrange("frutas", 0, -1))  # ['manzana', 'pera', 'uva']

# Hash (como un dict)
r.hset("usuario:1", mapping={"nombre": "Vicente", "ciudad": "Santiago"})
print(r.hgetall("usuario:1"))

print("✅ Todo funcionó!")