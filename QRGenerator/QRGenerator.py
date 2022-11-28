#pip install pyqrcode
#pip install pypng
import pyqrcode
import png
link = "https://drive.google.com/file/d/1TIOovmaMGl0QoTJJtuXaMasdGjHTuJ5F/view?usp=share_link"
shortLink = "https://tinyurl.com/2k56hn3s"
qr_code = pyqrcode.create(shortLink)
qr_code.png("FacundoRomeroSosaResume.png", scale=5)