from django.db import models

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    available_slots = models.IntegerField()

    def __str__(self):
        return f"{self.name} with {self.instructor} on {self.datetime}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} booked {self.fitness_class.name}"
