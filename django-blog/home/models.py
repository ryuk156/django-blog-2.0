from django.db import models
from django.contrib.auth.models import User
class homeintro(models.Model):
    homecontent=models.TextField()
    

class Books(models.Model):
    books=models.TextField()



class userpost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.TextField()
    content=models.TextField()



    def __str__(self):
        return 'post from '+ str(self.user)