from sqlalchemy.orm import Session
from .. import models, schemas
from typing import Optional, List

def create_device_data(db: Session, device_data: schemas.DeviceDataCreate):
    db_device_data = models.DeviceData(**device_data.model_dump())  # model_dump() yerine dict() kullanıldı.
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

def get_device_data(db: Session, device_data_id: int) -> Optional[models.DeviceData]:
    return db.query(models.DeviceData).filter(models.DeviceData.id == device_data_id).first()

def get_all_device_data(db: Session) -> List[models.DeviceData]:
    return db.query(models.DeviceData).all()

def get_device_location_history(db: Session, device_data_id: int) -> List[models.DeviceData]:
    # Bu örnekte, tüm konum geçmişini almak için basit bir query kullanıldı.
    # Gerçekte, bu fonksiyon belirli bir cihazın konum geçmişine göre filtrelenebilir.
    return db.query(models.DeviceData).filter(models.DeviceData.id == device_data_id).all()

def get_latest_location_for_all_devices(db: Session) -> List[models.DeviceData]:
    # Bu fonksiyon, her cihaz için son konumu döndürür.
    # Örnek bir SQL sorgusu: SELECT * FROM device_data WHERE id IN (SELECT MAX(id) FROM device_data GROUP BY device_id)
    # Burada basitleştirilmiş bir versiyon kullanacağız. Daha karmaşık bir sorgu, veritabanı yapınıza göre değişiklik gösterebilir.
    return db.query(models.DeviceData).group_by(models.DeviceData.device_id).all()
