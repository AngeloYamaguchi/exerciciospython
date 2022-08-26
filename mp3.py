import mp3play

filename = r'C:\Users\angel\Meus Documentos\pythonProject1cursoemvideo\musica.mp3'


clip = mp3play.load(filename)

clip.play()

import time
time.sleep(min(30, clip.seconds()))
clip.stop()
