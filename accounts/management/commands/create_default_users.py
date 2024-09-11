# accounts/management/commands/create_default_users.py
import random
import string
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Account

class Command(BaseCommand):
    help = 'Create 10 default users with a balance of 500,000 and unique IDs'

    def generate_unique_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def handle(self, *args, **options):
        sample_names = [
            'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Fay', 'George', 'Hannah', 'Ivy', 'Jack'
        ]

        for i in range(1, 11):
            username = f'user{i}'
            password = 'password123'
            email = f'{username}@example.com'
            full_name = random.choice(sample_names) + f' {i}'

            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=full_name.split()[0],
                last_name=full_name.split()[1]
            )

            # Generate a unique ID
            unique_id = self.generate_unique_id()

            # Create associated account with balance and unique ID
            Account.objects.create(
                user=user,
                balance=500000,  # Set the balance to 500,000
                unique_id=unique_id
            )

            self.stdout.write(self.style.SUCCESS(f'User {username} created with ID {user.id}, unique ID {unique_id}, and balance 500,000'))
