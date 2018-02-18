from django.http import JsonResponse

from main.models import Author


def index(request):
    authors =[]
    for author in Author.objects.all():
        authors.append({
            'first_name': author.first_name,
            'last_name': author.last_name,
            'email': author.email
        })

    return JsonResponse({'authors': authors})
