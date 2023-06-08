import asyncio
import uvicorn

async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Server!',
    })


async def main():
    config = uvicorn.Config("userver3:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__userver3__":
    asyncio.run(main())
