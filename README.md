# Topo Technical Assessment

## Overview
For this project, I have chosen the following technologies:

### Backend (Python with FastAPI)
- Python provides a rich set of libraries for data processing.
- FastAPI is known for its high performance and ease of use.
- **Data Ingestion & Processing**: Implemented with the Pipeline design pattern
    - This is to enhance the reusability of each processing and ingestion step as much as possible.

### Frontend (React with NextJS)
- **Routing**: NextJS provides built-in file-system based routing, simplifying the development process.
- **Visualization**: Implemented with Recharts library for simple and effective data visualization.

## Production Deployment
- For production, both the frontend and backend are containerized into a single Docker image.  
- The frontend's static files are served using FastAPI.  
- This approach simplifies the setup process and preparation for production.


## Run the Application
To set up and run the project, follow these steps:

1. **Build the Docker Image**:
   ```bash
   docker build -t app .
   ```
2. **Run the Docker Container**:
    ```bash
    docker run -p 80:80 app
    ```
3. **Access the Application**:
    - API (Swagger UI): http://localhost:80/docs
    - Frontend: http://localhost:80/frontend


## Run Tests or Setup Project for Development
Navigate to the README file under the respective sub-directory (backend or frontend) for detailed instructions.
