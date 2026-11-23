from pydantic import BaseModel, Field
from typing import Optional

# 1. El molde base: Atributos que TODOS los hechizos van a tener
class HechizoBase(BaseModel):
    # Field(...) indica que el campo es OBLIGATORIO (el equivalente a nullable=False de la BD, pero para internet)
    nombre: str = Field(..., min_length=3, description="Nombre exacto del hechizo")
    efecto: str = Field(..., min_length=5, description="Descripción de lo que hace")
    
    # ge=0 significa "Greater or Equal a 0". Evita que metan maná negativo.
    costo_mana: int = Field(default=0, ge=0)
    tipo_magia: str = Field(default="Utilidad")

# 2. El molde de ENTRADA (Lo que el usuario envía para crear un hechizo)
class HechizoCreate(HechizoBase):
    pass # Hereda todo de HechizoBase, no necesitamos pedirle el ID porque aún no existe.

# 3. El molde de SALIDA (Lo que tu API le responde al usuario)
class HechizoResponse(HechizoBase):
    id: int # Aquí SÍ le enviamos el ID que la base de datos generó

    # Esta configuración es la clave que conecta Pydantic con SQLAlchemy
    class Config:
        from_attributes = True

class HechizoUpdate(BaseModel):
    nombre: Optional[str] = None
    efecto: Optional[str] = None
    costo_mana: Optional[int] = None
    tipo_magia: Optional[str] = None

    