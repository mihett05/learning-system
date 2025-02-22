import asyncio
import logging

from aiohttp import web

from src.bot import on_startup, on_shutdown, dispatcher


def main():
    asyncio.run(on_startup(dispatcher))
    try:
        web.run_app(web.Application())
    except KeyboardInterrupt:
        asyncio.run(on_shutdown(dispatcher))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
