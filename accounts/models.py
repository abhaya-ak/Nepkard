from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError('The PIN code must be exactly 6 digits.')


STATE_CHOICE = (
    ('Tikapur', 'Tikapur'),
    ('Dhangadi', 'Dhangadi'),
    ('Kathmandu', 'Kathmandu'),
)
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    ) # added a one to one relation to map registration table of user

    name = models.CharField(max_length=100)
    dob = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    pin = models.PositiveIntegerField(
        validators=[validate_pin_length],
        help_text='Enter 6-digit pin code'
    )

    state = models.CharField(choices=STATE_CHOICE, max_length=100)

    mobile = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Enter a valid 10-digit mobile number'
            )
        ]
    )

    job_city = models.CharField(max_length=50)

    profile_image = models.ImageField(upload_to='profileimg/', blank=True, null=True)
    my_file = models.FileField(upload_to='doc/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"