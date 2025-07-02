from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/')
    skills = models.ManyToManyField('Skill', blank=True, related_name='projects')

    def __str__(self):
        return self.title
    
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # 0-100 scale
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name='categories')

    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title