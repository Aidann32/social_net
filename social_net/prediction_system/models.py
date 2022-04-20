from django.db import models
from profiles.models import Profile
from django.core.validators import MaxValueValidator,MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

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
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    olympiad_participation=models.PositiveIntegerField(choices=YES_NO_VALUES,
        verbose_name="Участие в олимпиадах")
    scholarship=models.PositiveIntegerField(choices=YES_NO_VALUES,
        verbose_name="Наличие хороших оценок")
    school=models.PositiveIntegerField(choices=YES_NO_VALUES,
        verbose_name="Нравится ли ходить в школу/университет")
    fav_sub=models.PositiveIntegerField(choices=SUBJECT_VALUES,
        verbose_name="Любимый предмет")
    projects=models.PositiveIntegerField(choices=YES_NO_VALUES,
        verbose_name="Есть ли научные проекты")
    grasping_power=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)],
        verbose_name='Обучаемость(от 1 до 6)')
    sport_time=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)],
        verbose_name="Времяпровождение над активными занятиями(от 1 до 6)")
    sport_medals=models.PositiveIntegerField(choices=YES_NO_VALUES,
        verbose_name="Наличие медалей по спорту")
    sport_career=models.PositiveIntegerField(choices=YES_NO_VALUES,
        verbose_name='Желание стать спортсменом')
    sport_active=models.PositiveIntegerField(choices=YES_NO_VALUES,
        verbose_name='Постоянны ли занятия спортом')
    fantastic_arts=models.PositiveIntegerField(choices=YES_NO_VALUES,
        verbose_name="Любите ли рисовать")
    won_arts=models.PositiveIntegerField(choices=YES_NO_MAYBE_VALUES,
        verbose_name="Выигрывали ли художественые соревнования")
    time_art=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(6)], 
        verbose_name="Времяпровождение над рисованием(от 1 до 6)")
    prediction=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.profile.user.username

    def save(self,*args,**kwargs):
        ml_model=joblib.load('ml_model/hobby_ml.joblib')
        self.prediction=ml_model.predict([[self.olympiad_participation,self.scholarship,
            self.school,self.fav_sub,self.projects,self.grasping_power,self.sport_time,
            self.sport_medals,self.sport_career,self.sport_active,self.fantastic_arts,
            self.won_arts,self.time_art,]])
        super(ProfileData,self).save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'Данные пользователей'
        verbose_name_plural = 'Данные пользователей'