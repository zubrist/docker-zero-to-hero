#  1) Choose a base image
FROM python:3.9-slim

# 2) Set the working directory
WORKDIR /app

# 3) Copy requirements.txt to the working directory || layer Optimization
# Docker caches layers, so if requirements.txt doesn't change, it won't re-install dependencies in 
# future builds.

COPY requirements.txt .        
# the dot after .txt means copy to the current working directory, which is /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# pip install requirements.text we all know , but 
# --no-cache-dir is here to avoid caching the dependencies which means it will not store the downloaded packages in the cache, which reduces the size of the final image.
# -r is here to tell pip to install the packages listed in the requirements.txt file. r stands for requirements.

# 4) Copy the rest of the application code to the working directory
COPY . .
# first dot means copy from the current directory, second dot means copy to the current working directory, which is /app


# 5) Expose the port that the application will run on
EXPOSE 8000

# 6) Set the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# "uvicorn" is the command to run the application, 
# "main:app" is the location of the FastAPI application, 
# "--host" and "--port" are used to specify the host and port that the application will run on.

# EXPOSE vs --port
# EXPOSE is used to inform Docker that the container will listen on the specified network ports at runtime.
# It does not actually publish the port to the host machine.
# whereas --port is used to specify the port that the application will run on inside the container.


