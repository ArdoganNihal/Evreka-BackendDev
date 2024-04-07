from pydantic import BaseModel

class DeviceDataCreate(BaseModel):
    route: str
    service_point: str
    mrf: str
    parcel: str
    gps: str

class DeviceData(BaseModel):
    id: int
    route: str
    service_point: str
    mrf: str
    parcel: str
    gps: str

    class Config:
        orm_mode = True
