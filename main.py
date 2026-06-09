from kivy.app import App
from kivy.uix.label import Label

class StoryEngine(App):
    def build(self):
        return Label(text="APK FUNCIONANDO")

StoryEngine().run()
