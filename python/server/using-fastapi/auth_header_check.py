class AuthHeaderCheck:
    def __init__(self, app, include_patterns) -> None:
        self.app = app
        self.include_patterns = include_patterns

    async def __call__(self, scope, receive, send) -> None:
        x_api_key_header = None
        request_path = scope['path']

        for h in scope['headers']:
            if h[0] == b'x-api-key':
                x_api_key_header = h[1]

        for pattern in self.include_patterns:
            if request_path.startswith(pattern) and not x_api_key_header:
                await send({
                    'type': 'http.response.start',
                    'status': 401,
                })
                await send({
                    'type': 'http.response.body',
                    'body': b'Specify X-API-Key header',
                })
                return
        await self.app(scope, receive, send)
