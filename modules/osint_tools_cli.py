#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OSINT Tools CLI - Versión estable con sentaku (sin compilar Rust)"""

import subprocess
import os
from pathlib import Path

C = '\033[96m'
G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
N = '\033[0m'

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"{C}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║     🗺️  OSINT TOOLS CLI (Sentaku Edition)  🗺️           ║")
    print("║     " + "Navegación por categorías OSINT".center(44) + "║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(f"{N}")

def run():
    sentaku_bin = Path.home() / "osint-tools-cli/sentaku/bin/sentaku"
    
    if not sentaku_bin.exists():
        print(f"{R}[!] sentaku no encontrado{N}")
        print(f"{Y}[*] Buscando en: {sentaku_bin}{N}")
        return
    
    # Categorías principales del TOC original
    categorias = """MAPS_GEOLOCATION_AND_TRANSPORT
SOCIAL_MEDIA
DOMAIN_IP_LINKS
IMAGE_SEARCH_AND_IDENTIFICATION
CRYPTOCURRENCIES
MESSENGERS
CODE
SEARCH_ENGINES
TOOLS_FOR_DUCKDUCKGO
TOOLS_FOR_GOOGLE
IOT
ARCHIVES
ARCHIVES_OF_DOCUMENTS
DATASETS
PASSWORDS_EMAILS_PHONE_NUMBERS
PEOPLE_SEARCH
SOCK_PUPPETS
NOOSINT_TOOLS
TOOLS_COLLECTIONS
FILES
NFT
IMEI_AND_SERIAL_NUMBERS
KEYWORDS_TRENDS_NEWS_ANALYTICS
APPS_AND_PROGRAMS
BRANDS_COMPANIES_ITEMS
MOVIES
TV_RADIO
VIRTUALMACHINES_LINUX_DISTRIBUTIONS
MY_PROJECTS"""
    
    banner()
    print(f"{G}🐋 Cargando menú OSINT...{N}\n")
    
    # Ejecutar sentaku con las categorías
    subprocess.run(f"echo '{categorias}' | {sentaku_bin}", shell=True)
    
    input(f"\n{G}[+] Presiona Enter para volver...{N}")

if __name__ == "__main__":
    run()
