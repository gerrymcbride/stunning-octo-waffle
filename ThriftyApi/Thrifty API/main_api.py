""" Cornice services.
"""
from cornice import Service


main_service = Service(name='hello', path='/', description="Simplest app")


@main_service.get()
def get_info(request):
    """Returns Hello in JSON."""
    return "GET"

@main_service.post()
def post_info(request):
	return "POST"

@main_service.put()
def put_info(request):
	return "PUT"

@main_service.delete()
def delete_info(request):
	return "DELETE"
