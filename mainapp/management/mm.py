from django.core.management import BaseCommand
from django.core.management import call_command



class Command(BaseCommand):

    help = (
        "This command using for call makemessages with using flags --locale, --ignore and --no-location"
    )

    def handle(self, *args, **options):
        call_command('makemessages','--locale=ru','--ignore=env','--no-location')