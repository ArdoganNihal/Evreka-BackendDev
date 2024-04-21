from fastapi import FastAPI
from .database import engine # Veritabanı bağlantı motorunu içe aktarır
from .models import Base  # Veritabanı modelleri için temel sınıfı içe aktarır
from .api import endpoints # Uygulamanın API endpoint'lerini içeren modülü içe aktarır
from tcp_server import start_tcp_server # TCP server başlatma fonksiyonunu içe aktarır
from worker import consume_message  # Mesaj tüketimi için worker fonksiyonunu içe aktarır
import asyncio # Asenkron işlemler için asyncio modülünü içe aktarır
import logging # Loglama işlemleri için logging modülünü içe aktarır


# Loglama yapılandırması
logging.basicConfig(level=logging.INFO) # Loglama seviyesini INFO olarak ayarlar
logger = logging.getLogger(__name__) # Logger nesnesi oluşturur

# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine) # Veritabanında tanımlı tüm tabloları oluşturur

app = FastAPI()  # FastAPI uygulaması nesnesi oluşturur

app.include_router(endpoints.router) # Uygulamaya API router'ını ekler


async def app_startup():
    # TCP Server ve Consumer'ı başlat
    task1 = asyncio.create_task(start_tcp_server()) # TCP server'ı asenkron olarak başlatır
    task2 = asyncio.create_task(consume_message())  # Mesaj tüketiciyi asenkron olarak başlatır
    logger.info("Uygulama başlıyor...")  # Log mesajı

async def app_shutdown():
    # Gerekirse, uygulama kapatılırken temizlik işlemleri yapın
    logger.info("Uygulama kapanıyor...")  # Log mesajı

@app.router.lifespan.on_startup
async def startup_event():
    await app_startup()

@app.router.lifespan.on_shutdown
async def shutdown_event():
    await app_shutdown()