from django.db import models


# Create your models here.


class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default='', blank=False, null=False)
    course_number = models.IntegerField(default='', blank=False, null=False)
    instructor_name = models.CharField(max_length=60, default='', blank=False, null=False)
    duration = models.DurationField(max_length=5, default='', blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title



