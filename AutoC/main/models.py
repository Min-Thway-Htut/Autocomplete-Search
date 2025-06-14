from django.db import models

class FakeAddress(models.Model):
    address = models.TextField()

    def __str__(self):
        return self.address