from classes.theme import Theme
from data.duties import *

def test_automate_theme_plaintext_lists_duties_with_title():
    automate_theme = Theme("Automate!", [duty_5, duty_7, duty_10])
    automate_text_output = automate_theme.plainText()
    assert duty_5.plainText() in automate_text_output
    assert duty_7.plainText() in automate_text_output
    assert duty_10.plainText() in automate_text_output
    assert duty_1.plainText() not in automate_text_output
    assert duty_11.plainText() not in automate_text_output
    assert "Automate!" in automate_text_output

def test_houston_theme_plaintext_lists_duties_with_title():
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
    
def test_theme_html_returns_html_string_with_heading():
    bootcamp_theme = Theme("Bootcamp", [duty_1, duty_2, duty_3, duty_4, duty_13])
    bootcamp_html_output = bootcamp_theme.htmlString()
    bootcamp_heading = "<h2>Theme: Bootcamp</h2>"
    assert duty_1.htmlListElement() in bootcamp_html_output
    assert duty_2.htmlListElement() in bootcamp_html_output
    assert duty_3.htmlListElement() in bootcamp_html_output
    assert duty_4.htmlListElement() in bootcamp_html_output
    assert duty_13.htmlListElement() in bootcamp_html_output
    assert duty_5.htmlListElement() not in bootcamp_html_output
    assert duty_10.htmlListElement() not in bootcamp_html_output
    assert bootcamp_heading in bootcamp_html_output
    assert bootcamp_html_output.count("<ul>") == 1
    assert bootcamp_html_output.count("</ul>") == 1
    assert bootcamp_html_output.count("<li>") == 5
    assert bootcamp_html_output.count("</li>") == 5