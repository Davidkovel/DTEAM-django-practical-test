from django.conf import settings

# class SettingsContextProcessor:
#     @staticmethod
#     def get_context(request):
#         return {'settings': settings}


def settings_context(request):
    return {
        'settings': settings,
    }