#!/bin/bash
echo "Ingresar contraseña de super usuario(sudo) para esta VM"
pass=$1
sudo apt-get install python3-pip pass
version=$(pip --version)
echo "La version instalada de pip es $version"
pip install pygame
python3 menu.py
