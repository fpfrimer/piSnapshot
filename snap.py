#!/usr/bin/env python

import sys
import os
from utils import camera_config
from datetime import datetime

def is_valid_resolution(value):
    return value.isdigit() and 250 <= int(value) <= 2000

if __name__ == "__main__":

    now = datetime.now()
    current_time = now.strftime("%d%m%Y_%H%M%S")
    filename = f'~/imagens/foto_{current_time}.bmp'
    width = height = 256

    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        if is_valid_resolution(sys.argv[2]):
            width = height = int(sys.argv[2])
        else:
            print("A resolução informada é inválida. Usando a resolução padrão (256x256).")
    else:
        filename = sys.argv[1]
        if is_valid_resolution(sys.argv[2]) and is_valid_resolution(sys.argv[3]):
            width = int(sys.argv[2])
            height = int(sys.argv[3])
        else:
            print("As resoluções informadas são inválidas. Usando a resolução padrão (256x256).")
    filename = os.path.expanduser(filename)

    # Verificar e criar o caminho da pasta, se necessário
    folder_path = os.path.dirname(filename)
    if folder_path and not os.path.exists(folder_path):
        os.makedirs(folder_path)

    picam2 = camera_config(width, height)
    picam2.capture_file(filename)
    print(f"Imagem capturada e salva como {filename}")

