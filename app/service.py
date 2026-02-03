from sqlalchemy.orm import Session
from fastapi import HTTPException
from .repository import VehiculoRepository
from . import models, schemas

class VehiculoService:
    def __init__(self, db: Session):
        self.repo = VehiculoRepository(db)

    def get_vehiculos(self):
        return self.repo.get_all()

    def registrar_vehiculo(self, datos: schemas.VehiculoCreate):
        if len(datos.placa) < 4 or datos.placa[3] != '-':
            raise HTTPException(status_code=400, detail="La placa debe tener un guion - en la posicion 4")
        base = datos.valor_comercial * 0.025
        recargo = 0.0
        descuento = 0.0
        if datos.fabricacion < 2010:
            recargo = base * 0.10
        vocales = ['a', 'e', 'i', 'o', 'u']
        if datos.marca and datos.marca[0].lower() in vocales:
            descuento = 30.0
        impuesto_final = (base + recargo) - descuento
        if impuesto_final < 0:
            impuesto_final = 0.0

        parte1 = datos.placa[:3]
        parte2 = str(len(datos.propietario))
        parte3 = str(datos.fabricacion)[-1]
        codigo_generado = f"{parte1}{parte2}{parte3}"

        nuevo_vehiculo = models.Vehiculo(
            placa=datos.placa,
            propietario=datos.propietario,
            marca=datos.marca,
            fabricacion=datos.fabricacion,
            valor_comercial=datos.valor_comercial,
            impuesto=impuesto_final,
            codigo_revision=codigo_generado
        )
        return self.repo.create(nuevo_vehiculo)