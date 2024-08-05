import qrcode 
from PIL import Image
import qrcode.constants 

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr.add_data("https://github.com/harshal4172005")
qr.make(fit=True) # optimize the qrcode size to fit the data
img =  qr.make_image(fill_color="brown",back_color="yellow")
img.save("harshal_git_hub_profile2.jpeg")