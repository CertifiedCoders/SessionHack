from pyrogram.types import InlineKeyboardButton as IKB
from pyrogram.types import InlineKeyboardMarkup as IKM

PM_TEXT = """
<b>ʜᴇʏ {user},</b>
ɪ ᴀᴍ <b>{bot}</b> — ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ sᴇssɪᴏɴ ʜᴀᴄᴋɪɴɢ ʀᴏʙᴏᴛ.

sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ <b>Pyrogram</b> ᴀɴᴅ <b>Telethon</b> sᴛʀɪɴɢ sᴇssɪᴏɴs.
ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴡʜᴀᴛ ɪ ᴄᴀɴ ᴅᴏ.
"""

HACK_TEXT = """
<b>ʜᴀᴄᴋ ᴍᴏᴅᴜʟᴇs</b>

<b>A</b> — ᴄʜᴇᴄᴋ ᴜsᴇʀ’s ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs  
<b>B</b> — ɢᴇᴛ ғᴜʟʟ ᴜsᴇʀ ɪɴғᴏ (ᴘʜᴏɴᴇ, ᴜsᴇʀɴᴀᴍᴇ, ᴇᴛᴄ)  
<b>C</b> — ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ  
<b>D</b> — ɢᴇᴛ ʟᴀsᴛ ᴏᴛᴘ (ᴀғᴛᴇʀ ʟᴏɢɪɴ)  
<b>E</b> — ᴊᴏɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ  
<b>F</b> — ʟᴇᴀᴠᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ  
<b>G</b> — ᴅᴇʟᴇᴛᴇ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ  
<b>H</b> — ᴄʜᴇᴄᴋ 2FA sᴛᴀᴛᴜs  
<b>I</b> — ᴛᴇʀᴍɪɴᴀᴛᴇ ᴀʟʟ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs  
<b>J</b> — ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ  
<b>K</b> — ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴜsᴇʀ  
<b>L</b> — ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴀᴅᴍɪɴs
"""

USER_INFO_TEMPLATE = """
<b>ᴜsᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>

<b>ɴᴀᴍᴇ:</b> {name}
<b>ɪᴅ:</b> <code>{id}</code>
<b>ᴘʜᴏɴᴇ:</b> <code>+{phone}</code>
<b>ᴜsᴇʀɴᴀᴍᴇ:</b> {username}
"""

PM_BUTTON = IKM([[IKB("ʜᴀᴄᴋ ᴍᴏᴅᴜʟᴇs", callback_data="show_hack_menu")]])

HACK_MODS = IKM([
    [IKB("A", callback_data="hack_groups"),   IKB("B", callback_data="hack_info"),   IKB("C", callback_data="hack_banall")],
    [IKB("D", callback_data="hack_otp"),      IKB("E", callback_data="hack_join"),   IKB("F", callback_data="hack_leave")],
    [IKB("G", callback_data="hack_delete"),   IKB("H", callback_data="hack_2fa"),    IKB("I", callback_data="hack_terminate")],
    [IKB("J", callback_data="hack_delacc"),   IKB("K", callback_data="hack_promote"), IKB("L", callback_data="hack_demoteall")],
    [IKB("ʙᴀᴄᴋ", callback_data="back_to_start")]
])

LOG_TEXT = """
● ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ●

ᴀ ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ ᴛᴏ ᴄᴏɴᴛʀᴏʟ ᴀɴʏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴠɪᴀ
Pyrogram ᴏʀ Telethon sᴛʀɪɴɢ sᴇssɪᴏɴ.

ᴏᴡɴᴇʀ: ᴄᴇʀᴛɪғɪᴇᴅ ᴄᴏᴅᴇʀ
"""