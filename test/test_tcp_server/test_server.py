import asyncio
import pytest

async def tcp_client(message: str, host="localhost", port=8888):
    reader, writer = await asyncio.open_connection(host, port)
    writer.write(message.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()
    print("TCP client sent:", message)

@pytest.mark.asyncio
async def test_tcp_server():
    # Gönderilecek test mesajı
    test_message = "Test message"
    # TCP istemcisi aracılığıyla sunucuya mesaj gönder
    await tcp_client(test_message)
    # NOT: Bu test, sunucunun mesajı aldığını doğrulamaz.
    # Gerçek bir test ortamında, RabbitMQ'ya mesajın başarıyla gönderilip gönderilmediğini kontrol etmek için
    # ek mantık veya araçlar kullanmanız gerekir.
