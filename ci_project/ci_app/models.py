from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=255)
    script = models.TextField()
    host = models.CharField(max_length=255)

    def __str__(self):
        return self.name