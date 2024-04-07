# tcp_server/server.py
import asyncio
import aio_pika

async def send_to_rabbitmq(message: str):
    rabbitmq_url = "amqp://guest:guest@localhost/"
    connection = await aio_pika.connect_robust(rabbitmq_url)
    
    async with connection:
        channel = await connection.channel()        
        await channel.declare_queue("device_location", durable=True)        
        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key="device_location",
        )
        print("Message sent to RabbitMQ:", message)

async def handle_client(reader, writer):
    data = await reader.read(100)  # Adjust based on your data size
    message = data.decode()
    print("Received from TCP:", message)
    
    await send_to_rabbitmq(message)
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8888)
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
