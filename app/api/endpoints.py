import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas
from . import crud
from ..database import get_db

# Logger'ı yapılandırın
logger = logging.getLogger("uvicorn.info")

router = APIRouter()

@router.post("/device_data/", response_model=schemas.DeviceData)
def create_device_data(device_data: schemas.DeviceDataCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating device data: {device_data}")
    created_data = crud.create_device_data(db=db, device_data=device_data)
    logger.info(f"Device data created with ID: {created_data.id}")
    return created_data

@router.delete("/device_data/{device_data_id}", status_code=204)
def delete_device_data(device_data_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting device data with ID: {device_data_id}")
    success = crud.delete_device_data(db=db, device_data_id=device_data_id)
    if not success:
        logger.warning(f"Device data not found: ID {device_data_id}")
        raise HTTPException(status_code=404, detail="DeviceData not found")
    logger.info(f"Device data deleted successfully: ID {device_data_id}")
    return {"message": "DeviceData deleted successfully"}

@router.get("/device_data/{device_data_id}", response_model=schemas.DeviceData)
def read_device_data(device_data_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching device data for ID: {device_data_id}")
    db_device_data = crud.get_device_data(db=db, device_data_id=device_data_id)
    if db_device_data is None:
        logger.warning(f"Device data not found: ID {device_data_id}")
        raise HTTPException(status_code=404, detail="DeviceData not found")
    return db_device_data

@router.get("/device_data/", response_model=List[schemas.DeviceData])
def read_all_device_data(db: Session = Depends(get_db)):
    logger.info("Fetching all device data")
    all_data = crud.get_all_device_data(db=db)
    return all_data

@router.get("/device_data_history/{device_id}", response_model=List[schemas.DeviceData])
def read_device_location_history(device_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching device location history for device ID: {device_id}")
    history = crud.get_device_location_history(db=db, device_data_id=device_id)
    return history

@router.get("/latest_device_locations/", response_model=List[schemas.DeviceData])
def read_latest_location_for_all_devices(db: Session = Depends(get_db)):
    logger.info("Fetching latest location for all devices")
    latest_locations = crud.get_latest_location_for_all_devices(db=db)
    return latest_locations
