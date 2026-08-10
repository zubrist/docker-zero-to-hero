from fastapi import FastAPI
import platform
# platfrm is used to get the system information like OS, version, etc.
import os


app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "online",
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
        "env_app_version": os.getenv("APP_VERSION", "1.0.0"),
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
    