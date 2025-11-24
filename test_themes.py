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
    html_list_name = "list_of_duties.html"
    
    def remove_file(self):
        if os.path.exists(self.html_list_name):
            os.remove(self.html_list_name)
            assert not os.path.exists(self.html_list_name)
    
    def test_html_doc_is_created(self):
        create_html_document(self.html_list_name)
        assert os.path.exists(self.html_list_name)
        self.remove_file()
        # os.remove(self.html_list_name)
        # assert not os.path.exists(self.html_list_name)
    
    def test_html_doc_includes_title(self):
        create_html_document(self.html_list_name)
        title_section = "<h1>Devops Engineer: Occupation Duties</h1>"
        html_file = open(self.html_list_name).read()
        assert title_section in html_file
        html_file.close()
        self.remove_file()

        
    
        