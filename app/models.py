from sqlalchemy import Column, String, Integer, Float
from . database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    placa = Column(String, primary_key=True, index=True)
    propietario = Column(String)
    marca = Column(String)
    fabricacion = Column(Integer)
    valor_comercial = Column(Float)
    impuesto = Column(Float)
    codigo_revision = Column(String)

    