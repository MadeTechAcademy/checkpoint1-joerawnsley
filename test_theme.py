from theme import Theme
from duty import Duty
from duties_and_themes_data import *

def test_theme_lists_duties_as_text_with_title_1():
    automate_theme = Theme("Automate!", [duty_5, duty_7, duty_10])
    assert automate_theme.plainText() == ("Theme: Automate!"
    "Duties:"
    f"Duty 5: {duty_5.plainText()}."
    f"Duty 7: {duty_7.plainText()}."
    f"Duty 10: {duty_10.plainText()}."
    )