import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Buscamos la variable DATABASE_URL (la que inyectamos en docker-compose).
# Si no la encuentra, usa SQLite como plan de respaldo local.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./grimorio.db")

# PostgreSQL no requiere el connect_args de SQLite
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""

# 2. El motor (El cable físico)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. La sesión (La sala de trabajo)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. La clase Base
Base = declarative_base()

# 5. El portero de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""