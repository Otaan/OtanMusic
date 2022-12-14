from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Otan import db_mem


def others_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 1
    return [[
            InlineKeyboardButton(
                text="ð ðð´ð°ðð²ð· ð»ððð¸ð²ð",
                callback_data=f"lyrics {videoid}|{user_id}",
            )
        ], [
            InlineKeyboardButton(
                text="â ðð¾ðð ð¿ð»ð°ðð»ð¸ðð",
                callback_data=f"your_playlist {videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="â ð¶ðð¾ðð¿ ð¿ð»ð°ðð»ð¸ðð",
                callback_data=f"group_playlist {videoid}|{user_id}",
            ),
        ], [
            InlineKeyboardButton(
                text="âï¸ï¸ï¸ ð³ð¾ðð½ð»ð¾ð°ð³ ð°ðð³ð¸ð¾/ðð¸ð³ð´ð¾",
                callback_data=f"audio_video_download {videoid}|{user_id}",
            )
        ], [InlineKeyboardButton(
                text="â® ð¶ð¾ ð±ð°ð²ðº",
                callback_data=f"pr_go_back_timer {videoid}|{user_id}",
            ), InlineKeyboardButton(text="â ð²ð»ð¾ðð´ â", callback_data="close")]]


def download_markup(videoid, user_id):
    return [[
            InlineKeyboardButton(
                text="âï¸ï¸ï¸ ð¶ð´ð ð°ðð³ð¸ð¾",
                callback_data=f"gets audio|{videoid}|{user_id}",
            ),
            InlineKeyboardButton(
                text="âï¸ï¸ï¸ ð¶ð´ð ðð¸ð³ð´ð¾",
                callback_data=f"gets video|{videoid}|{user_id}",
            ),
        ], [InlineKeyboardButton(
                text="â® ð¶ð¾ ð±ð°ð²ðº", callback_data=f"goback {videoid}|{user_id}"
            ), InlineKeyboardButton(text="â¢CÊá´sá´â¢â", callback_data="close")]]