import logging
import os
from telegram.ext import CallbackQueryHandler, CommandHandler, Updater
import news
import helper
import statistics

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

BOTTOKEN = os.environ.get("BOTTOKEN")

updater = Updater(token=BOTTOKEN, use_context=True)
dispatcher = updater.dispatcher


def cmd_start(update, context):
    # TODO: complete with command instructions
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to the CovidBot, where you can get updated statistics and news!\n\n" +
        "/headlines - for global headlines\n" +
        "/news <country> - for country-specific news (NOT IMPLEMENTED)\n" +
        "/stats <country> - for country-specific stats")


def cmd_headlines(update, context):
    # 1. Ping to API
    # 2. Put into list with "viewed" status
    # 3. Send link with preview
    headlines = news.get_covid_headlines()["articles"]
    string = helper.format_in_markdown("headlines", headlines)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=string,
                             parse_mode="Markdown")


def cmd_stats(update, context):
    # 1. Take in arguments for country
    # 2. Ping to API
    # 3. Send list
    if not context.args:
        country = "Singapore"
    else:
        country = context.args[0]
    resp = statistics.get_covid_stats(country)
    string = helper.format_stats(resp)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=string,
                             parse_mode="Markdown")


def cmd_news(update, context):
    if not context.args:
        country = "Singapore"
    else:
        country = context.args[0]
    newslist = news.get_covid_local_news(country)
    for i in range(3):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=newslist[i])

    # ========================================== HANDLERS ================================================ #


def add_handlers():
    start_handler = CommandHandler('start', cmd_start)
    news_handler = CommandHandler('headlines', cmd_headlines)
    stats_handler = CommandHandler('stats', cmd_stats)
    news_handler = CommandHandler('news', cmd_news)

    dispatcher.add_handler(news_handler)
    dispatcher.add_handler(stats_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(news_handler)


if __name__ == "__main__":
    updater.start_polling()
    add_handlers()
    print("Bot running...")
