from django.db import models

class Register(models.Model):
    register_number = models.CharField(max_length=15, null=True, unique=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    branch = models.CharField(max_length=10, null=True)
    year = models.CharField(max_length=10, null=True)
    concept_to_present = models.CharField(max_length=30, null=True)
    slot_number = models.PositiveIntegerField(null=True, blank=True) 
    evalutor_1=models.IntegerField(null=True)
    evalutor_2=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.register_number}"

    def save(self, *args, **kwargs):
        if not self.slot_number:  # Assign slot number only if it's not already assigned
            # Get the highest existing slot number
            last_slot = Register.objects.all().order_by('-slot_number').first()
            last_slot_number = last_slot.slot_number if last_slot else 0

            # Assign the next available slot number
            self.slot_number = last_slot_number + 1

        super().save(*args, **kwargs)
