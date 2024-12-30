import qrcode

from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 5)

qr.add_data("This is a website test.")

qr.make(fit = True)

img = qr.make_image(fill_color = "black", back_color = "blue")

img.save("test_website.png")