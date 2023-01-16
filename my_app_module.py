from aiohttp import web

async def index(request):
    return web.Response(text="Welcome home!")


my_web_app = web.Application()
my_web_app.router.add_get('/', index)
