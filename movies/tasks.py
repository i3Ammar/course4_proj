from celery import shared_task
from omdb import omdb_integration
from django.core.mail import mail_admins


@shared_task
def search_and_save(search):
    return omdb_integration.search_and_save(search)
@shared_task
def notify_of_new_search(search_term):
     mail_admins("New search term ", f"A new seach term was used : '{search_term}'")




