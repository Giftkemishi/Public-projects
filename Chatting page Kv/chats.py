from kivy.app import App
from datetime import datetime
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty


class ChatLabel(Label):
    bg_color = ListProperty([0.1, 0.1, 0.1, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = (10, 5)
        self.halign = 'left'
        self.valign = 'middle'
        self.size_hint_y = None
        self.bind(pos=self.redraw, size=self.redraw)
        # Schedule initial text_size adjustment
        Clock.schedule_once(self.update_text_size, 0)

    def update_text_size(self, dt):
        self.text_size = (self.width - self.padding[0]*2, None)
        self.height = self.texture_size[1] + self.padding[1]*2

    def on_size(self, *args):
        self.update_text_size(0)

    def redraw(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[15])


class chatUI(App):
    ai_spinner = None

    def send_message(self):
        user_text = self.root.ids.chat_input.text.strip()
        if not user_text:
            return

        timestamp = datetime.now().strftime("%H:%M")
        self.show_loading()

        user_label = ChatLabel(
            text=f"{user_text}\n[size=12][color=aaaaaa]{timestamp}[/color][/size]",
            markup=True,
            size_hint_y=None,
            size_hint_x=0.45,
            halign='left',
            valign='middle',
            bg_color=[0, 0.5, 1, 1]
        )
        user_label.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]+20))

        # AnchorLayout for right alignment
        container = AnchorLayout(anchor_x='right', size_hint_y=None)
        container.add_widget(user_label)
        # Bind container height to bubble height + spacing
        def update_height(instance, value):
            container.height = user_label.height + dp(15)
        user_label.bind(height=update_height)

        self.root.ids.messages_container.add_widget(container)
        self.root.ids.chat_input.text = ""

        Clock.schedule_once(lambda dt: self.finish_loading(), 1)
        Clock.schedule_once(lambda dt: setattr(self.root.ids.scroll, 'scroll_y', 0), 0.05)

    def add_ai_message(self, msg):
        timestamp = datetime.now().strftime("%H:%M")

        ai_label = ChatLabel(
            text=f"{msg}\n[size=12][color=aaaaaa]{timestamp}[/color][/size]",
            markup=True,
            size_hint_y=None,
            size_hint_x=0.45,
            halign='left',
            valign='middle',
            bg_color=[0.2, 0.2, 0.2, 1]
        )
        ai_label.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]+20))

        container = AnchorLayout(anchor_x='left', size_hint_y=None)
        container.add_widget(ai_label)
        def update_height(instance, value):
            container.height = ai_label.height + dp(15)
        ai_label.bind(height=update_height)

        self.root.ids.messages_container.add_widget(container)
        Clock.schedule_once(lambda dt: setattr(self.root.ids.scroll, 'scroll_y', 0), 0.05)

    def show_loading(self):
        if self.ai_spinner:
            return
        box = BoxLayout(size_hint_y=None, height=40, padding=(5, 5))
        spinner = ChatLabel(
            text="[i]...[/i]",
            markup=True,
            size_hint_x=None,
            width=80,
            bg_color=[0.2, 0.2, 0.2, 1],
        )
        spinner.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]+10))
        box.add_widget(spinner)
        box.add_widget(Widget())
        self.root.ids.messages_container.add_widget(box)
        self.ai_spinner = box
        self.root.ids.scroll.scroll_y = 0

    def finish_loading(self, *_):
        if self.ai_spinner:
            self.root.ids.messages_container.remove_widget(self.ai_spinner)
            self.ai_spinner = None
        self.add_ai_message("Hello! I am AI.")


if __name__ == "__main__":
    chatUI().run()
