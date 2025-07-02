from django.shortcuts import render
from .models import Project, Skill, BlogPost, SkillCategory

# Create your views here.

def home(request):
    skill_categories_with_skills = [
        {
            'name': category.name,
            'description': category.description,
            'skills': list(category.skills.all())
        }
        for category in SkillCategory.objects.all()
    ]

    context = {
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'skill_categories_with_skills': skill_categories_with_skills,
        # Adding latest 3 blog posts if needed:
        # 'latest_blog_posts': BlogPost.objects.order_by('-created_at')[:3],
    }
    return render(request, 'mywebsite/home.html', context)
