import image
import qrcode

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

link = input("Enter a link to create QR code ")

qr.add_data(link)
qr.make(fit =True)
img = qr.make_image(fill = 'black', back_color = "white")
img.save("code.png")