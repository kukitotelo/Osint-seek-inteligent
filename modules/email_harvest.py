#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Modulo de recoleccion de emails usando theHarvester"""

import subprocess
import sys

def run(domain):
    print(f"[*] Recolectando emails para: {domain}")
    try:
        subprocess.run(["theharvester", "-d", domain, "-b", "bing,duckduckgo", "-l", "300"])
    except FileNotFoundError:
        print("[!] theHarvester no instalado")
        print("[*] Instalando con: pip install theharvester")
        subprocess.run(["pip", "install", "theharvester"])
        subprocess.run(["theharvester", "-d", domain, "-b", "bing,duckduckgo"])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        print("Uso: python email_harvest.py <dominio>")
