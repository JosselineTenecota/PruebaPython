from sqlalchemy.orm import Session
from . import models

class VehiculoRepository:
    def __init__ (self, db: Session):
        self.db = db
        def get_all(self):
            return self.db.query(models.Vehiculo).all()
        def create(self, vehiculo: models.Vehiculo):
            self.db.add(vehiculo)
            self.db.commit()
            self.db.refresh(vehiculo)
            return vehiculo
