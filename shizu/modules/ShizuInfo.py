# █ █ █ █▄▀ ▄▀█ █▀▄▀█ █▀█ █▀█ █ █
# █▀█ █ █ █ █▀█ █ ▀ █ █▄█ █▀▄ █▄█

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 👤 https://t.me/hikamoru


from pyrogram import Client, types
from .. import loader, utils, version


@loader.module("ShizuInfo", "sh1tn3t")
class InformationMod(loader.Module):
    """Info"""

    strings = {
        "custom_msg": "Custom message must have {mention}, {version}, {prefix}, {branch}, {platform} keywords",
        "custom_button": "Custom button must have text and url",
        "photo_url": "Photo url must be valid",
    }

    strings_ru = {
        "custom_msg": "Пользовательское сообщение должно содержать ключевые слова {mention}, {version}, {prefix}, {branch}, {platform}",
        "custom_button": "Пользовательская кнопка должна содержать текст и url",
        "photo_url": "URL фотографии должен быть действительным",
    }

    strings_uz = {
        "custom_msg": "Foydalanuvchi xabari {mention}, {version}, {prefix}, {branch}, {platform} kalit so'zlarini o'z ichiga olishi kerak",
        "custom_button": "Foydalanuvchi tugmasi matn va url ni o'z ichiga olishi kerak",
        "photo_url": "Rasm url manzili to'g'ri bo'lishi kerak",
    }

    strings_jp = {
        "custom_msg": "カスタムメッセージには、{mention}、{version}、{prefix}、{branch}、{platform}のキーワードが必要です",
        "custom_button": "カスタムボタンにはテキストとURLが必要です",
        "photo_url": "写真のURLは有効である必要があります",
    }

    strings_ua = {
        "custom_msg": "Користувацьке повідомлення повинно містити ключові слова {mention}, {version}, {prefix}, {branch}, {platform}",
        "custom_button": "Користувацька кнопка повинна містити текст та url",
        "photo_url": "URL фотографії повинен бути дійсним",
    }

    strings_kz = {
        "custom_msg": "Қолданушы қолданбасы {mention}, {version}, {prefix}, {branch}, {platform} сөздерін қолжетімді болуы керек",
        "custom_button": "Қолданушы түймесі мәтін мен url болуы керек",
        "photo_url": "Фото URL мекен-жайы растауы керек",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "custom_message",
            False,
            lambda: self.strings("custom_msg"),
            "custom_buttons",
            {"text": "🏄 Here we are", "url": "https://t.me/shizu_talks"},
            lambda: self.strings("custom_button"),
            "photo_url",
            "https://0x0.st/HOP4.jpg",
            lambda: self.strings("photo_url"),
        )

    def text_(self, me: types.User):
        mention = f'<a href="tg://user?id={me.id}">{utils.get_display_name(me)}</a>'
        prefix = ", ".join(self.prefix)
        if self.config["custom_message"]:
            return "🐙 Shizu\n" + self.config["custom_message"].format(
                mention=mention,
                version={".".join(map(str, version.__version__))},
                prefix=prefix,
                branch=version.branch,
                platform=utils.get_platform(),
            )
        else:
            return (
                "🐙 <b>Shizu UserBot</b>\n\n"
                f"👑 <b>Owner</b>: {mention}\n\n"
                f"🌳 <b>Branch</b>: <code>{version.branch}</code>\n"
                f"🦋 <b>Version</b>: <code>{'.'.join(map(str, version.__version__))}</code>\n\n"
                f"⌨️ <b>Prefix</b>: <code>{prefix}</code>\n"
                f"{utils.get_platform()}"
            )

    @loader.command()
    async def info(self, app: Client, message: types.Message):
        """Info about Shizu"""
        await message.answer(
            response=self.text_(self.me),
            reply_markup=[[self.config["custom_buttons"]]],
            photo=self.config["photo_url"],
        )

    @loader.command()
    async def wuserbot(self, app: Client, message: types.Message):
        """What is a userbot?"""
        text = """<emoji id=5188377234380954537>🌘 <b>Userbot</b>

<emoji id=5472238129849048175>😎 A userbot can be characterized as a <b>third-party software application</b> that engages with the Telegram API in order to execute <b>automated operations on behalf of an end user</b>. These userbots possess the capability to streamline a variety of tasks, encompassing activities such as <b>dispatching messages, enrolling in channels, retrieving media files, and more</b>.

<emoji id=5474667187258006816>😎 Diverging from conventional Telegram bots, <b>userbots operate within the confines of a user's account</b> rather than within a dedicated bot account. This particular distinction empowers userbots with enhanced accessibility to a broader spectrum of functionalities and a heightened degree of flexibility in executing actions.

<emoji id=5472267631979405211>🚫 It is imperative to underscore, however, that <b>userbots do not receive official endorsement from the Telegram platform</b>, and their utilization may potentially infringe upon the terms of service established by the platform. Consequently, <b>users are advised to exercise discernment and prudence when deploying userbots</b>, ensuring that their usage remains devoid of any malevolent intent or misconduct.
        """
        await message.answer(text)
