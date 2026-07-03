from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)

    logo = models.ImageField(
        upload_to="company/",
        blank=True,
        null=True,
    )

    gst_number = models.CharField(
        max_length=20,
        blank=True,
    )

    pan_number = models.CharField(
        max_length=20,
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
    )

    email = models.EmailField(
        blank=True,
    )

    website = models.URLField(
        blank=True,
    )

    address = models.TextField()

    bank_name = models.CharField(
        max_length=100,
        blank=True,
    )

    account_number = models.CharField(
        max_length=50,
        blank=True,
    )

    ifsc_code = models.CharField(
        max_length=20,
        blank=True,
    )

    def __str__(self):
        return self.name