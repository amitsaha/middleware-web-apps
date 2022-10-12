class AuthHeaderCheck:

    def __init__(self, wsgi_app, included_patterns):
        self.wsgi_app = wsgi_app
        self.included_patterns = included_patterns

    def __call__(self, environ, start_response):
        request_path = environ['PATH_INFO']
        x_api_key_header = environ.get('HTTP_X_API_KEY')

        for path in self.included_patterns:
            if request_path.startswith(path) and not x_api_key_header:
                status = '401 Unauthorized'
                headers = []
                start_response(status, headers)
                for item in [b'Specify X-API-KEY header']:
                    yield item
                return
        
        yield from self.wsgi_app(environ, start_response)
