from pydantic import BaseModel

class DeviceDataCreate(BaseModel):
    id:int
    route: str
    service_point: str
    mrf: str
    parcel: str
    gps: str

class DeviceData(DeviceDataCreate):
    id: int

    class Config:
        orm_mode = True
