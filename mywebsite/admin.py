from django.contrib import admin
from .models import Project, Skill, BlogPost, SkillCategory

# Register your models here.

admin.site.register(Project)
admin.site.register(Skill)  
admin.site.register(BlogPost)
admin.site.register(SkillCategory)