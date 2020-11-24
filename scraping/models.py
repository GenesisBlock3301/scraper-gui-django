from django.db import models


class Trust(models.Model):
    url = models.CharField(max_length=3000,primary_key=True)

    def __str__(self):
        return self.url

class Facebook(models.Model):
    url = models.CharField(max_length=3000,primary_key=True)

    def __str__(self):
        return self.url

class Youtube(models.Model):
    url = models.CharField(max_length=3000,primary_key=True)

    def __str__(self):
        return self.url

class FeeFO(models.Model):
    url = models.CharField(max_length=3000,primary_key=True)

    def __str__(self):
        return self.url

class GOOGLE(models.Model):
    url = models.CharField(max_length=3000,primary_key=True)

    def __str__(self):
        return self.url






