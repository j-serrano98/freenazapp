from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class PlanChoices(models.TextChoices):
        FREE = "FREE", "Free"
        PREMIUM = "PREMIUM", "Premium"
        BUSINESS = "BUSINESS", "Business"

    base_role = PlanChoices.FREE

    plan = models.CharField(max_length=10, choices=PlanChoices.choices, default=PlanChoices.FREE)
    email_verified = models.BooleanField(default=False)

    def is_premium(self):
        return self.plan in [self.PlanChoices.PREMIUM, self.PlanChoices.BUSINESS]
    
    def __str__(self):
        return self.username