from django.shortcuts import render

from .models import Goal


def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'roadmap/goal_list.html', {'goals': goals})
