from utils.common import *


running = True
while running:
    userInput = input("enter the ipv6 address with its prefix >>> ").strip()

    ipwithprefix = userInput.split("/")
    ip = ipwithprefix[0]
    pref = int(ipwithprefix[1])

    try:
        validate(ip, pref)
        abbr = abbreviate(ip)
        print(f"{abbr}/{pref}")

    except ValueError as err:
        print(err)
