from pydantic import BaseModel
from typing import List

class DeviceDataCreate(BaseModel):
    route: str
    service_point: str
    mrf: str
    parcel: str
    gps: List[str]  # Cihazın birden fazla GPS verisini tutacak şekilde güncellendi

class DeviceData(DeviceDataCreate):
    id: int  # Veritabanında her cihaz verisi için benzersiz bir ID
    route: str
    service_point: str
    mrf: str
    parcel: str
    gps: List[str] 
    class Config:
        orm_mode = True
