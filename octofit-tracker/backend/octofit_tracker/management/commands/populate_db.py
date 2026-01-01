from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (use Django FK)
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Heavy lifting and resistance', suggested_for='Marvel')
        w2 = Workout.objects.create(name='Flight Training', description='Aerobic and agility', suggested_for='DC')

        # Create Activities (use Django FK)
        today = timezone.now().date()
        Activity.objects.create(user=tony, type='Running', duration=30, date=today)
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=today)
        Activity.objects.create(user=bruce, type='Martial Arts', duration=60, date=today)
        Activity.objects.create(user=clark, type='Flying', duration=50, date=today)

        # Create Leaderboard (use Django FK)
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=98)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
