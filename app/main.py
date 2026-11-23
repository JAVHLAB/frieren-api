from fastapi import FastAPI
from app.database import engine, Base
from app.routers import hechizos

# 1. ORDEN DE CONSTRUCCIÓN: Le dice a SQLAlchemy que vaya a models.py
# y cree la tabla físicamente en el disco duro (el archivo grimorio.db)
Base.metadata.create_all(bind=engine)

# 2. INICIALIZACIÓN: Creamos la instancia de FastAPI
app = FastAPI(
    title="Frieren's Spell Archive",
    description="API RESTful para registrar y consultar magia",
    version="1.0.0"
)

# 3. ENCHUFAR LAS RUTAS: Conectamos el archivo hechizos.py al servidor principal
app.include_router(hechizos.router)

# 4. RUTA BASE: Un saludo de bienvenida
@app.get("/")
def root():
    return {
        "mensaje": "El Grimorio está abierto.", 
        "instruccion": "Visita http://localhost:8000/docs para probar la API"
    }