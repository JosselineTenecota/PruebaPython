from pydantic import BaseModel

class VehiculoBase(BaseModel):
    placa: str
    propietario: str
    marca: str
    fabricacion: int
    valor_comercial: float

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoResponse(VehiculoBase):
    impuesto: float
    codigo_revision: str

    class Config:
        from_attributes = True




