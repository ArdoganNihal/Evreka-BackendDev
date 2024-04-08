import pytest
import asyncio
import json

@pytest.mark.asyncio
async def test_tcp_server_receives_json_message():
    # TCP sunucunuza bağlanıp mesaj gönderen asenkron bir istemci fonksiyonu
    async def send_tcp_message(host, port, message):
        reader, writer = await asyncio.open_connection(host, port)
        writer.write(message.encode())
        await writer.drain()
        writer.close()
        await writer.wait_closed()

    # Test için JSON mesajı, birden fazla GPS verisi içeren bir liste ile
    test_message = json.dumps({
        "route": "route1",
        "service_point": "service_point1",
        "mrf": "mrf1",
        "parcel": "parcel1",
        "gps": ["gps1", "gps2", "gps3"]  # GPS alanını bir liste olarak güncelle
    })

    # TCP sunucunuza mesaj gönderin
    await send_tcp_message("localhost", 8888, test_message)

    # Bu örnekte, sunucunun mesajı aldığını doğrulamak için ek bir mekanizma yoktur.
    # Gerçek bir test senaryosunda, sunucunun mesajı aldığına dair bir doğrulama yapmanız gerekir.
