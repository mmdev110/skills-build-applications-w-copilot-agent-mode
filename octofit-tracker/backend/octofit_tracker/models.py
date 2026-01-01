from djongo import models
from bson import ObjectId

class Team(models.Model):
    mongo_id = models.ObjectIdField(unique=True, editable=False, default=ObjectId)
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'
        managed = True
    def __str__(self):
        return self.name

class User(models.Model):
    mongo_id = models.ObjectIdField(unique=True, editable=False, default=ObjectId)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    class Meta:
        db_table = 'users'
        managed = True
    def __str__(self):
        return self.name

class Activity(models.Model):
    mongo_id = models.ObjectIdField(unique=True, editable=False, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    date = models.DateField()
    class Meta:
        db_table = 'activities'
        managed = True

class Workout(models.Model):
    mongo_id = models.ObjectIdField(unique=True, editable=False, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        db_table = 'workouts'
        managed = True

class Leaderboard(models.Model):
    mongo_id = models.ObjectIdField(unique=True, editable=False, default=ObjectId)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
        managed = True
