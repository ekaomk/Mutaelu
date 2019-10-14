from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {
        'recommend_place': [
            {
                'name': 'ศาลพระตรีมูรติ',
                'category': 'ความรัก',
                'rating': 4.5,
                'rating_count': 10,
            },
            {
                'name': 'ศาลพระพิฆเนศ',
                'category': 'การงาน',
                'rating': 4.7,
                'rating_count': 12,
            }
        ],
        'nearest_place': [
            {
                'name': 'หลวงพ่อดำ วัดช่องแสมสาร',
                'category': 'โชคลาภ',
                'rating': 4.5,
                'rating_count': 10,
                'distance': 1.0,
            },
            {
                'name': 'ศาลเจ้าพ่อเกศงาม',
                'category': 'การงาน',
                'rating': 4.5,
                'rating_count': 10,
                'distance': 1.5,
            }
        ]
    })