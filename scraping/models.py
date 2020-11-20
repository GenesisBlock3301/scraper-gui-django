from django.db import models


class UrlStore(models.Model):
    url = models.CharField(max_length=3000)

    def __str__(self):
        return self.url[:50]+".."

