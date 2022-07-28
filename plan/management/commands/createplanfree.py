
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from plan.models import PlanItem


class Command(BaseCommand):
    help = 'creates a 30 day free plan'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--title', type=str, help='title for plan')
        parser.add_argument('-des', '--description', type=str, help='description for plan')
        parser.add_argument('-d', '--duration', type=int, help='duration for free plan')

    def handle(self, *args, **options):
        if options['title'] == None:
            options['title'] = input('title : ')
        if options['description'] == None:
            options['description'] = input('description : ')
        if options['duration'] == None:
            options['duration'] = input('duration (days): ')
        PlanItem.objects.create(
            name = options['title'],
            description =options['description'],
            duration = options['duration'],
            price = 0,
            slug = slugify(options['description']),  
        )
        return 'Free plan created.'
