from fastapi import FastAPI
from .database import engine
from .models import Base
from .api import endpoints
from tcp_server import start_tcp_server
from worker import consume_message
import asyncio


# Veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(endpoints.router)


async def app_startup():
    # TCP Server ve Consumer'ı başlat
    task1 = asyncio.create_task(start_tcp_server())
    task2 = asyncio.create_task(consume_message())
    print("Uygulama başlıyor...")

async def app_shutdown():
    # Gerekirse, uygulama kapatılırken temizlik işlemleri yapın
    print("Uygulama kapanıyor...")

@app.on_event("startup")
async def startup_event():
    await app_startup()

@app.on_event("shutdown")
async def shutdown_event():
    await app_shutdown()