from django.db import models


# Create your models here.
class Language(models.Model):
    title = models.CharField(max_length=30)


class User(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    mother_tongue = models.CharField(max_length=30)
    target_tongues = models.ManyToManyField(Language)
    leader_board_score = models.IntegerField()


class Answer(models.Model):
    text = models.CharField(max_length=300)
    user_id = models.ManyToManyField(User)


class Question(models.Model):
    text = models.CharField(max_length=300)
    answers = models.ManyToManyField(Answer)
    correct_answer = models.IntegerField()


class Round(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)


class Game(models.Model):
    user_list = models.ManyToManyField(User)
    rounds = models.ForeignKey(Round, on_delete=models.CASCADE)
    score_list = models.CharField(max_length=300)



