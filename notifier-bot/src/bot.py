import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiohttp import web

import hooks
from config import get_config
from utils import save

bot = Bot(token=get_config().API_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message(commands=["start", "register"])
async def register_user(message: types.Message):
    args = message.text.split()
    if len(args) < 2:
        await message.reply("Использование: /register <github_username>")
        return

    github_username = args[1]
    hooks.user_registry[github_username] = message.from_user.id
    save(hooks.user_registry)

    await message.reply(f"Вы зарегистрированы как {github_username}!")


async def handle_pull_request(request: web.Request):
    message = await hooks.handle_pull_request(request)

    await bot.send_message(get_config().CHAT_ID, message, parse_mode="HTML")
    return web.Response(status=200)


async def handle_pull_request_review(request: web.Request):
    message = await hooks.handle_pull_request_review(request)

    await bot.send_message(get_config().CHAT_ID, message, parse_mode="HTML")
    return web.Response(status=200)


async def on_startup(_: Dispatcher):
    await bot.set_webhook(get_config().WEBHOOK_URL)
    app = web.Application()
    app.router.add_post("/webhook/github/pull_request", handle_pull_request)
    app.router.add_post("/webhook/github/review", handle_pull_request_review)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()

    logging.info("Webhook server started")


async def on_shutdown(_: Dispatcher):
    logging.warning("Shutting down webhook server")
    await bot.delete_webhook()


def main():
    asyncio.run(on_startup(dispatcher))
    try:
        web.run_app(web.Application())
    except KeyboardInterrupt:
        asyncio.run(on_shutdown(dispatcher))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
