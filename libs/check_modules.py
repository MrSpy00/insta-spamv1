# coding=utf-8
#!/usr/bin/env python3

import sys

def check_modules():
    try:
        import requests
    except:
        print("[-] 'requests' adlı paket yüklü değil!")
        print("[*] Yüklemek için 'pip install requests[socks]' yazmalısınız!")
        sys.exit(0)

    try:
        import colorama
    except Exception as e:
        print("[-] 'colorama' adlı paket yüklü değil!")
        print("[*] Yüklemek için 'pip install colorama' yazmalısınız!")
        print(e)
        sys.exit(0)

    try:
        import asyncio
    except:
        print("[-] 'asyncio' adlı paket yüklü değil!")
        print("[*] Yüklemek için 'pip install asyncio' yazmalısınız")
        sys.exit(0)

    try:
        import proxybroker
    except:
        print("[-] 'proxybroker' adlı paket yüklü değil!")
        print("[*] Yüklemek için 'pip install proxybroker' yazmalısınız!")
        sys.exit(0)

    try:
        import warnings
    except:
        print("[-] 'warnings' adlı paket yüklü değil!")
        print("[*] Yüklemek için 'pip install warnings' yazmalısınız!")
        sys.exit(0)

    import warnings
    warnings.filterwarnings("ignore")

    from colorama import init
    init()
