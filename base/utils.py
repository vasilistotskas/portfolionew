from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile


def resize_image_fun(image):
    imageTemporary = Image.open(image)
    outputIoStream = BytesIO()
    imageTemporaryResized = imageTemporary.resize((475, 225))
    imageTemporaryResized = imageTemporaryResized.convert("RGB")
    imageTemporaryResized.save(outputIoStream, format='JPEG', quality=150)
    outputIoStream.seek(0)

    image = InMemoryUploadedFile(outputIoStream, 'ImageField',
                                       "%s.jpg" % image.name.split('.')[0],
                                       'image/jpeg', sys.getsizeof(outputIoStream), None)
    return image


def resize_image(self):
    self.image1 = resize_image_fun(self.image1)
    self.image2 = resize_image_fun(self.image2)
    self.image3 = resize_image_fun(self.image3)
    self.image4 = resize_image_fun(self.image4)