from django.db import models
from profiles.models import Profile
from django.core.validators import MaxValueValidator,MinValueValidator
YES_NO_VALUES=(
    (0,'Нет'),
    (1,'Да'),
)
YES_NO_MAYBE_VALUES=(
    (0,'Нет'),
    (1,'Да'),
    (2,'Возможно')
)

SUBJECT_VALUES=(
    (1,'Математика'),
    (2,'Любая другая точная наука'),
    (3,'История/География'),
    (4,'Любой язык'),
)


class ProfileData(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    olympiad_participation=models.PositiveIntegerField(choices=YES_NO_VALUES)
    scholarship=models.PositiveIntegerField(choices=YES_NO_VALUES)
    school=models.PositiveIntegerField(choices=YES_NO_VALUES)
    fav_sub=models.PositiveIntegerField(choices=SUBJECT_VALUES)
    projects=models.PositiveIntegerField(choices=YES_NO_VALUES)
    grasping_power=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)])
    sport_time=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)])
    sport_medals=models.PositiveIntegerField(choices=YES_NO_VALUES)
    sport_career=models.PositiveIntegerField(choices=YES_NO_VALUES)
    sport_active=models.PositiveIntegerField(choices=YES_NO_VALUES)
    fantastic_arts=models.PositiveIntegerField(choices=YES_NO_VALUES)
    won_arts=models.PositiveIntegerField(choices=YES_NO_MAYBE_VALUES)
    time_art=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)])
    prediction=models.CharField(max_length=200,blank=True)