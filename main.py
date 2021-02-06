import requests
import time

f = open('webhook.txt', 'r')

webhook = f.read()

print(f"Your webhook is: {webhook}")
msg = input('Message: ')
delay = input('Delay: ')

delay = int(delay)

json = {"content": f"@everyone {msg}"}

while True:
	r = requests.post(f"{webhook}", json=json)
	time.sleep(delay)