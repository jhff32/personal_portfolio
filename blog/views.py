from django.shortcuts import render
from .models import Project


def all_blogs(request):
    projects = Project.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'projects': projects})
