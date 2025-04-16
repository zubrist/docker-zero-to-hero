# 🐍 Python Docker Example

This directory contains a simple Python application containerized with Docker. Let's explore how it works and how to run it!

## 📁 What's in this directory?

- **hello.py**: A simple Python script that prints "Hello, Docker World!"
- **Dockerfile**: Instructions for Docker on how to build the container image

## 🔍 Understanding the Code

### hello.py

```python
def main():
    print("Hello, Docker World!")

if __name__ == "__main__":
    main()
```

This is a simple Python script that:
1. Defines a `main()` function that prints a greeting
2. Uses the `if __name__ == "__main__":` pattern to ensure the function runs when the script is executed directly

### Dockerfile

```dockerfile
FROM python:3.8-slim-buster
WORKDIR /
COPY hello.py /
CMD ["python", "hello.py"]
```

This Dockerfile:
1. Starts with the official Python 3.8 slim image based on Debian Buster
2. Sets the working directory to the root of the container
3. Copies our hello.py script into the container
4. Specifies the command to run when the container starts (execute the Python script)

## 🚀 How to Run the Container

Follow these steps to build and run the Docker container:

### 1. Build the Docker Image

Navigate to the python directory (where the Dockerfile is located) and run:

```bash
docker build -t hello-python .
```

This command:
- `-t hello-python`: Tags (names) your image as "hello-python"
- `.`: Uses the current directory as the build context

### 2. Run the Container

After building the image, run it with:

```bash
docker run hello-python
```

You should see the output:
```
Hello, Docker World!
```

The container will exit after printing the message since the Python script completes its execution.

## 🔄 Making Changes

If you want to modify the message:

1. Edit the `hello.py` file
2. Rebuild the image: `docker build -t hello-python .`
3. Run the container again: `docker run hello-python`

## 🧪 Additional Docker Commands

Here are some useful Docker commands for working with this container:

```bash
# List all images
docker images

# List running containers
docker ps

# List all containers (including stopped ones)
docker ps -a

# Remove the image
docker rmi hello-python

# Run the container with a custom name
docker run --name my-python-app hello-python

# Remove a stopped container
docker rm my-python-app
```

## 🌟 Next Steps

Try these challenges to learn more:
1. Modify the Python script to accept a name parameter and print a personalized greeting
2. Add environment variables to the Docker run command to customize the behavior
3. Create a volume to share files between your host and the container

Happy containerizing! 🐳