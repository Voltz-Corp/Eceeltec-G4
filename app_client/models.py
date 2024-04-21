from django.db import models
#import User
class Order(models.Model):
    productType = models.CharField(max_length=75)
    productbrand = models.CharField(max_length=75)
    productModel = models.CharField(max_length=75)
    prductProblemDescription = models.CharField(max_length=75)
    


