from django.shortcuts import render, redirect, get_object_or_404, reverse

from .models import Goal, Task
from .forms import GoalForm, TaskForm


def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'roadmap/goal_list.html', {'goals': goals})


def goal_detail(request, slug):
    goal = get_object_or_404(Goal, slug=slug)
    return render(request, 'roadmap/goal_detail.html', {'goal': goal})


def goal_add(request):
    form = GoalForm()
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.creator = request.user
            goal.save()
            return redirect('goal_list')
    return render(request, 'roadmap/goal_add.html', {'form': form})


def goal_edit(request, slug):
    goal = get_object_or_404(Goal, slug=slug)
    form = GoalForm(instance=goal)

    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goal_list')
    return render(request, 'roadmap/goal_edit.html', {'form': form, 'goal': goal})


def goal_delete(request, slug):
    goal = get_object_or_404(Goal, slug=slug)
    goal.delete()
    return redirect('goal_list')


def task_add(request, slug):
    goal = get_object_or_404(Goal, slug=slug)
    form = TaskForm

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.goal = goal
            task.save()
            return redirect(reverse('goal_detail', args=[goal.slug]))
    return render(request, 'roadmap/task_add.html', {'form': form, 'goal': goal})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    goal_slug = task.goal.slug
    task.delete()
    return redirect(reverse('goal_detail', args=[goal_slug]))
