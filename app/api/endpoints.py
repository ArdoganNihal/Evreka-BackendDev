from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas
from . import crud
from ..database import get_db

router = APIRouter()


@router.post("/device_data/", response_model=schemas.DeviceData)
def create_device_data(device_data: schemas.DeviceDataCreate, db: Session = Depends(get_db)):
    print(device_data)
    return crud.create_device_data(db=db, device_data=device_data)

@router.delete("/device_data/{device_data_id}", status_code=204)
def delete_device_data(device_data_id: int, db: Session = Depends(get_db)):
    success = crud.delete_device_data(db=db, device_data_id=device_data_id)
    if not success:
        raise HTTPException(status_code=404, detail="DeviceData not found")
    return {"message": "DeviceData deleted successfully"}

@router.get("/device_data/{device_data_id}", response_model=schemas.DeviceData)
def read_device_data(device_data_id: int, db: Session = Depends(get_db)):
    db_device_data = crud.get_device_data(db=db, device_data_id=device_data_id)
    if db_device_data is None:
        raise HTTPException(status_code=404, detail="DeviceData not found")
    return db_device_data

@router.get("/device_data/", response_model=List[schemas.DeviceData])
def read_all_device_data(db: Session = Depends(get_db)):
    return crud.get_all_device_data(db=db)

@router.get("/device_data_history/{device_id}", response_model=List[schemas.DeviceData])
def read_device_location_history(device_id: int, db: Session = Depends(get_db)):
    return crud.get_device_location_history(db=db, device_data_id=device_id)

@router.get("/latest_device_locations/", response_model=List[schemas.DeviceData])
def read_latest_location_for_all_devices(db: Session = Depends(get_db)):
    return crud.get_latest_location_for_all_devices(db=db)