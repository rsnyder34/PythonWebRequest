#!/usr/bin/python3
import requests
import sys
from time import sleep

url = 

payload = {
    "action": "polls",
    "view" : "process",
    "poll_id": "418",
    "poll_418": "2098",
    "poll_418_nonce": "1bc2cce9dc"
}

def main():
    print('Starting\n')
    votes = 0
    while True:
        sleep(1)
        sys.stdout.flush()
        votes += 1
        r = requests.post(url=url, data=payload)
        print(f"Votes: {votes}",end='\r')


if __name__ == '__main__':
    main()
