from django.db import models

# Create your models here.
class Quota(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    socials = models.CharField(max_length=64, blank=False, null=False)
    services = models.CharField(max_length=1000, blank=False, null=False)
    budget = models.CharField(max_length=16, blank=False, null=False)
    details = models.CharField(max_length=255, blank=False, null=False)
    traffic = models.CharField(max_length=255, blank=False, null=False)
    
    class Meta:
        verbose_name_plural = "Quotas"
        
    def save(self, *args, **kwargs):
        self.full_clean()
        
        return super(Quota, self).save(*args, **kwargs)
    
    
class Partner(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    socials = models.CharField(max_length=64, blank=False, null=False)
    stream = models.CharField(max_length=1000, blank=True, null=True, default=None)
    followers = models.CharField(max_length=64, blank=True, null=True, default=None)
    details = models.CharField(max_length=255, blank=False, null=False)
    
    class Meta:
        verbose_name_plural = "Partners"
    
    def save(self, *args, **kwargs):
        self.full_clean()
        
        return super(Partner, self).save(*args, **kwargs)
    
        
    