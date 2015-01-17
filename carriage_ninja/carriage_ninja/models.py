from django.contrib.gis.db import models
from django.contrib.auth.models import User

from localflavor.us.models import USStateField

from cities.models import PostalCode


class Address(models.Model):
    ''' https://docs.djangoproject.com/en/1.7/ref/contrib/gis/model-api/
    '''
    num = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.ForeignKey(PostalCode)
    objects = models.GeoManager()


class DriversLicense(models.Model):
    """ A driver's license
    """

    user = models.ForeignKey(User)
    pic_front = models.ImageField()
    pic_back = models.ImageField()
    state = USStateField()
    number = models.CharField(max_length=255)
    validated = models.BooleanField(default=False)


class Trip(models.Model):
    """ A trip being taken
    """

    carrier = models.ForeignKey(User)
    departure_zip = models.ForeignKey(PostalCode, related_name='departure_postal_code')
    departure_date = models.DateTimeField()
    arrival_zip = models.ForeignKey(PostalCode, related_name='arrival_postal_code')
    arrival_date = models.DateTimeField()
