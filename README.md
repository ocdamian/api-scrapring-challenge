# Introduction 
This project is an API developed in Python that allows receiving a URL through a POST endpoint and extracting products from the online store.

# Getting Started
To run our project locally we must:
1.  Clone the repository


# Run with Docker
TTo run the project using Docker Desktop, follow these steps:
1.  Build the Docker image
    ```sh 
    docker build -t image-challenge . 
2.  Run the container:
    ```sh 
    docker run -it --rm -d -p 8000:8000 --name container-challenge image-challenge:latest
Now, the API should be running at http://localhost:8000 inside the Docker container.

# API Usage

## Endpoint:
**POST** `http://localhost:8000/api/v1/products/`

## Request Body (JSON Example)

```json
{
    "url": "https://www.jumbocolombia.com/supermercado/despensa/enlatados-y-conservas"
}
```


# Other examples:
   `https://www.jumbocolombia.com/supermercado/despensa/harinas-y-mezclas-para-preparar`
   `https://www.jumbocolombia.com/supermercado/despensa/bebida-achocolatada-en-polvo`
   `https://www.jumbocolombia.com/supermercado/despensa/aceite`

# Getting Started
To run our project locally we must:
1.  Create a virtual environment
    ```sh
    python -m venv venv
2.  Activate the virtual environment:
    - Windows
        ```sh
        .\venv\Scripts\Activate.ps1
    
    - Mac
        ```sh
        source venv/bin/activate    

3.  Install dependencies:
    ```sh
    pip install fastapi[standard]
4.  Run project:
    ```sh
    fastapi dev
# API Documentation (Swagger)
Once the project is running, you can access the interactive documentation at:

http://localhost:8000/docs





