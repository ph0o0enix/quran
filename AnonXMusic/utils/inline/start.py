from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
        InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")
        ],
        [
        InlineKeyboardButton(
                text= "₁ القناه ₁", url=f"https://t.me/S1_I_I"), 
        InlineKeyboardButton(
                text= "₂ القناه ₂", url=f"https://t.me/CH_KORAN")
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
        [
        
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ]
    ]
    return buttons
