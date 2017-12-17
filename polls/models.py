from django.db import models

# Create your models here.

class Question(models.Model):
	text = models.CharField(max_length=200)
	created_date = models.DateTimeField('created date')

	def __str__(self):
		return self.text

class Choice(models.Model):
	question = models.ForeignKey(Question)
	text = models.CharField(max_length=200)
	vote = models.IntegerField(default=0)

	def __str__(self):
		return self.text
