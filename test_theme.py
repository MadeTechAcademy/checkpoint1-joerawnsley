from theme import Theme
from duty import Duty
from duties_and_themes_data import *

def test_theme_lists_duties_as_text_with_title_1():
    automate_theme = Theme("Automate!", [duty_5, duty_7, duty_10])
    assert automate_theme.plainText() == ("Theme: Automate!\n\n"
    "Duties:\n\n"
    f"{duty_5.plainText()}\n"
    f"{duty_7.plainText()}\n"
    f"{duty_10.plainText()}"
    )