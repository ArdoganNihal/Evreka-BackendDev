import asyncio
import aio_pika
import httpx


async def consume_message():
    rabbitmq_url = "amqp://guest:guest@localhost/"
    connection = await aio_pika.connect_robust(rabbitmq_url)
    
    async with connection:
        # Bağlantı üzerinden bir kanal oluştur
        channel = await connection.channel()
        
        # 'device_location' adlı kuyruğu tanımla
        queue = await channel.declare_queue("device_location", durable=True)
        
        # Kuyruktan gelen mesajları tüketmeye başla
        async for message in queue:
            async with message.process():
                data = message.body.decode()
                print("Received message:", message.body.decode())
                async with httpx.AsyncClient() as client:
                    response = await client.post("http://localhost:8000/device_data/", json={"data": data})
                    print("Data sent to FastAPI, response status:", response.status_code)
                # Burada mesajı işleyebilirsiniz
                # Örneğin, bir veritabanına kaydetmek

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume_message())
