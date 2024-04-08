from sqlalchemy.orm import Session
from .. import models, schemas
from typing import Optional, List
from sqlalchemy import func, desc

def create_device_data(db: Session, device_data: schemas.DeviceDataCreate):
    db_device_data = models.DeviceData(**device_data.dict())  # Pydantic modelden dict'e dönüşüm
    db.add(db_device_data)
    db.commit()
    db.refresh(db_device_data)
    return db_device_data

def delete_device_data(db: Session, device_data_id: int):
    db_device_data = db.query(models.DeviceData).filter(models.DeviceData.id == device_data_id).first()
    if db_device_data:
        db.delete(db_device_data)
        db.commit()
        return True
    return False

def get_device_data(db: Session, device_data_id: int):
    return db.query(models.DeviceData).filter(models.DeviceData.id == device_data_id).first()

def get_all_device_data(db: Session) -> List[models.DeviceData]:
    return db.query(models.DeviceData).all()

def get_device_location_history(db: Session, device_data_id: int):
    return db.query(models.DeviceData).filter(models.DeviceData.id == device_data_id).all()




def get_latest_location_for_all_devices(db: Session):
    device_data_list = db.query(models.DeviceData).all()
    latest_locations = []
    for device_data in device_data_list:
        # gps alanı bir liste olarak saklanıyor ve son konumu alıyoruz
        if device_data.gps and isinstance(device_data.gps, list):
            latest_gps = device_data.gps[-1]  # Listenin son elemanı en son GPS konumudur
            latest_locations.append({
                "id": device_data.id,
                "route": device_data.route,
                "service_point": device_data.service_point,
                "mrf": device_data.mrf,
                "parcel": device_data.parcel,
                "gps": [latest_gps]  # En son GPS konumu ekleyin
            })
    return latest_locations


