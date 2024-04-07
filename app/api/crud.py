from sqlalchemy.orm import Session
from .. import models, schemas
from typing import Optional, List


def create_device_data(db: Session, device_data: schemas.DeviceDataCreate):
    db_device_data = models.DeviceData(**device_data.model_dump())
    db.add(db_device_data)
    db.commit()
    db.refresh(db_device_data)
    return db_device_data

def get_device_data(db: Session, device_data_id: int) -> Optional[models.DeviceData]:
    return db.query(models.DeviceData).filter(models.DeviceData.id == device_data_id).first()

def get_all_device_data(db: Session) -> List[models.DeviceData]:
    return db.query(models.DeviceData).all()