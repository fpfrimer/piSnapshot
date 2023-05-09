from picamera2 import Picamera2
import time

def camera_config(x_resolution, y_resolution):
    """
    Configura a câmera com a resolução desejada e retorna um objeto Picamera2.
    
    Parâmetros:
    x_resolution (int): Resolução horizontal (largura) em pixels.
    y_resolution (int): Resolução vertical (altura) em pixels.
    
    Retorna:
    picam2 (Picamera2): Objeto Picamera2 configurado com a resolução desejada.
    """
    picam2 = Picamera2()

    camera_config = picam2.create_still_configuration({"size": (x_resolution, y_resolution)})
    picam2.configure(camera_config)

    picam2.start()
    time.sleep(2)
    return picam2