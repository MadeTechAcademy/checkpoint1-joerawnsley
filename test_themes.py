from themes import list_of_duties
from themes import print_duties_to_terminal
from themes import create_html_document

import os



duty_3 = "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review."
duty_8 = "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance."
duty_13 = "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
        
class TestListOfDuties():
    def test_length(self):
        assert len(list_of_duties) == 13
    
    def test_includes_duties(self):
        assert duty_3 in list_of_duties
        assert duty_8 in list_of_duties
        assert duty_13 in list_of_duties


class TestPrintFunction():
    def test_check_capsys(self, capsys):
        print_duties_to_terminal()
        captured = capsys.readouterr()

        assert duty_3 in captured.out
        assert duty_8 in captured.out
        assert duty_13 in captured.out


class TestCreateHTMLDocument():
    def test_html_doc_is_created(self):
        html_list = "list_of_duties.html"
        create_html_document(html_list)
        
        assert os.path.exists(html_list)
        
        os.remove(html_list)
        assert not os.path.exists(html_list)
        