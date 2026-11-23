from sqlalchemy import Column, Integer, String
from app.database import Base

class Hechizo(Base):
    __tablename__ = "magia"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, index=True, nullable=False)
    efecto = Column(String, nullable=False)
    costo_mana = Column(Integer, default=0)
    tipo_magia = Column(String, default="Utilidad")

