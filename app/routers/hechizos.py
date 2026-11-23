from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

# Creamos el enrutador (un mini-FastAPI dedicado solo a hechizos)
router = APIRouter(
    prefix="/hechizos",
    tags=["Magia de Frieren"]
)

# RUTA 1: CREAR (POST)
@router.post("/", response_model=schemas.HechizoResponse, status_code=201)
def registrar_hechizo(hechizo: schemas.HechizoCreate, db: Session = Depends(get_db)):
    
    # 1. Lógica de negocio: Evitar duplicados
    hechizo_existente = db.query(models.Hechizo).filter(models.Hechizo.nombre == hechizo.nombre).first()
    if hechizo_existente:
        raise HTTPException(status_code=400, detail="Este hechizo ya está en el Grimorio")
    
    # 2. La TRADUCCIÓN: De Esquema (Internet) a Modelo (Base de Datos)
    nuevo_hechizo = models.Hechizo(
        nombre=hechizo.nombre,
        efecto=hechizo.efecto,
        costo_mana=hechizo.costo_mana,
        tipo_magia=hechizo.tipo_magia
    )
    
    # 3. La ESCRITURA: Usamos la sesión para guardar
    db.add(nuevo_hechizo)
    db.commit()
    db.refresh(nuevo_hechizo) # Actualiza el objeto para que Python sepa qué ID le dio la base de datos
    
    # 4. La RESPUESTA: FastAPI convierte este modelo automáticamente al HechizoResponse
    return nuevo_hechizo

# RUTA 2: LEER (GET)
@router.get("/", response_model=list[schemas.HechizoResponse])
def listar_hechizos(db: Session = Depends(get_db)):
    # Trae absolutamente todos los registros de la tabla
    hechizos = db.query(models.Hechizo).all()
    return hechizos

# RUTA 3: BORRAR (DELETE)
@router.delete("/{hechizo_id}", status_code=204)
def eliminar_hechizo(hechizo_id: int, db: Session = Depends(get_db)):
    hechizo = db.query(models.Hechizo).filter(models.Hechizo.id == hechizo_id).first() 

    if not hechizo:
        raise HTTPException(status_code=404, detail="Hechizo no encontrado")

    db.delete(hechizo)
    db.commit()

    return None

@router.patch("/{hechizo_id}", response_model=schemas.HechizoResponse)
def actualizar_hechizo(hechizo_id: int, hechizo_nuevo: schemas.HechizoUpdate, db: Session = Depends(get_db)):
    
    hechizo_actual = db.query(models.Hechizo).filter(models.Hechizo.id == hechizo_id).first()

    if not hechizo_actual:
        raise HTTPException(status_code=404, detail="Hechizo no encontrado")

    datos_nuevos = hechizo_nuevo.model_dump(exclude_unset=True)

    for llave, valor in datos_nuevos.items():
        setattr(hechizo_actual, llave, valor)

    db.commit()
    db.refresh(hechizo_actual)

    return hechizo_actual

