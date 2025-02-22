from aiohttp import web

from utils import load

user_registry = load()


async def handle_pull_request(request: web.Request) -> str:
    data = await request.json()

    pull_request_action = data.get("action", "")
    pull_request_title = data["pull_request"]["title"]
    pull_request_url = data["pull_request"]["html_url"]
    pull_request_user = data["pull_request"]["user"]["login"]

    tg_user_id = user_registry.get(pull_request_user, None)
    mention = (
        f"<a href='tg://user?id={tg_user_id}'>@{pull_request_user}</a>"
        if tg_user_id
        else pull_request_user
    )
    message = (
        f"<b>Pull Request</b> {pull_request_action}: \n\n"
        f"Title: {pull_request_title}\n"
        f"Author: {mention}\n"
        f"URL: {pull_request_url}"
    )
    return message


async def handle_pull_request_review(request: web.Request) -> str:
    data = await request.json()

    review_state = data["review"]["state"]
    pull_request_url = data["pull_request"]["html_url"]
    reviewer = data["review"]["user"]["login"]

    tg_user_id = user_registry.get(reviewer, None)
    mention = (
        f"<a href='tg://user?id={tg_user_id}'>@{reviewer}</a>"
        if tg_user_id
        else reviewer
    )

    message = (
        f"<b>Review</b> {review_state}: \n\n"
        f"Reviewer: {mention}\n"
        f"PR: {pull_request_url}"
    )

    return message
