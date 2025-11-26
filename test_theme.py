from theme import Theme
from duty import Duty
from duties_and_themes_data import *

def test_theme_lists_duties_as_text_with_title():
    automate_theme = Theme("Automate!", [duty_5, duty_7, duty_10])
    assert automate_theme.plainText() == f"""
    Theme: Automate!
    Duties:
    Duty 5: {duty_5.plainText()}.
    Duty 7: {duty_5.plainText()}.
    Duty 10: {duty_5.plainText()}.
    """