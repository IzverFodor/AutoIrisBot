__version__ = (0, 0, 7)


import asyncio

from .. import loader, utils


class AutoIrisBotMod(loader.Module):
    """Автомайнинг в боте ирис"""

    strings = {"name": "AutoIrisBot"}

    async def fermacmd(self, message):
        """Включение автофермы. Выключение "Ферма стоп"."""
        self.set("ferma", True)
        while self.get("ferma"):
            await message.reply("Ферма")
            await asyncio.sleep(0.1)
            await utils.answer(
                message,
                "Следующая команда будет произведена через 4 часа.",
            )
            await asyncio.sleep(14460)

    async def watcher(self, message):
        if not getattr(message, "out", False):
            return

        if message.raw_text.lower() == "ферма стоп":
            self.set("ferma", False)
            await utils.answer(message, "<b>Автоматическая ферма остановлена.</b>")
