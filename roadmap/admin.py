from django.contrib import admin

from .models import Goal, Task


class TaskInlined(admin.StackedInline):
    model = Task
    extra = 1


class GoalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'deadline']
    list_filter = ['deadline']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [TaskInlined]


admin.site.register(Goal, GoalAdmin)
