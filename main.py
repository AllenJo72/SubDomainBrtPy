import requests
import socket

domain = input("Website Link/Domain: ")
print("[+]Domain Ip Address: " + socket.gethostbyname(domain))
file = open('sublist.txt')
content = file.read()
subdomains = content.splitlines()
for subdomain in subdomains:
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[+] Found Subdomain: ", url)
