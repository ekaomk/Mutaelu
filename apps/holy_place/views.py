from django.shortcuts import render
from django.http import HttpResponse
from django import template

register = template.Library()

@register.filter
def intcomma(value):
    return value + 1

def index(request):
    context = {}
    category = ["ความรัก","โชคลาภ","คุ้มครอง","การงาน","อื่นๆ"]
    holy_place_list = {
        'recommend_place': [
            {
                'name': 'ศาลพระตรีมูรติ',
                'category': 'ความรัก',
                'rating': 4.5,
                'rating_count': 10,
                'img': "https://upload.wikimedia.org/wikipedia/commons/9/9a/Spring_Temple_Buddha_1.jpg"
            },
            {
                'name': 'ศาลพระพิฆเนศ',
                'category': 'การงาน',
                'rating': 4.7,
                'rating_count': 12,
                'img': "https://upload.wikimedia.org/wikipedia/commons/9/9a/Spring_Temple_Buddha_1.jpg"
            },
            {
                'name': 'วัดแขก สีลม',
                'category': 'การงาน',
                'rating': 4.7,
                'rating_count': 12,
                'img': "https://upload.wikimedia.org/wikipedia/commons/9/9a/Spring_Temple_Buddha_1.jpg"
            },
            {
                'name': 'วัดมหาบุศย์',
                'category': 'ความรัก',
                'rating': 4.5,
                'rating_count': 10,
                'img': "https://upload.wikimedia.org/wikipedia/commons/9/9a/Spring_Temple_Buddha_1.jpg"
            }
        ],
        'nearest_place': [
            {
                'name': 'หลวงพ่อดำ วัดช่องแสมสาร',
                'category': 'โชคลาภ',
                'rating': 4.5,
                'rating_count': 10,
                'distance': 1.0,
                'img': "https://upload.wikimedia.org/wikipedia/commons/9/9a/Spring_Temple_Buddha_1.jpg"
            },
            {
                'name': 'ศาลเจ้าพ่อเกศงาม',
                'category': 'การงาน',
                'rating': 4.5,
                'rating_count': 10,
                'distance': 1.5,
                'img': "https://upload.wikimedia.org/wikipedia/commons/9/9a/Spring_Temple_Buddha_1.jpg"

            },
            {
                'name': 'ศาลปู่ย่าเมืองทอง',
                'category': 'โชคลาภ',
                'rating': 4.5,
                'rating_count': 10,
                'distance': 1.7,
                'img': "https://upload.wikimedia.org/wikipedia/commons/9/9a/Spring_Temple_Buddha_1.jpg"

            },
            {
                'name': 'ศาลเจ้าพ่อเสือ พระนคร',
                'category': 'คุ้มครอง',
                'rating': 4.5,
                'rating_count': 10,
                'distance': 2.5,
                'img': "https://upload.wikimedia.org/wikipedia/commons/9/9a/Spring_Temple_Buddha_1.jpg"
            }
        ]
    }
    
    context["holy_place_list"] = holy_place_list
    context["category"] = category

    return render(request, 'index.html', context)
