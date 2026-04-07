#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Modulo de generacion de Google Dorks"""

import os
import sys
import time
import subprocess

G = '\033[92m'
R = '\033[91m'
C = '\033[96m'
W = '\033[93m'
N = '\033[0m'

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"""{C}
    ╔═══════════════════════════════════════════════╗
    ║     🎯 GENERADOR DE GOOGLE DORKS              ║
    ╚═══════════════════════════════════════════════╝{N}
    """)

def generar_dorks(cat, dominio):
    dorks = {
        '1': [
            f'intitle:"index of" "parent directory" {dominio}',
            f'site:{dominio} intitle:"index of" /backup',
            f'site:{dominio} intitle:"index of" /admin'
        ],
        '2': [
            f'filetype:log inurl:password {dominio}',
            f'"username" "password" filetype:xls {dominio}',
            f'filetype:env DB_PASSWORD {dominio}'
        ],
        '3': [
            f'filetype:xls "email" "@gmail.com" {dominio}',
            f'intitle:"contact" "@" {dominio}'
        ],
        '4': [
            f'filetype:sql "CREATE TABLE" {dominio}',
            f'inurl:phpmyadmin {dominio}'
        ],
        '5': [
            f'filetype:pdf "confidencial" {dominio}',
            f'filetype:doc "interno" {dominio}'
        ],
        '6': [
            'intitle:"Live View" -inurl:youtube.com',
            '"Hikvision" inurl:login'
        ],
        '7': [
            f'site:{dominio} intitle:admin',
            f'site:{dominio} inurl:login'
        ]
    }
    return dorks.get(cat, [])

def main():
    while True:
        banner()
        print(f"{W}Categorias:{N}\n")
        print(f"{G}1.{N} Directorios sensibles")
        print(f"{G}2.{N} Archivos con contrasenas")
        print(f"{G}3.{N} Correos electronicos")
        print(f"{G}4.{N} Bases de datos SQL")
        print(f"{G}5.{N} Documentos PDF/DOC")
        print(f"{G}6.{N} Camaras IoT")
        print(f"{G}7.{N} Paneles de admin")
        print(f"{G}0.{N} Salir\n")
        
        opcion = input(f"{C}[>] Opcion: {N}").strip()
        if opcion == '0':
            break
        if opcion not in ['1','2','3','4','5','6','7']:
            print(f"{R}[!] Opcion invalida{N}")
            time.sleep(1)
            continue
        
        dominio = input(f"{W}[?] Dominio (opcional): {N}").strip()
        dorks = generar_dorks(opcion, dominio)
        
        print(f"\n{G}[+] Dorks generados:{N}\n")
        for i, dork in enumerate(dorks, 1):
            print(f"{C}{i}.{N} {dork}")
        
        guardar = input(f"\n{W}[?] Guardar en archivo? (s/n): {N}").lower()
        if guardar == 's':
            nombre = input("Nombre del archivo: ").strip() or "dorks"
            with open(f"output/{nombre}.txt", "w") as f:
                for dork in dorks:
                    f.write(dork + "\n")
            print(f"{G}[+] Guardado en output/{nombre}.txt{N}")
        
        input(f"\n{G}[>] Enter para continuar...{N}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Saliendo...{N}")
