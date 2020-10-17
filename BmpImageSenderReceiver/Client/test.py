from PIL import Image
import io

fd = open(
    '/Users/Han/programming/python-server/BmpImageSenderReceiver/Client/lena.bmp', "rb")
b = bytearray(fd.read())

byte_image = b
image = Image.open(io.BytesIO(byte_image))
image.show()
