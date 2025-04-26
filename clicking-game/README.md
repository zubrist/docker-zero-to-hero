# 🎮 Cyber Clicker: A Docker-Powered Click Game

This directory contains an interactive clicking game built with FastAPI and Redis, containerized with Docker. Let's explore how this cyberpunk-themed project works!

## 📁 What's in this directory?

- **app.py**: The FastAPI application with our clicking game
- **requirements.txt**: Python dependencies
- **Dockerfile**: Instructions for building our application container
- **docker-compose.yml**: Multi-container setup for our app and Redis

## 🔍 Understanding the Components

### FastAPI Application (app.py)
Our FastAPI application serves as the backbone of the Cyber Clicker game. It:
1. Tracks visitor counts using Redis
2. Manages the clicking game interface
3. Handles high score persistence
4. Serves a cyberpunk-themed UI

### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

```dockerfile
FROM python:3.9-slim
```
- **Why?** This is our base image. We chose `python:3.9-slim` because:
  - It includes Python 3.9 runtime
  - `slim` variant is smaller than full image but includes essential build tools
  - Reduces final container size while maintaining functionality

```dockerfile
WORKDIR /app
```
- **Why?** Sets the working directory inside the container:
  - Creates `/app` if it doesn't exist
  - All subsequent commands will run from this directory
  - Keeps container filesystem organized

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```
- **Why?** Two-step dependency installation:
  - Copies only requirements first to leverage Docker's cache
  - `--no-cache-dir` reduces image size by not storing pip cache
  - This layer only rebuilds if requirements.txt changes

```dockerfile
COPY app.py .
```
- **Why?** Copies our application code:
  - Done after dependencies for better caching
  - Changes to app.py won't trigger dependency reinstallation

```dockerfile
EXPOSE 8000
```
- **Why?** Documents the port:
  - Acts as documentation for other developers
  - Tells Docker which port the application uses
  - Note: Doesn't actually publish the port (docker-compose.yml does that)

```dockerfile
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```
- **Why?** Specifies the command to run:
  - Uses Uvicorn ASGI server for FastAPI
  - `--host "0.0.0.0"` allows external access
  - `--reload` enables hot-reload for development
  - Can be overridden from docker-compose.yml


### Docker Compose
```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - redis

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```


```yaml
services:
  web:
    build: .
```
- **Why?** Defines our FastAPI service:
  - `build: .` tells Docker to use local Dockerfile
  - Service named 'web' for easy reference

```yaml
    ports:
      - "8000:8000"
```
- **Why?** Maps container ports to host:
  - Left side (8000): Host port
  - Right side (8000): Container port
  - Allows accessing app from browser

## How Port Mapping Works

Think of it as: `"HOST_PORT:CONTAINER_PORT"`
- HOST_PORT: Where you access the service on your computer
- CONTAINER_PORT: Where the service runs inside Docker

## Let's Modify Our Project

### Example 1: Change Web Access Port
```yaml
services:
  web:
    ports:
      - "3000:8000"  # Now access at localhost:3000
```
What changes?
- Inside container: FastAPI still runs on port 8000
- On your computer: Access at `http://localhost:3000`
- In `app.py`: No changes needed! Code stays the same


```yaml
    volumes:
      - .:/app
```
- **Why?** Mounts local directory:
  - Maps current directory (.) to container's /app
  - Enables live code updates
  - Changes reflect without rebuilding

```yaml
    depends_on:
      - redis
```
- **Why?** Manages service startup order:
  - Ensures Redis starts before web service
  - Doesn't guarantee Redis is ready, just started

```yaml
  redis:
    image: redis:alpine
```
- **Why?** Sets up Redis service:
  - Uses official Redis image
  - Alpine variant for smaller size
  - No build needed, pulls from Docker Hub

```yaml
    ports:
      - "6379:6379"
```
- **Why?** Exposes Redis port:
  - Allows direct Redis access if needed
  - Useful for development/debugging
  - Could be removed in production

## 🏗️ The Architecture

### FastAPI: Our Speed-Demon Web Framework
FastAPI serves as our game's backend, providing:
- Lightning-fast HTTP endpoints
- Automatic API documentation
- Real-time score updates
- HTML template serving

### Redis: Our Speedy Data Store
Redis acts as our in-memory database:
- Tracks visitor counts
- Stores high scores for each game mode
- Provides blazing-fast data access
- Persists data between container restarts

## 🚀 How to Run the Game

1. **Build and Start the Containers**
```bash
docker-compose up --build
```

2. **Access the Game**
- Open your browser to `http://localhost:8000`
- Start clicking!
- Try different time modes
- Save your high scores

3. **View the Logs**
```bash
docker-compose logs -f
```

## 🔄 Development Workflow

The setup includes hot-reload, so you can:
1. Modify `app.py`
2. Changes apply automatically
3. Refresh your browser to see updates

## 🛠️ Useful Docker Commands

```bash
# Start in background
docker-compose up -d

# Stop containers
docker-compose down

# View container status
docker-compose ps

# Check container logs
docker-compose logs web
docker-compose logs redis
```

## 🌟 Future additions 

1. Add new game modes
2. Implement user authentication
3. Add multiplayer support
4. Create additional visual effects

Happy clicking! 🎮✨