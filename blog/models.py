from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #user model
from django.urls import reverse


#Model is a class that is in the models module in Django framework...
class Post(models.Model):   # Post inherits from models
	title = models.CharField(max_length=100)  #atributes
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # one to many hece use foriegn key

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self})