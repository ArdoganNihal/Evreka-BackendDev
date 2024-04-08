from unittest.mock import patch, AsyncMock
import pytest
import json
from worker.consumer import consume_message

@pytest.mark.asyncio
@patch("worker.consumer.aio_pika.connect_robust", new_callable=AsyncMock)
@patch("worker.consumer.send_to_fastapi", new_callable=AsyncMock)
async def test_consume_message(mock_send_to_fastapi, mock_connect_robust):
    # Mesajı ve queue'yu mock'la
    mock_message = AsyncMock()
    mock_message.body.decode.return_value = json.dumps({
        "route": "route1", 
        "service_point": "service_point1", 
        "mrf": "mrf1", 
        "parcel": "parcel1", 
        "gps": "g"
    })
    
    mock_queue = AsyncMock()
    mock_queue.get = AsyncMock(return_value=mock_message)
    
    mock_channel = AsyncMock()
    mock_channel.declare_queue = AsyncMock(return_value=mock_queue)
    
    mock_connection = AsyncMock()
    mock_connection.channel = AsyncMock(return_value=mock_channel)
    
    mock_connect_robust.return_value = mock_connection
    print(mock_send_to_fastapi.call_args)

    # RabbitMQ'dan mesaj alımını simüle et
    await consume_message()

    # `send_to_fastapi` fonksiyonunun beklenen argümanlarla çağrıldığını doğrula
    mock_send_to_fastapi.assert_awaited_with({
        "route": "route1", 
        "service_point": "service_point1", 
        "mrf": "mrf1", 
        "parcel": "parcel1", 
        "gps": "g"
    })
