from theme import Theme
from duty import Duty
from duties_and_themes_data import *

def test_theme_plaintext_lists_duties_with_title():
    automate_theme = Theme("Automate!", [duty_5, duty_7, duty_10])
    automate_text_output = automate_theme.plainText()
    assert duty_5.plainText() in automate_text_output
    assert duty_7.plainText() in automate_text_output
    assert duty_10.plainText() in automate_text_output
    assert duty_1.plainText() not in automate_text_output
    assert duty_11.plainText() not in automate_text_output
    assert "Automate!" in automate_text_output
    houston_theme = Theme("Houston, Prepare to Launch", [duty_6, duty_7, duty_10, duty_12])
    houston_text_output = houston_theme.plainText()
    assert duty_6.plainText() in houston_text_output
    assert duty_7.plainText() in houston_text_output
    assert duty_10.plainText() in houston_text_output
    assert duty_12.plainText() in houston_text_output
    assert duty_5.plainText() not in houston_text_output
    assert duty_13.plainText() not in houston_text_output
    assert "Houston, Prepare to Launch" in houston_text_output
    assert "Automate!" not in houston_text_output