from django.db import models
from django.contrib.auth.models import User,AbstractUser
from app_company.models import Users
class OrderRequest(models.Model):
    productType = models.CharField(max_length=75)
    productbrand = models.CharField(max_length=75)
    productModel = models.CharField(max_length=75)
    productProblemDescription = models.CharField(max_length=200)
    otherProductType = models.CharField(max_length=75)
    userClient = models.ForeignKey(Users, on_delete=models.CASCADE)
    


