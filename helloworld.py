from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial


class TestApp(App):
    def build(self):
        wid = Widget()
        hello = Button(text='Hello World')
        other = Button(text='Something Else')

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(hello)
        layout.add_widget(other)

        root = BoxLayout(orientation='vertical')
        root.add_widget(wid)
        root.add_widget(layout)

        return root
TestApp().run()
