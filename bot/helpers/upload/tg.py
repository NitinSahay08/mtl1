import os
import time
from pyrogram.types import CallbackQuery
from bot.helpers.utils import humanbytes, get_duration, get_thumbnail, progress_for_pyrogram
from bot.config import TG_CONFIG
from bot.__init__ import user as userBot

FILE_SIZE_LIMIT = 2 * (1024 ** 3)

class TGUploader:
    def __init__(self, app, msg, premium=False, client=None):
        self.app = app
        self.msg = msg
        self.tg_config = TG_CONFIG()
        self.premium = TG_CONFIG.premium

    def upload_video(self, callback: CallbackQuery, file_path: str) -> None:
        """Upload a video to Telegram"""
        file_name = os.path.basename(file_path)
        duration = get_duration(file_name)
        thumb = get_thumbnail(file_name, "", duration / 2)

        file_size = os.stat(file_path).st_size
        caption = f'''<code>{file_name}</code>'''

        progress_args_text = f"<code>[+]</code> <b>{'Uploading'}</b>\n<code>{file_name}</code>"
        progress = progress_for_pyrogram(callback.from_user.id, self.app, callback.message)
        start_time = time.time()

        if self.premium or file_size > FILE_SIZE_LIMIT:  # 2GB
            self._send_video_(callback, file_path, duration, thumb, caption, progress, start_time)
        else:
            self._send_video_to_chat(callback, file_path, duration, thumb, caption, progress, start_time)

    def _send_video_(self, callback: CallbackQuery, file_path: str, duration: int, thumb: str, caption: str, progress: progress_for_pyrogram, start_time: float) -> None:
        """Send video"""
        try:
            sent_ = userBot.send_video(
                chat_id=callback.message.chat.id,
                video=file_path,
                height=self.tg_config.video_height,
                width=self.tg_config.video_width,
                duration=duration,
                thumb=thumb,
                caption=caption,
                progress=progress.progress_for_pyrogram,
                progress_args=(progress_args_text, start_time),
            )
        except Exception as e:
            print(e)
            self.msg.edit(f"`{e}`")

    def _send_video_to_chat(self, callback: CallbackQuery, file_path: str, duration: int, thumb: str, caption: str, progress: progress_for_pyrogram, start_time: float) -> None:
        """Send video to chat"""
        try:
            sent_ = self.app.send_video(
                chat_id=callback.message.chat.id,
                video=file_path,
                height=self.tg_config.video_height,
                width=self.tg_config.video_width,
                duration=duration,
                thumb=thumb,
                caption=caption,
                progress=progress.progress_for_pyrogram,
                progress_args=(progress_args_text, start_time),
            )
        except Exception as e:
            print(e)
            self.msg.edit(f"`{e}`")
