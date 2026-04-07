#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OSINT-SEEK-INTELIGENCE - Suite unificada de OSINT con estilo ballena"""

import os
import sys
import subprocess
from pathlib import Path

# Colores - Azul ballena
B = '\033[94m'
C = '\033[96m'
G = '\033[92m'
R = '\033[91m'
W = '\033[93m'
BL = '\033[38;5;39m'
N = '\033[0m'

def clear():
    os.system('clear')

def whale_banner():
    """ASCII art de ballena estilo DeepSeek"""
    clear()
    print(f"""{BL}
                         ╔══════════════════════════════════════════════════╗
                         ║     🐋  OSINT-SEEK-INTELIGENCE  v2.0  🐋        ║
                         ║     "Buscando inteligencia en el oceano de datos"║
                         ╚══════════════════════════════════════════════════╝{N}
    """)
    print(f"""{C}
                        .-"-.
                       /     \\
                       |     |
                       \.===./
                       (/~~~\)
                        ^^^^
                    {BL}🐋  DEEP WHALE  🐋{C}
                    Buscando... como ballena en el mar{BL}
    """)
    print(f"{N}")

def show_menu():
    print(f"{W}╔════════════════════════════════════════════════════════╗{N}")
    print(f"{W}║      {C}[ MODULOS DISPONIBLES ]{W}                                    ║{N}")
    print(f"{W}╚════════════════════════════════════════════════════════╝{N}\n")
    print(f"{G} 1.{N} 🌊 Enumeracion de Subdominios (Sublist3r)")
    print(f"{G} 2.{N} 🐟 Generador de Google Dorks (M-dork)")
    print(f"{G} 3.{N} 📧 Recoleccion de Emails (theHarvester)")
    print(f"{G} 4.{N} 🎯 OSINT Tools CLI (sentaku - tu herramienta)")
    print(f"{G} 5.{N} ⚡ Escaneo Completo (Ballena modo caza)")
    print(f"{G} 6.{N} 📂 Ver resultados (Lo que encontre)")
    print(f"{G} 7.{N} 🛠️  Instalar/Actualizar dependencias")
    print(f"{G} 8.{N} 🐋 Info de la Ballena")
    print(f"{G} 0.{N} 🚪 Salir del oceano\n")

def run_module(module_name, *args):
    """Ejecuta un modulo desde la carpeta modules"""
    module_path = Path(__file__).parent / "modules" / f"{module_name}.py"
    if module_path.exists():
        print(f"{C}🐋 Lanzando modulo {module_name}...{N}")
        subprocess.run([sys.executable, str(module_path), *args])
    else:
        print(f"{R}[!] Modulo {module_name} no encontrado{N}")
        input("Presiona Enter...")

def full_scan():
    """Ejecuta escaneo completo - La ballena se lanza"""
    domain = input(f"{W}🐋 [>] Dominio objetivo para escaneo completo: {N}")
    print(f"{BL}")
    print("🐋 La ballena se sumerge en el oceano...")
    print("🌊 Buscando subdominios...")
    print("📡 Rastreando señales...")
    print(f"{N}")
    
    print(f"{C}[1/4] Enumerando subdominios...{N}")
    run_module("subdomain_enum", domain)
    
    print(f"{C}[2/4] Recolectando emails...{N}")
    run_module("email_harvest", domain)
    
    print(f"{C}[3/4] Generando dorks...{N}")
    run_module("dork_generator")
    
    print(f"{C}[4/4] Lanzando OSINT Tools CLI...{N}")
    run_module("osint_tools_cli")
    
    print(f"{G}🐋 ¡Caza completada! Revisa output/{N}")

def install_deps():
    """Instala todas las dependencias"""
    print(f"{C}🐋 Instalando herramientas de pesca...{N}")
    
    # Sublist3r
    sublist3r_path = Path.home() / "Sublist3r"
    if not sublist3r_path.exists():
        subprocess.run(["git", "clone", "https://github.com/aboul3la/Sublist3r.git", str(sublist3r_path)])
        req_path = sublist3r_path / "requirements.txt"
        if req_path.exists():
            subprocess.run(["pip", "install", "-r", str(req_path)])
    else:
        print(f"{G}[+] Sublist3r ya instalado{N}")
    
    # theHarvester
    subprocess.run(["pip", "install", "theharvester"])
    
    # Sentaku (para osint-tools-cli)
    subprocess.run(["pip", "install", "sentaku"])
    
    # osint-tools-cli
    osint_path = Path.home() / "osint-tools-cli"
    if not osint_path.exists():
        subprocess.run(["git", "clone", "https://github.com/makikas/osint-tools-cli.git", str(osint_path)])
        print(f"{G}[+] osint-tools-cli clonado{N}")
    else:
        print(f"{G}[+] osint-tools-cli ya existe{N}")
    
    print(f"{G}🐋 Dependencias listas!{N}")
    input("Presiona Enter...")

def whale_info():
    """Informacion sobre la ballena"""
    print(f"{C}")
    print("🐋 OSINT-SEEK-INTELIGENCE")
    print("=" * 40)
    print(f"{W}Version:{N} 2.0.0")
    print(f"{W}Estilo:{N} Ballena Azul (DeepSeek vibes)")
    print(f"{W}Creador:{N} makikas")
    print(f"{W}Mision:{N} Unificar todas tus herramientas OSINT")
    print(f"{W}Integraciones:{N}")
    print("   - Sublist3r (subdominios)")
    print("   - M-dork Pro (Google Dorks)")
    print("   - theHarvester (emails)")
    print("   - osint-tools-cli (tu herramienta con sentaku)")
    print(f"{W}Frase:{N} 'Como ballena en el mar, buscamos datos'")
    print(f"{C}")
    print("    .-'-.")
    print("   /     \\")
    print("   |     |")
    print("   \.===./")
    print("   (/~~~\\)")
    print("    ^^^^")
    print(f"{BL}    🐋  OSINT SEEKER  🐋{N}")
    input("\nPresiona Enter...")

def main():
    # Crear carpetas necesarias
    Path("output").mkdir(exist_ok=True)
    Path("logs").mkdir(exist_ok=True)
    
    while True:
        whale_banner()
        show_menu()
        
        choice = input(f"{BL}🐋 [>] Elige una opcion: {N}").strip()
        
        if choice == "1":
            domain = input(f"{W}🌊 Dominio objetivo: {N}")
            run_module("subdomain_enum", domain)
        elif choice == "2":
            run_module("dork_generator")
        elif choice == "3":
            domain = input(f"{W}📧 Dominio objetivo: {N}")
            run_module("email_harvest", domain)
        elif choice == "4":
            run_module("osint_tools_cli")
        elif choice == "5":
            full_scan()
        elif choice == "6":
            print(f"{C}📂 Resultados guardados:{N}")
            subprocess.run(["ls", "-la", "output"])
            input("\nPresiona Enter...")
        elif choice == "7":
            install_deps()
        elif choice == "8":
            whale_info()
        elif choice == "0":
            print(f"{C}🐋 ¡Hasta luego! La ballena se despide...{N}")
            sys.exit(0)
        else:
            print(f"{R}[!] Opcion invalida{N}")
            input("Presiona Enter...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C}🐋 Ballena interrumpida. Saliendo...{N}")
        sys.exit(0)
