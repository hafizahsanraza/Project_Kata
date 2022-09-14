import aiohttp_cors
import config

from aiohttp import web

from src.resources.kata import KataWrapper, Status




def _create_app():
    app = web.Application()

    kata_resource = KataWrapper()
    status_resource = Status()
    app.add_routes(
        [
            web.get(config.get_api_base_path() + "/status", status_resource.status),
            web.post(config.get_api_base_path() + "/kata", kata_resource.wrap)
        ]
    )
    # Configure default CORS settings.
    cors = aiohttp_cors.setup(
        app,
        defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
                allow_methods="*",
            )
        },
    )
    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)
    return app


def get_app():
    app = _create_app()
    return app

if __name__ == "__main__":
    web.run_app(get_app(), port=8080)