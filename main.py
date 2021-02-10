import requests
import time
import os
import threading
import concurrent.futures

f = open('webhook.txt', 'r')

webhook = f.read()

print(f"Your webhook is: {webhook}")
msg = input('Message: ')
delay = input('Delay: ')
threads = input('Threads: ')
delay = int(delay)
threads = int(threads)
json = {"content": f"@everyone {msg}"}

def spam():
	r = requests.post(f"{webhook}", json=json)
	time.sleep(delay)

while True:
	spammer = concurrent.futures.ThreadPoolExecutor(max_workers=threads)
	spammer.submit(spam)
