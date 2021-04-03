"""
Discord Webhook Send Tool
"""
# made by jeong ji min
# jeong@jimin.email

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from discord_webhook import DiscordWebhook


class discordwebhook(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.url_input = toga.TextInput(style=Pack(flex=1), placeholder='discord webhook url')
        self.name_input = toga.TextInput(style=Pack(flex=1), placeholder='message')
        
        url_box = toga.Box(style=Pack(direction=ROW, padding=5))
        url_box.add(self.url_input)
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(self.name_input)

        button = toga.Button(
            'Send',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(url_box)
        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        webhook = DiscordWebhook(url=self.url_input.value, content=self.name_input.value)
        response = webhook.execute()


def main():
    return discordwebhook()
