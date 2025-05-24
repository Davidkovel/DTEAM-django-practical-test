from .models import RequestLog


class RequestLogMiddleware:
    """
    Middleware to log request information.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request method and path
        if not request.path.startswith('/api/'):
            return self.get_response(request)

        response = self.get_response(request)

        print(f"[INFO] Request Method: {request.method}, Request Path: {request.path}")

        try:
            query_params = dict(request.GET) if request.GET else None

            RequestLog.objects.create(
                method=request.method,
                path=request.path,
                query_params=query_params,
                remote_ip_address=self.get_client_ip(request)
            )
        except Exception as ex:
            print(f"[ERROR] Failed to log request: {ex}")

        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR', '')
        return ip
