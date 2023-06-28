from django.db import models

# Create your models here.

class AppPackage(models.Model):
    """
    This Model Store the Package Name
    """
    package_name=models.CharField(max_length=100)

    def __str__(self):
        return f'{id}-{self.package_name}'

class AppDetails(models.Model):
    """
    This Model Store the App Details
    """
    app_package = models.ForeignKey(AppPackage,on_delete=models.CASCADE ,related_name='app_package')
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    developerAddress = models.TextField(null=True,blank=True)
    summary = models.TextField(null=True,blank=True)
    installs = models.CharField(max_length=100,null=True,blank=True)
    install_count = models.IntegerField(null=True,blank=True)
    score = models.FloatField(null=True,blank=True)
    ratings = models.IntegerField(null=True,blank=True)
    reviews = models.CharField(max_length=100,null=True,blank=True)
    developerId = models.CharField(max_length=100,null=True,blank=True)
    version = models.CharField(max_length=100,null=True,blank=True)
    video= models.URLField(null=True,blank=True)
    icon= models.URLField(null=True,blank=True)
    developerWebsite= models.URLField(null=True,blank=True)
    privacyPolicy= models.URLField(null=True,blank=True)
    genre= models.CharField(max_length=100,null=True,blank=True)
    developer= models.CharField(max_length=100,null=True,blank=True)
    free= models.BooleanField(default=True)
    price= models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title

class AppComments(models.Model):
    """
    This Model Store the Comments of particular App Details
    """
    app_details = models.ForeignKey(AppDetails, on_delete=models.CASCADE,related_name='app_details')
    comments = models.TextField()

    def __str__(self):
        return self.app_details.title
