# ☕ Java Docker Example

This directory contains a simple Java application containerized with Docker. Let's explore how it works and how to run it!

## 📁 What's in this directory?

- **helloWorld.java**: A simple Java program that prints "Hello, World!"
- **Dockerfile**: Instructions for Docker on how to build the container image

## 🔍 Understanding the Code

### helloWorld.java

```java
package java;
// @file helloWorld.java

public class helloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

This is a simple Java program that:
1. Declares a package named `java`
2. Defines a class called `helloWorld` with a `main` method
3. Prints "Hello, World!" to the console when executed

### Dockerfile

```dockerfile
FROM openjdk:8
WORKDIR /
COPY helloWorld.java /
RUN javac helloWorld.java
EXPOSE 8080
CMD ["java", "helloWorld"]
```

This Dockerfile:
1. Starts with the official OpenJDK 8 image
2. Sets the working directory to the root of the container
3. Copies our helloWorld.java file into the container
4. Compiles the Java code during the build process
5. Exposes port 8080 (though our simple app doesn't use it)
6. Specifies the command to run when the container starts (execute the compiled Java class)

## 🚀 How to Run the Container

Follow these steps to build and run the Docker container:

### 1. Build the Docker Image

Navigate to the java directory (where the Dockerfile is located) and run:

```bash
docker build -t hello-java .
```

This command:
- `-t hello-java`: Tags (names) your image as "hello-java"
- `.`: Uses the current directory as the build context

During the build process, Docker will:
1. Pull the OpenJDK 8 base image (if not already present)
2. Copy your Java file into the container
3. Compile the Java code
4. Create a runnable image

### 2. Run the Container

After building the image, run it with:

```bash
docker run hello-java
```

You should see the output:
```
Hello, World!
```

The container will exit after printing the message since the Java program completes its execution.

## 🔄 Making Changes

If you want to modify the message or code:

1. Edit the `helloWorld.java` file
2. Rebuild the image: `docker build -t hello-java .`
3. Run the container again: `docker run hello-java`

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
docker rmi hello-java

# Run the container with a custom name
docker run --name my-java-app hello-java

# Remove a stopped container
docker rm my-java-app

# Run the container in interactive mode
docker run -it hello-java
```

## 🌟 Next Steps

Try these challenges to learn more:
1. Modify the Java program to accept command-line arguments and print a personalized greeting
2. Create a more complex Java application with multiple classes
3. Use a multi-stage build to create a smaller final image
4. Add a volume to share files between your host and the container



**Happy containerizing!** 🐳
