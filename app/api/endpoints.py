from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas
from . import crud
from ..database import get_db

router = APIRouter()

@router.post("/device_data/", response_model=schemas.DeviceData)
def create_device_data(device_data: schemas.DeviceDataCreate, db: Session = Depends(get_db)):
    return crud.create_device_data(db=db, device_data=device_data)

@router.get("/device_data/", response_model=List[schemas.DeviceData])
def read_device_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    device_data = crud.get_device_data_list(db, skip=skip, limit=limit)
    return device_data

@router.get("/device_data/", response_model=List[schemas.DeviceData])
def read_all_device_data(db: Session = Depends(get_db)):
    return crud.get_all_device_data(db=db)
# Burada diğer CRUD operasyonları için route'lar tanımlanabilir
