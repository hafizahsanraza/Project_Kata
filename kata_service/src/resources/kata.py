
from aiohttp import web

class Status:
    async def status(self, request):
        return web.json_response("Service is running fine.", status=200)

class KataWrapper:
    async def wrap(self, request):
        
        data = await request.json()
        result = self._kata(data["content"],int(data["len"]))
        
        return web.json_response({"result": result}, status=200)

    def _kata(self, content, column):
        if len(content) <= column:
            return content
        
        # check if last space saving a word cut
        last_spacing = content[0:column].rfind(" ")
        if last_spacing == -1:
            last_spacing = column
        
        return content[0:last_spacing] + "\n" + self._kata(content[last_spacing:].lstrip(), column)
        