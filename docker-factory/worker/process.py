import time
import os 
# os is a module that provides a way of using operating system dependent functionality like reading or writing 
# to the file system.

def heavy_computation():
    print("worker sarting heavy computation ...")

    # Simulate CPU bound task
    result = 0
    for i in range(10**7):
        result += i
    print(f"Computation result: {result}")


if __name__ == "__main__":
    interval = int(os.getenv("WORKER_INTERVAL", "10"))
    while True:
        heavy_computation()
        print(f"Sleeping for {interval} seconds ...")
        time.sleep(interval)