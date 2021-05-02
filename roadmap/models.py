from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError

User = settings.AUTH_USER_MODEL


def validate_deadline_not_in_past(value):
    current = timezone.now()
    if value <= current:
        raise ValidationError('Deadline should be in future date.')


class Goal(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='created')
    deadline = models.DateField(validators=[validate_deadline_not_in_past])
    created = models.DateTimeField(auto_now_add=True)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

