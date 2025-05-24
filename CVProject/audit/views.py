from datetime import timezone, datetime

from django.views.generic import ListView

from .models import RequestLog


class RequestLogView(ListView):
    model = RequestLog
    template_name = 'audit/request_log.html'
    context_object_name = 'request_logs'
    paginate_by = 10
    ordering = ['-timestamp']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()
        return context

    def get_queryset(self):
        return super().get_queryset().only('timestamp', 'method', 'path', 'query_params', 'remote_ip_address')
