import asyncio
import aio_pika
import httpx
import json

async def send_to_fastapi(data_dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/device_data/",
            json=data_dict,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )
        print("Data sent to FastAPI, response status:", response.status_code)

async def consume_message():
    rabbitmq_url = "amqp://guest:guest@localhost/"
    connection = await aio_pika.connect_robust(rabbitmq_url)
    
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("device_location", durable=True)
        
        async for message in queue:
            async with message.process():
                data = message.body.decode()
                try:
                    # JSON string'ini Python sözlüğüne dönüştür
                    data_dict = json.loads(data)
                    print("Received message:", data)
                    # Dönüştürülen JSON verisini FastAPI uygulamanıza gönderin
                    await send_to_fastapi(data_dict)
                except json.JSONDecodeError as e:
                    print(f"JSON decoding error: {e}")
                    # Burada hatalı veri için uygun bir işlem yapabilirsiniz.
                    # Örneğin, loglama yapmak veya bir hata kuyruğuna eklemek.

if __name__ == "__main__":
    asyncio.run(consume_message())
