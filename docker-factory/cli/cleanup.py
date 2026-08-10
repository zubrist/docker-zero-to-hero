import os
import glob 
# glob is used to find all the pathnames matching a specified pattern according to the rules
#  used by the Unix shell, although results are returned in arbitrary order.
import sys 
# sys module provides access to some variables used or maintained by the interpreter 
# and to functions that interact strongly with the interpreter.

def cleanup():
    print("Running cleanup task ...")

    log_dir = os.getenv("LOG_DIR", "var/log/app")
    if not os.path.exists(log_dir):
        print(f"Log directory '{log_dir}' does not exist. Skipping cleanup.")
        return

    files = glob.glob(f"{log_dir}/*.log")

    for file in files:
        try:
            os.remove(file)
            print(f"Deleted log file: {file}")
        except Exception as e:
            print(f"Error deleting file {file}: {e}")

    print("Cleanup task completed.")


if __name__ == "__main__":
    cleanup()            