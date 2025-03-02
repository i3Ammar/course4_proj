from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SearchTerm
from movies.tasks import notify_of_new_search

@receiver(post_save , sender = SearchTerm , dispatch_uid = 'search_term_saved')
def search_term_saved(sender , instance , created , **kwargs):
    if created :
        notify_of_new_search.delay(instance.term)
