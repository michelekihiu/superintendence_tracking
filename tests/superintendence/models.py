from __future__ import unicode_literals
import random
import string

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

"""
@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Book(models.Model):
    name = models.CharField('Book name', max_length=100)
    author = models.ForeignKey(Author, blank=True, null=True)
    author_email = models.EmailField('Author email', max_length=75, blank=True)
    imported = models.BooleanField(default=False)
    published = models.DateField('Published', blank=True, null=True)
    published_time = models.TimeField('Time published', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True,
                                blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name
"""

@python_2_unicode_compatible
class Shipment(models.Model):
    vessel = models.CharField(max_length=200)
    ata_eta_mom = models.DateField()
    ocean_del_terms = models.CharField(max_length=10, null=True, blank=True)
    bl_teu = models.IntegerField(null=True, blank=True)
    bl_feu = models.IntegerField(null=True, blank=True)
    cf_agent = models.CharField(max_length=20, null=True, blank=True)
    bl_number = models.CharField(max_length=50, null=True, blank=True)
    tonnage = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    ex_si_number_po_number = models.CharField(max_length=500, null=True, blank=True)
    commodity = models.CharField(max_length=50, null=True, blank=True)
    pack = models.CharField(max_length=10, null=True, blank=True)
    recipient_country = models.CharField(max_length=20, null=True, blank=True)
    project_type = models.CharField(max_length=20, null=True, blank=True)
    po_number = models.CharField(max_length=20, null=True, blank=True)
    ses_number = models.CharField(max_length=20, null=True, blank=True)
    sgs_amount = models.IntegerField(null=True, blank=True)



    def __str__(self):
        return self.vessel

"""
@python_2_unicode_compatible
class Parent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Child(models.Model):
    parent = models.ForeignKey(Parent)
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s - child of %s' % (self.name, self.parent.name)
"""

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    is_private = models.BooleanField(default=True)


class Entry(models.Model):
    user = models.ForeignKey('auth.User')


class WithDefault(models.Model):
    name = models.CharField('Default', max_length=75, blank=True,
                            default='foo_bar')

def random_name():
    chars = string.ascii_lowercase
    return ''.join(random.SystemRandom().choice(chars) for _ in range(100))

class WithDynamicDefault(models.Model):

    name = models.CharField('Dyn Default', max_length=100,
            default=random_name)


class WithFloatField(models.Model):
    f = models.FloatField(blank=True, null=True)
