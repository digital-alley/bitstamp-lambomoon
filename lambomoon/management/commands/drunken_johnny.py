from django.core import management
from django.conf import settings
import time


class Command(management.BaseCommand):
    """
    DrunkenJohnny is one of our many bots. It takes care for
    earning money to people while they're having beer.
    """
    help = 'Usage example: python manage.py drunken_johnny'

    def handle(self, *args, **options):
        print('Using ApiKey: {0}, ApiSecret: {1} for ClienId: {2}', settings.API_KEY,
              settings.API_SECRET, settings.CLIENT_ID)
        while True:
            print('[*] Drunken johnny is working ...')
            time.sleep(3)
