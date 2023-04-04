import requests

http = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http%22")
socks4 = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4%22")
socks5 = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5%22")
all = ("https://api.proxyscrape.com/v2/?request=getproxies&protocol=all%22")

choice = input("Http, Socks4, Socks5, All: ")

if choice == "http":
    r = requests.get(http)
    filename = "http.txt"
elif choice == "socks4":
    r = requests.get(socks4)
    filename = "socks4.txt"
elif choice == "socks5":
    r = requests.get(socks5)
    filename = "socks5.txt"
elif choice == "all":
    r = requests.get(socks5)
    filename = "all.txt"
else:
    print("Not Valid Choice")
    exit()

with open(filename, "a+") as y:
    y.write(r.text)

open3 = []
with open(filename, "r") as y:
    for proxy in y.readlines():
        if len(proxy) > 5:
            open3.append(proxy)
    y.close()

with open(filename, "w") as y:
    y.write("".join(open3))

print("Done!")
