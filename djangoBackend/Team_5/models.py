from djongo import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Add the import for GridFSStorage
from djongo.storage import GridFSStorage

# Define your GrifFSStorage instance
grid_fs_storage = GridFSStorage(collection='myfiles', base_url=''.join([settings.ROOT_URLCONF, 'myfiles/']))


# Create your models here.

class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    zipcode = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='userphoto', blank=True, storage=grid_fs_storage)
    photo_1 = models.ImageField(upload_to='userphoto', blank=True, storage=grid_fs_storage)
    photo_2 = models.ImageField(upload_to='userphoto', blank=True, storage=grid_fs_storage)
    photo_3 = models.ImageField(upload_to='userphoto', blank=True, storage=grid_fs_storage)
    photo_4 = models.ImageField(upload_to='userphoto', blank=True, storage=grid_fs_storage)
    photo_5 = models.ImageField(upload_to='userphoto', blank=True, storage=grid_fs_storage)
    photo_6 = models.ImageField(upload_to='userphoto', blank=True, storage=grid_fs_storage)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title, self.address1, self.zipcode

    def values(self):
        return self.title, self.address1


class CustomUser(AbstractUser):
    pass
    user_type = models.CharField(max_length=200)
    favorites = models.ManyToManyField(Listing, related_name="favorited_by")

    def __str__(self):
        return self.username

    def get_user_type(self):
        return self.user_type
