README.md
# 🐋 OSINT-SEEK-INTELIGENT

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Termux](https://img.shields.io/badge/Termux-Compatible-brightgreen)
![OSINT](https://img.shields.io/badge/OSINT-Suite-orange)
![Python](https://img.shields.io/badge/Python-3.13+-yellow)

**"Buscando inteligencia en el océano de datos"**

</div>

---

## 🌊 Descripción

**OSINT-SEEK-INTELIGENT** es una suite unificada de herramientas OSINT (Open Source Intelligence) diseñada para **Termux**. Integra las mejores herramientas de enumeración, búsqueda y recolección en una sola interfaz con estilo de ballena azul 🐋.

---

## 🚀 Instalación

### En Termux

```bash
# Clonar el repositorio
git clone https://github.com/kukitotelo/Osint-seek-inteligent.git
cd Osint-seek-inteligent

# Instalar dependencias
pkg update && pkg upgrade -y
pkg install python git -y
pip install -r requirements.txt

# Ejecutar
python cli.py
