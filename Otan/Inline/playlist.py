from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    return [
        [
            InlineKeyboardButton(
                text="πΏπ»π°ππ»πΈππ",
                callback_data=f"playlist_check {user_id}|πΆππΎππΏ|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s πΏπ»π°ππ»πΈππ",
                callback_data=f"playlist_check {user_id}|πΏπ΄πππΎπ½π°π»|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="β π²π»πΎππ΄ ββ", callback_data="close")],
    ]


def playlist_markup(user_name, user_id, videoid):
    return [
        [
            InlineKeyboardButton(
                text="πΏπ»π°ππ»πΈππ\u200b",
                callback_data=f"show_genre {user_id}|πΆππΎππΏ|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s πΏπ»π°ππ»πΈππ",
                callback_data=f"show_genre {user_id}|πΏπ΄πππΎπ½π°π»|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="β π²π»πΎππ΄ ββ", callback_data="close")],
    ]


def play_genre_playlist(user_id, type, videoid):
    return [
        [
            InlineKeyboardButton(
                text="π³πΉ",
                callback_data=f"play_playlist {user_id}|{type}|π±πΎπ»π»πππΎπΎπ³",
            ),
            InlineKeyboardButton(
                text="ππ»π΄π΄πΏ",
                callback_data=f"play_playlist {user_id}|{type}|π·πΎπ»π»πππΎπΎπ³",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ππ°π³",
                callback_data=f"play_playlist {user_id}|{type}|πΏπ°πππ",
            ),
            InlineKeyboardButton(
                text="πΏπ°πππ",
                callback_data=f"play_playlist {user_id}|{type}|π»πΎπ΅πΈ",
            ),
        ],
        [
            InlineKeyboardButton(
                text="β π±π°π²πΊ β",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="β π²π»πΎππ΄ ββ", callback_data="close"),
        ],
    ]


def add_genre_markup(user_id, type, videoid):
    return [
        [
            InlineKeyboardButton(
                text="β π³πΉ",
                callback_data=f"add_playlist {videoid}|{type}|ππ΄π΄π±",
            ),
            InlineKeyboardButton(
                text="β πΏπ°πππ",
                callback_data=f"add_playlist {videoid}|{type}|ππ°π³",
            ),
        ],
        [
            InlineKeyboardButton(
                text="β ππ°π³",
                callback_data=f"add_playlist {videoid}|{type}|πΏπ°πππ",
            ),
            InlineKeyboardButton(
                text="β ππ»π΄π΄πΏ",
                callback_data=f"add_playlist {videoid}|{type}|π»πΎπ΅πΈ",
            ),
        ],
        [
            InlineKeyboardButton(
                text="β π±π°π²πΊ ββ", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="β π²π»πΎππ΄ β", callback_data="close"),
        ],
    ]


def check_genre_markup(type, videoid, user_id):
    return [
        [
            InlineKeyboardButton(
                text="π³πΉ", callback_data=f"check_playlist {type}|ππ΄π΄π±"
            ),
            InlineKeyboardButton(
                text="πΏπ°πππ", callback_data=f"check_playlist {type}|ππ°π³"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ππ°π³", callback_data=f"check_playlist {type}|πΏπ°πππ"
            ),
            InlineKeyboardButton(
                text="ππ»π΄π΄πΏ", callback_data=f"check_playlist {type}|π»πΎπ΅πΈ"
            ),
        ],
        [InlineKeyboardButton(text="β π²π»πΎππ΄ ββ", callback_data="close")],
    ]


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    return [
        [
            InlineKeyboardButton(
                text="πΏπ»π°ππ»πΈππ\u200b",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s πΏπ»π°ππ»πΈππ",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s πΏπ»π°ππ»πΈππ",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="β π²π»πΎππ΄ ββ", callback_data="close")],
    ]


def paste_queue_markup(url):
    return [
        [
            InlineKeyboardButton(text="βΆοΈ", callback_data="resumecb"),
            InlineKeyboardButton(text="βΈοΈ", callback_data="pausecb"),
            InlineKeyboardButton(text="β­οΈ", callback_data="skipcb"),
            InlineKeyboardButton(text="βΉοΈ", callback_data="stopcb"),
        ],
        [InlineKeyboardButton(text="π²π·π΄π²πΊπΎππ πππ΄ππ΄π³ πΏπ»π°ππ»πΈππ", url=f"{url}")],
        [InlineKeyboardButton(text="β π²π»πΎππ΄ ββ", callback_data="close")],
    ]


def fetch_playlist(user_name, type, genre, user_id, url):
    return [
        [
            InlineKeyboardButton(
                text=f"πΏπ»π°π {user_name[:10]}'s {genre} πΏπ»π°ππ»πΈππ",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="π²π·π΄π²πΊπΎππ πΏπ»π°ππ»πΈππ", url=f"{url}")],
        [InlineKeyboardButton(text="β π²π»πΎππ΄ ββ", callback_data="close")],
    ]


def delete_playlist_markuup(type, genre):
    return [
        [
            InlineKeyboardButton(
                text="ππ΄π π³π΄π»π΄ππ΄!",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="β π½πΎ ββ", callback_data="close"),
        ]
    ]