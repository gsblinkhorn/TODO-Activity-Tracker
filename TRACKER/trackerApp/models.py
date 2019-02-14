from django.db import models

class List(models.Model):
    activity = models.CharField(max_length=200)
    subject = models.CharField(max_length=25, null=True)
    isCompleted = models.BooleanField(default=False)
    date = models.DateField(null=True)
    
    def __str__(self):
        return self.activity + ' | ' + self.subject + ' | ' + str(self.date) + ' | ' + str(self.isCompleted)



