# 🚀 Spring Boot with Docker: A Complete Setup Guide

This directory contains a Spring Boot application containerized with Docker. Let's explore how we set up and ran this project step by step!

---

## 📁 What's in this directory?

- **`Application.java`**: The main entry point for our Spring Boot application.
- **`HelloController.java`**: A simple REST controller to test our application.
- **`pom.xml`**: Maven configuration file for managing dependencies and building the project.
- **`Dockerfile`**: Instructions for building our Spring Boot application container.
- **`docker-compose.yml`**: (Optional) Multi-container setup for future extensions.

---

## 🔍 Understanding the Components

### Spring Boot Application (`Application.java`)
Our Spring Boot application serves as the backbone of this project. It:
1. Starts the application using the `SpringApplication.run()` method.
2. Includes a REST controller (`HelloController`) that responds with a simple message: `"Hello, Docker!"`.

### Dockerfile
```dockerfile
FROM openjdk:17-jdk-slim

WORKDIR /app

COPY ./target/SB_Mongo-0.0.1-SNAPSHOT.jar /app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app.jar"]
```
This Dockerfile:
1. Uses the `openjdk:17-jdk-slim` base image.
2. Sets the working directory to `/app`.
3. Copies the compiled JAR file to the container.
4. Exposes port `8080` for the application.
5. Defines the entry point to run the JAR file.

### Docker Compose (`docker-compose.yml`)
```yaml
version: '3'
services:
  sb-mongo:
    build: .
    ports:
      - "8080:8080"
```
This `docker-compose.yml` file:
1. Defines a service named `sb-mongo`.
2. Builds the Docker image using the current directory's Dockerfile.
3. Maps port `8080` of the container to port `8080` on the host.

---

## 🛠️ Step-by-Step Setup
1.  Build the JAR File:
We used a Maven Docker image to build the Spring Boot application without installing Maven locally:

```bash
docker run --rm -v "$PWD":/app -w /app maven:3.8.4-openjdk-17 mvn package
```
- **what it does**:
  - mounts the current directory (`$PWD`) to the container at `/app`.
  - sets the working directory to `/app`.
  - runs the `mvn package` command to build the JAR file.

- **Output**: The JAR file is built and placed in the `target` directory.

2.  Build the Docker Image:
We built the Docker image  for the Spring Boot application using the Dockerfile in the current directory:

```bash
docker build -t springboot-app ./SpringBoot
```
- **what it does**:
  - ses the `Dockerfile` to create an image named springboot-app.
  - Copies the JAR file from the `target` directory to the container.

- **Output**: The Docker image is built and ready to be run.

3.  Run the Docker Container:
We ran the Docker container and mapped the container to port `8080` on the host:

```bash
docker run -p 8080:8080 springboot-app
```
- **what it does**:
  - runs the Docker container with the image springboot-app.
  - maps the container's port `8080` to the host's port `8080`.
  - starts the Spring Boot application.

- **Output**: The Spring Boot application is running and accessible at `http://localhost:8080`.

4.  Test the Application:
We tested the application by sending a GET request to the root URL (`/`) and checking the response:

```bash
curl http://localhost:8080/
```
- **what it does**:
  - sends a GET request to the root URL of the application.
  - checks the response to verify that the application is running correctly.

- **Output**: The response should be a simple "Hello, Docker!" message.


## 🔄 Development Workflow
1. Modify the code (e.g., HelloController.java).
2. Rebuild the JAR file:

```bash
docker run --rm -v "${PWD}/SpringBoot:/app" -w /app maven:3.8.5-openjdk-17 mvn clean package
```
3. Rebuild the Docker image:

```bash
docker build -t springboot-app ./SpringBoot
```
4. Restart the container:

```bash
docker run -p 8080:8080 springboot-app
```
> OR run the `docker-compose.yml` file

```bash
docker-compose up --build
```

5. Test the Application:

```bash
curl http://localhost:8080/
```
6. Repeat steps 1-5 as needed to make further changes and test the application.