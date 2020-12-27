import random

from django.http import Http404
from django.http import HttpResponseNotFound
from django.http import HttpResponseServerError
from django.shortcuts import render

from . import data


def main_view(request):
    context = {'title': data.title,
               'subtitle': data.subtitle,
               'description': data.description,
               'departures': data.departures,
               'tours': data.tours}
    # выбираем рандомные шесть туров
    all_tours = []
    for key in context['tours']:
        all_tours.append(key)
    random_tours = {}
    for i in range(6):
        random_tour = random.choice(all_tours)
        random_tours[str(i+1)] = (context['tours'][random_tour])
        all_tours.remove(random_tour)
    context['tours'] = random_tours

    return render(request, 'index.html', context=context)


def departure_view(request, departure):
    context = {}
    tours = {}
    all_tours = data.tours
    count_of_tours = 0
    prices_of_tours = []
    nights = []
    for tour, inf in all_tours.items():
        if inf['departure'] == departure:
            count_of_tours += 1
            prices_of_tours.append(inf['price'])
            nights.append(inf['nights'])
            tours[count_of_tours] = inf
    if count_of_tours == 0:
        raise Http404
    context['tours'] = tours
    context['count_of_tours'] = count_of_tours
    context['max_price'] = max(prices_of_tours)
    context['min_price'] = min(prices_of_tours)
    context['max_count_if_nights'] = max(nights)
    context['min_count_if_nights'] = min(nights)
    if departure == 'spb':
        context['departure'] = 'Летим из Петербурга'
    elif departure == 'msk':
        context['departure'] = 'Летим из Москвы'
    elif departure == 'kazan':
        context['departure'] = 'Летим из Казани'
    elif departure == 'nsk':
        context['departure'] = 'Летим из Новосибирска'
    elif departure == 'ekb':
        context['departure'] = 'Летим из Екатеринбурга'
    return render(request, 'tours/departure.html', context=context)


def tour_view(request, tour_id):
    context = {}
    for key, value in data.tours.items():
        if key == tour_id:
            context = value
    if context == {}:
        raise Http404
    stars = '★' * int(context['stars'])
    context['stars'] = stars
    return render(request, 'tours/tour.html', context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Страница не найдена')


def custom_handler500(request):
    return HttpResponseServerError('Внутренняя ошибка сервера')
