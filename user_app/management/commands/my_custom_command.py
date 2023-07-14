from typing import Any, Optional
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone

class Command(BaseCommand):
    help = "Dreate random users"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help="indicates the number of users to be created")

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=get_random_string(5), email='', password='123')

           

    