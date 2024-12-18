#pip install qrcode
import qrcode as qr
image=qr.make("https://www.linkedin.com/in/mikhileshpatha/") #we can provide any link,text..... but in double quotes
image.save("Linkden.png")  # name of the image to save
