#install qrcode and import 
import qrcode

#giving source and save file name 
url=""
file="qrcode.png"

#defining its look 
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L ,
    border=2,
    box_size=15
)
a=input("which color you want in your fill side on qrcode:")
b=input("which color you want in your back side on qrcode:")

#
qr.add_data(url)
qr.make(fit=True)

#color of fill and back and save 
img=qr.make_image(fill_color=a,back_color=b)
img.save(f"python projects/{file}")
print(f"qrcode generated seccessfully of file name {file}")
