from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from . import database, models, schemas, service

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI(title="Gestión Matrícula Vehicular")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_service(db: Session = Depends(database.get_db)):
    return service.VehiculoService(db)
@app.get("/api/vehiculos", response_model=List[schemas.VehiculoResponse])
def listar_vehiculos(srv: service.VehiculoService = Depends(get_service)):
    return srv.get_vehiculos()
@app.post("/api/vehiculos", response_model=schemas.VehiculoResponse)
def registrar_vehiculo(vehiculo: schemas.VehiculoCreate, srv: service.VehiculoService = Depends(get_service)):
    return srv.registrar_vehiculo(vehiculo)
