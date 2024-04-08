from sqlalchemy import Column, JSON, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class DeviceData(Base):
    __tablename__ = 'device_data'
    id = Column(Integer, primary_key=True, index=True)
    route = Column(String, index=True)
    service_point = Column(String, index=True)
    mrf = Column(String, index=True)
    parcel = Column(String, index=True)
    gps = Column(JSON)  # GPS verilerini JSON olarak saklıyoruz  # Basitlik adına, GPS verisini bir string olarak saklıyoruz. (Örn: "lat,lon")

# Veritabanı bağlantısı ve session oluşturucu
DATABASE_URL = "postgresql://postgres:postgres@localhost/devices"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Veritabanı tablosunu oluştur
Base.metadata.create_all(bind=engine)
