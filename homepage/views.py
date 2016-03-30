from collections import defaultdict

import markdown
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from htmlmin.decorators import minified_response

from .classes import Page
from .models import AccessCount, Card, Category, Reviews, ReviewCategory, Blog, BlogCategory


@minified_response
@cache_page(60 * 60)
def index(request):
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

    reviews_map = defaultdict(list)
    reviews = Reviews.objects.all().order_by('-score')
    for review in reviews:
        review.description = markdown.markdown(review.description)
        reviews_map[review.category.id].append(review)

    review_pages = list()
    categories = ReviewCategory.objects.all().order_by('id')
    for category in categories:
        page = Page(id=category.id,
                    title=category.title,
                    description=markdown.markdown(category.description),
                    cards=reviews_map[category.id])
        review_pages.append(page)

    context = {'pages': pages, 'reviews': review_pages}

    return render(request, 'index.html', context)


@minified_response
@cache_page(60 * 60)
def blog(request):
    blog_map = defaultdict(list)
    blogs = Blog.objects.all().order_by('position')
    for blog in blogs:
        blog.description = markdown.markdown(blog.description)
        blog_map[blog.category.id].append(blog)

    pages = list()
    categories = BlogCategory.objects.all().order_by('id')
    for category in categories:
        page = Page(id=category.id,
                    title=category.title,
                    description=markdown.markdown(category.description),
                    cards=blog_map[category.id])
        pages.append(page)

    context = {'pages': pages}

    client_ip = AccessCount.get_client_ip(request)
    access_count, created = AccessCount.objects.get_or_create(ip=client_ip)
    access_count.visit_count += 1
    access_count.save()

    return render(request, 'blog.html', context)
