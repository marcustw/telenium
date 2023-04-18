import sys
import json
import os

from time import sleep
from signal import SIGTERM

if __name__ == "__main__":
    timeout = int(sys.argv[1])
    pids = json.loads(sys.argv[2])
    
    # wait timeout
    sleep(timeout)

    # kill pids
    for pid in pids:
        os.kill(pid, SIGTERM)

