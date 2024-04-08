from fastapi.testclient import TestClient
from app.main import app  # Uygulamanızın FastAPI instance'ını import edin
from app.database import Base, engine

# Test veritabanı için veritabanı tablolarını oluştur
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_api_create_device_data():
    response = client.post(
        "/device_data/",
        json={"route": "API Test Route", "service_point": "API Test SP", "mrf": "API Test MRF", "parcel": "API Test Parcel", "gps": "API Test GPS"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["route"] == "API Test Route"

def test_api_get_device_data():
    # Önce bir veri oluşturur ve sonra bu veriyi almak için GET isteği yapar
    post_response = client.post(
        "/device_data/",
        json={"route": "API Test Route", "service_point": "API Test SP", "mrf": "API Test MRF", "parcel": "API Test Parcel", "gps": "API Test GPS"}
    )
    device_data_id = post_response.json()["id"]
    get_response = client.get(f"/device_data/{device_data_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == device_data_id
    assert data["route"] == "API Test Route"
    # Daha fazla doğrulama...
