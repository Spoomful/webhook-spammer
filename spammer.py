import requests
import time
import json
import argparse
import threading
import concurrent.futures

parser = argparse.ArgumentParser(description="amogus")
parser.add_argument('-w', '--webhook', type=str, required=True, help="Discord webhook you want to spam")
parser.add_argument('-d', '--delay', type=int, required=True, help="The delay")
parser.add_argument('-t', '--threads', type=int, required=True, help="The amount of threads")
args = parser.parse_args()

with open('message.json', 'r') as f:
	messagejson = json.load(f)

delay = args.delay
threads = args.threads

def spam(webhook):
	r = requests.post(webhook, json=messagejson)
	print(f"Status Code: {r.status_code}")
	time.sleep(delay)

while True:
	spammer = concurrent.futures.ThreadPoolExecutor(max_workers=threads)
	spammer.submit(spam, args.webhook)
