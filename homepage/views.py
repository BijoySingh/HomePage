from collections import defaultdict

import markdown
from django.shortcuts import render

from .classes import Page
from .models import Access, Card, Category


def index(request):
    access = Access()
    access.ip = Access.get_client_ip(request)
    access.save()

    cards_map = defaultdict(list)
    cards = Card.objects.all().order_by('-last_updated')
    for card in cards:
        card.description = markdown.markdown(card.description)
        cards_map[card.category.id].append(card)

    pages = list()

    categories = Category.objects.all().order_by('id')
    for category in categories:
        page = Page(id=category.id,
                    title=category.title,
                    description=markdown.markdown(category.description),
                    cards=cards_map[category.id])
        pages.append(page)

    context = {'pages': pages}
    return render(request, 'index.html', context)
