import qrcode

url = input("Enter the URL: ")
file_path = "C:\\Users\\mohdw\\OneDrive\\Desktop\\desktop\\python\\Projects\\QRcodeMaker\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)


# this is stylish QR maker
'''
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

url = input("Enter the URL: ")

file_path = "C:\\Users\\mohdw\\OneDrive\\Desktop\\desktop\\python\\Projects\\QRcodeMaker\\styled_qr.png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=2,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=RadialGradiantColorMask(
        center_color=(145, 60, 255),  # Purple
        edge_color=(30, 144, 255),    # Blue
    )
)

img.save(file_path)
print("Stylish Gradient QR Code created!")


'''