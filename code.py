import image
import qrcode

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

link = "https://www.google.com/search?sca_esv=602071010&rlz=1C1CHBF_enUS1057US1063&sxsrf=ACQVn0--gZshRV3WKut_wD6EO1krZEE0ig:1706407642391&q=funny+memes&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjakvfq__6DAxV8v4kEHeMVDj4Q0pQJegQIDBAB&biw=1536&bih=738&dpr=1.25#imgrc=ia9zCZwnqGjP6M"

qr.add_data(link)
qr.make(fit =True)
img = qr.make_image(fill = 'green', back_color = "white")
img.save("code1.png")