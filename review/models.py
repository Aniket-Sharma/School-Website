from django.db import models


class Review(models.Model):
    RATING_CHOICES={(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)}
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review = models.CharField(max_length=1500, null=True, blank=True)

    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=40)
    designation = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    other = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField()
    tel_no = models.BigIntegerField(null=True, blank=True)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.email


class Subscriber(models.Model):
    email = models.EmailField()
