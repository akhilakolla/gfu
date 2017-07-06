from django.db import models
from django.utils import timezone;
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    fname = models.CharField(max_length = 100)
    mname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    lname = models.CharField(max_length = 50, null = True, blank = True, default = None)
    is_registered = models.BooleanField(default = False)

@receiver(post_save, sender= User)
def create_user_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 
 
class Agegroup(models.Model):
    #agegroup_id = models.CharField(max_length = 50)
    start_age = models.CharField(max_length = 2)
    end_age = models.CharField(max_length = 2)
    def __str__(self):
        return self.start_age
        

class Personality(models.Model):
    #personality_id = models.CharField(max_length = 50)
    personality = models.CharField(max_length = 50)
    def __str__(self):
        return self.personality

class Occassion(models.Model):
    occassion_type = models.CharField(max_length = 50)
    def __str__(self):
        return self.occassion_type

class Gifts(models.Model):
    giftsid = models.CharField(max_length = 50, null = True, blank = True, default = None)
    qty = models.CharField(max_length = 100, null = True, blank = True, default = None)
    color = models.CharField(max_length = 20, null = True, blank = True, default = None)
    reviews = models.CharField(max_length = 100, null = True, blank = True, default = None)
    imgpath = models.CharField(max_length = 200, null = True, blank = True, default = None)
    imgname = models.CharField(max_length = 100, null = True, blank = True, default = None)
    cost = models.CharField(max_length = 10, null = True, blank = True, default = None)
    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}-{5}-{6}".format(str(self.giftsid), str(self.qty), str(self.color), str(self.reviews), str(self.imgpath), str(self.imgname), str(self.cost))

class Gender(models.Model):
    gender = models.CharField(max_length = 2)
    def __str__(self):
        return self.gender

class Gift_mapping(models.Model):
    fgiftsid = models.CharField(max_length = 50)
    focassid = models.ForeignKey(Occassion, null = True, blank = True, default = None)
    fpersonality = models.ForeignKey(Personality, null = True, blank = True, default = None)
    fage = models.ForeignKey(Agegroup, null = True, blank = True, default = None)
    fgender = models.ForeignKey(Gender, null = True, blank = True, default = None)
    def __str__(self):
        return "{0}-{1}-{2}-{3}-{4}".format(str(self.focassid), str(self.focassid), str(self.fpersonality), str(self.fage), str(self.fgender))

class Quest(models.Model):
    gender = models.CharField(max_length = 1)
    age = models.CharField(max_length = 2)
    personality = models.CharField(max_length = 50)
    
    

 

