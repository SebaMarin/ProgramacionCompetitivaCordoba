from django.db import models

# Create your models here.

class Problem(models.Model):
    problem_name=models.CharField(max_length=128)
    problem_url=models.URLField()
    problem_tags=models.ManyToManyField('Tag')
    def __str__(self):
        return self.problem_name

class Tag(models.Model):
    tag_name=models.CharField(max_length=128,unique=True)
    def __str__(self):
        return self.tag_name

