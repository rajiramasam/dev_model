from django.db import models

class Patient(models.Model):
    nurse_first_name = models.CharField(max_length=100)
    nurse_last_name = models.CharField(max_length=100)
    patient_first_name = models.CharField(max_length=100)
    patient_last_name = models.CharField(max_length=100)
    health_issue = models.TextField()
    response_to_medication = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
