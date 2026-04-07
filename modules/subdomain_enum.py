#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Modulo de enumeracion de subdominios usando Sublist3r"""

import subprocess
import sys
import os

def run(domain):
    print(f"[*] Enumerando subdominios para: {domain}")
    sublist3r_path = os.path.expanduser("~/Sublist3r/sublist3r.py")
    
    if not os.path.exists(sublist3r_path):
        print("[!] Sublist3r no encontrado en ~/Sublist3r")
        print("[*] Instalando Sublist3r...")
        subprocess.run(["git", "clone", "https://github.com/aboul3la/Sublist3r.git", 
                       os.path.expanduser("~/Sublist3r")])
        subprocess.run(["pip", "install", "-r", os.path.expanduser("~/Sublist3r/requirements.txt")])
    
    output_file = f"output/subdomains_{domain}.txt"
    cmd = f"python {sublist3r_path} -d {domain} -o {output_file}"
    
    try:
        subprocess.run(cmd, shell=True)
        print(f"[+] Resultados guardados en: {output_file}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        print("Uso: python subdomain_enum.py <dominio>")
