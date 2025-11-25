from duty import Duty

def test_duty_class_returns_as_text():
    duty_1 = Duty(1, "Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage")
    assert duty_1.plainText() == "Duty 1: Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.\n"

def test_duty_class_returns_as_html():
    duty_9 = Duty(9, "Apply leading security practices throughout the Software Development Lifecycle (SDLC)")
    assert duty_9.htmlListElement() == "<li><b>Duty 9:</b> Apply leading security practices throughout the Software Development Lifecycle (SDLC).</li>\n"