from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team='marvel'),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team='marvel'),
            User.objects.create(name='Batman', email='batman@dc.com', team='dc'),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team='dc'),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=users[1], type='cycle', duration=45, date='2023-01-02')
        Activity.objects.create(user=users[2], type='swim', duration=25, date='2023-01-03')
        Activity.objects.create(user=users[3], type='yoga', duration=60, date='2023-01-04')

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do situps', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
