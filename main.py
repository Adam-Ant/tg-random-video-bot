#!/usr/bin/env python

import logging
from random import randint
from uuid import uuid4

from environs import Env
from telegram import Update, InlineQueryResultVideo, error
from telegram.ext import Updater, InlineQueryHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
env = Env()


def inlinequery(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""

    results = [
        InlineQueryResultVideo(
            id=str(uuid4()),
            title=inline_title,
            video_url=f"{base_url}/{randint(1,max_clips)}.mp4",
            thumb_url=f"{base_url}/thumb.jpg",
            mime_type="video/mp4"
        )
    ]

    update.inline_query.answer(results, cache_time=1, is_personal=True)


def main() -> None:
    """Run the bot."""

    # Check for required environs
    try:
        env.read_env()
        bot_token = env.str("TOKEN")
        # Can't add arbitrary vars to the handler functions :(
        global max_clips
        max_clips = env.int("CLIPS", 50, validate=lambda n: n > 0)
        global base_url
        base_url = env.str("BASE_URL")
        global inline_title
        inline_title = env.str("TITLE", "Get a random clip!")
    except:
        logging.critical("Unable to parse required environment variables", exc_info=True)
        exit(1)
    
    # Create the Updater and pass it your bot's token.
    try:
        updater = Updater(bot_token)
    except error.InvalidToken:
        logging.critical("Invalid Telegram Token - exiting")
        exit(1)


    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Handle inline queries
    dispatcher.add_handler(InlineQueryHandler(inlinequery))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()