from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DeviceData(Base):
    __tablename__ = 'device_data'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    route = Column(String, index=True)
    service_point = Column(String)
    mrf = Column(String)
    parcel = Column(String)
    gps = Column(String)  # Basitlik adına, GPS verisini bir string olarak saklıyoruz. (Örn: "lat,lon")

# Veritabanı bağlantısı ve session oluşturucu
DATABASE_URL = "postgresql://postgres:postgres@localhost/devices"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Veritabanı tablosunu oluştur
Base.metadata.create_all(bind=engine)
