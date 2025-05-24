import requests
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache


@csrf_exempt
def translate_cv(request, cv_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            language = data.get('language')
            cv_data = data.get('cv_data')

            cache_key = f'translation_{cv_id}_{language}'
            if cached := cache.get(cache_key):
                return JsonResponse({'translated': cached})

            if not language or not cv_data:
                return JsonResponse({'error': 'Missing language or CV data'}, status=400)

            def translate_text(text, lang):
                if not text:
                    return text

                try:
                    response = requests.get(
                        'https://api.mymemory.translated.net/get',
                        params={
                            'q': text,
                            'langpair': f'en|{lang}',
                            'de': 'your-email@example.com'  # Для бесплатного API
                        }
                    )
                    result = response.json()
                    return result['responseData']['translatedText'] or text
                except Exception:
                    return text

            translated = {
                'first_name': translate_text(cv_data['first_name'], language),
                'last_name': translate_text(cv_data['last_name'], language),
                'bio': translate_text(cv_data['bio'], language),
                'skills': [
                    {
                        'name': translate_text(skill['name'], language),
                        'proficiency': skill['proficiency']
                    }
                    for skill in cv_data['skills']
                ],
                'projects': [
                    {
                        'title': translate_text(project['title'], language),
                        'description': translate_text(project['description'], language)
                    }
                    for project in cv_data['projects']
                ]
            }

            cache.set(cache_key, translated, timeout=60 * 60 * 24)
            return JsonResponse({'translated': translated})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
