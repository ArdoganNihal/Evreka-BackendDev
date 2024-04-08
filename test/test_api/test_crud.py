import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app import models, schemas
from app.api.crud import create_device_data, get_device_data
from app.database import Base

# Test veritabanı için SQLAlchemy engine ve sessionmaker oluştur
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/devices"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db_session():
    # Veritabanı tablolarını oluştur
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_create_device_data(db_session: Session):
    test_data = schemas.DeviceDataCreate(route="Test Route", service_point="Test SP", mrf="Test MRF", parcel="Test Parcel", gps="Test GPS")
    device_data = create_device_data(db_session, device_data=test_data)
    assert device_data.route == test_data.route
    # Daha fazla doğrulama...

def test_get_device_data(db_session: Session):
    test_data = schemas.DeviceDataCreate(route="Test Route", service_point="Test SP", mrf="Test MRF", parcel="Test Parcel", gps="Test GPS")
    device_data = create_device_data(db_session, device_data=test_data)
    retrieved_data = get_device_data(db_session, device_data_id=device_data.id)
    assert retrieved_data == device_data
