from django.db import models

# Create your models here.

class ProgrammingLanguage(models.Model):

    LEARNING_MODE_CHOICES = (
        ("Self Taught", "Self Taught"),
        ("Boot Camp", "Boot Camp"), 
        ("College", "College"),
    )

    COMMENDATIONS_CHOICES = (
        ("Star 1", "Star 1"),
        ("Star 2", "Star 2"),
        ("Star 3", "Star 3"),
        ("Star 4", "Star 4"),
        ("Star 5", "Star 5"),
        ("Star 6", "Star 6"),
        ("Star 7", "Star 7"),

    )

    LEVEL_CHOICES = (
        ("Master", "Master"),
        ("Expert", "Expert"),
        ("Intermediate", "Intermediate"),
        ("Junior", "Junior"), 
        ("Beginner", "Beginner")
    )

    name = models.CharField(max_length=100)
    favourite_framework = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    learning_mode = models.CharField(max_length=100, choices=LEARNING_MODE_CHOICES)
    number_of_Projects = models.IntegerField()
    current_level = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    commendations = models.CharField(max_length=100, choices=COMMENDATIONS_CHOICES)

    def __str__(self):
        return self.name

