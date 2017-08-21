# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        # check all fields for emptyness
        for field, value in post_data.iteritems():
#             if value and field != "csrfmiddlewaretoken":
#                 errors[field] = "{} field is required".format(field.replace('_', ' '))

            # check name fields for min length
            if field == "course_name":
                if not field in errors and len(value) < 6:
                    errors[field] = "{} field must bet more than 5 characters".format(field.replace('_', ' '))
            elif field == "description":
                if not field in errors and len(value) < 16:
                    errors[field] = "{} field must bet more than 15 characters".format(field.replace('_', ' '))
        
        return errors

class Description(models.Model):
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    def __repr__(self):
        return "<Description object - desc: {}".format(self.desc)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE, related_name="course")
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    objects = CourseManager()
    def __repr__(self):
        return "<Course object - name: {}; description: {}".format(self.name, self.description.desc)
