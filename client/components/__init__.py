from client.components.base import BaseComponent
from client.components.button import Button
from client.components.input import Input
from client.components.text_area import TextArea


class Components:
    button = Button
    text_area = TextArea
    input = Input
    base = BaseComponent


__all__ = ["BaseComponent", "Button"]
