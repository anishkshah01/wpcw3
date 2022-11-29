from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

# Inheriting from AbstractUser
# Account= Users
# Users != Usersss
# Account = Userss
class Account(AbstractUser):
    email=models.EmailField(max_length=100, unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    # USERNAME_FIELD='email'
    # REQUIRED_FIELDS=[]
    # password=models.CharField(max_length=100,default='',null=True)
    pass
    def __str__(self):
        return self.email


# class Account(models.Model):
#     firstName=models.CharField(max_length=100)
#     surname=models.CharField(max_length=100)
#     # Username=mode
#     # Password
#     # Email

class Userr(models.Model):
    # First arg indicates the model,
    '''second arg tells Django if the first one is deleted, delete this one too.
    Last arg prevent orphan data (orphan keyy? Hanging key?) '''
    # primary_key tells Django to use relationship ID as the primary key? Explaination on this?
    accountID=models.OneToOneField(Account,null=True,default='',on_delete=models.CASCADE)
    profileImage=models.ImageField(null=True, blank=True)
    dOB=models.DateTimeField()
    phoneNumber=models.IntegerField()
    # phoneNumber=models.IntegerField(max_length=11)
    addressLine1=models.CharField(max_length=200)
    addressLine2=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    postcode=models.CharField(max_length=200)
    country=models.CharField(max_length=200)

    # What is the string method here?
    # User object in Userr
    def __str__(self):
        return str(self.accountID)



class Item(models.Model):
    # check this:
    user=models.ForeignKey(Userr ,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    startingPrice=models.IntegerField()
    pictureOfItem=models.ImageField()
    startDateTimeItem=models.DateTimeField()
    endDateTimeItem=models.DateTimeField()

    def __str__(self):
        return self.title
        # return u'%s %s' % (self.title,self.description)
    # def get_absolute_url(self):
    #     return reverse('item_detail', args=[str(self.id)])
        

class Bid(models.Model):
    # userFK
    userIDFK=models.OneToOneField(Userr,on_delete=models.CASCADE)
    # ItemFK
    itemIDFK=models.OneToOneField(Item,on_delete=models.CASCADE,)
    bidAmount=models.DecimalField(decimal_places=2,max_digits=10)
    dateTimeBids=models.DateTimeField()
    
    # What is the string?
    def __str__(self):
        return str(self.userIDFK)


class Question(models.Model):
    # User FK:
    userFK=models.ForeignKey(Userr,on_delete=models.CASCADE)
    # Item FK:
    itemFK=models.ForeignKey(Item,on_delete=models.CASCADE)
    questionText=models.TextField()
    # Double check with this field?
    dateTimeOfQuestion=models.DateField()

    def __str__(self):
        return str(self.questionText)

class Answer(models.Model):
    # Question FK:
    questionFK=models.OneToOneField(Question,on_delete=models.CASCADE)
    answerText=models.TextField()
    dateTimeOfAnswer=models.DateField()
    
    def __str__(self):
        return str(self.questionFK)





     

