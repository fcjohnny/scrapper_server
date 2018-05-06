from django.core.management.base import BaseCommand, CommandError
from mgm_scrapper.mgm_scrapper import scrap

class Command(BaseCommand):
  help = 'perform a one time scrap to Mgm website.'

  def handle(self, *args, **options):
    scrap('csv')
    self.stdout.write(self.style.SUCCESS('scrapped and saved to db.'))
