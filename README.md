# IoT Location Service

This project is designed to handle location data from IoT devices using a robust architecture that includes a TCP server for data intake, a message queue for intermediate storage, and a PostgreSQL database for persistent storage. It leverages FastAPI as a Python web framework, providing a RESTful API for managing devices and querying location data.

## Features

- **TCP Server for Data Collection**: Collects GPS location data from IoT devices using TCP as the communication protocol.
- **Queue System**: Utilizes a message queue to temporarily store incoming data before it is written to the database, ensuring data integrity and decoupling data intake from processing.
- **PostgreSQL Database**: Stores device information and location data, providing a robust solution for data persistence.
- **RESTful API**: Offers endpoints for creating, deleting, and listing devices, as well as listing location history by device and retrieving the last known location for all devices.
- **Logging**: Comprehensive logging of activities and errors for troubleshooting and monitoring purposes.
- **Documentation**: Includes clear and readable documentation for easy understanding and maintenance. http://localhost:8000/docs/
- **Testing**: Comes with examples of unit and integration tests to ensure the reliability of the service.

## Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- PostgreSQL
- RabbitMQ or any other message queue solution
- Uvicorn or any ASGI server for running FastAPI

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourgithub/iot-location-service.git
   ```

2. Navigate to the project directory:
   ```sh
   cd Evreka-BackendDev
   pip install -r requirements.txt
   source venv/bin/activate
   ```
3. Start the PostgreSQL database and RabbitMQ service.
4. ```sh
   uvicorn app.main:app --reload
   ```

5. Testing

```sh
pytest
```

## API Endpoints

### The RESTful API provides the following endpoints:

- **POST /device_data/**: Create a new device with location data.
- **DELETE /device_data/{device_id}**: Delete a device by its ID.
- **GET /device_data/**: List all devices.
- **GET /device_data/{device_id}**: Get location history for a specific device.
- **GET /latest_device_locations/**: Get the last known location for all devices.

## Architecture Overview

The IoT Location Service is designed with scalability and reliability in mind. The architecture includes:

- **TCP Server**: Handles high-throughput data intake from IoT devices in real-time.
- **Message Queue**: Acts as a buffer to ensure data is processed efficiently without loss, even during high load.
- **Database**: Ensures safe storage of device and location data, supporting complex queries for analytics.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Ensure to update tests as appropriate.
