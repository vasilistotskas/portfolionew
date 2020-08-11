from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from PIL import Image
from io import BytesIO
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.


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


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images", default="images/placeholder.png")
    body = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)


class SocialImage(models.Model):
    image1 = models.ImageField(null=True, blank=True, upload_to='images')
    image2 = models.ImageField(null=True, blank=True, upload_to='images')
    image3 = models.ImageField(null=True, blank=True, upload_to='images')
    image4 = models.ImageField(null=True, blank=True, upload_to='images')

    def save(self, *args, **kwargs):

        resize_image(self)

        super(SocialImage, self).save(*args, **kwargs)