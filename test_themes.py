from themes import list_of_duties
from themes import print_duties_to_terminal
from themes import create_html_document

import os
import re



duty_2 = "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members."
duty_3 = "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review."
duty_7 = "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members."
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
        create_html_document(list_of_duties)
        assert os.path.exists(self.html_list_name)
        self.remove_file()

    
    def test_html_doc_includes_title(self):
        create_html_document(list_of_duties)
        title_section = "<h1>Devops Engineer: Occupation Duties</h1>"
        with open(self.html_list_name) as html_file:
            assert title_section in html_file.read()
        self.remove_file()
    
    def test_html_doc_includes_duties_as_list_element(self):
        
        def list_element(duty):
            return f"<li>{duty}</li>" 
        
        create_html_document(list_of_duties) 
        with open(self.html_list_name) as html_file:
            file_contents = html_file.read()
            assert list_element(duty_2) in file_contents
            assert list_element(duty_3) in file_contents
            assert list_element(duty_13) in file_contents
        self.remove_file()

    def test_ul_tags_in_file_contents(self):
        create_html_document(list_of_duties)
        with open(self.html_list_name) as html_file:
            file_contents = html_file.read()
            assert "<ul>" in file_contents
            assert "</ul>" in file_contents
        self.remove_file()
    
    def test_html_file_contains_two_ul_tags(self):
        create_html_document(list_of_duties)
        with open(self.html_list_name) as html_file:
            file_contents = html_file.read()
            assert file_contents.count("<ul>") == 1
            assert file_contents.count("</ul>") == 1
        self.remove_file()
    
    def _test_html_file_contains_26_li_tags(self):
        create_html_document(list_of_duties)
        with open(self.html_list_name) as html_file:
            file_contents = html_file.read()
            assert file_contents.count("<li>") == 13
            assert file_contents.count("</li>") == 13
        self.remove_file()
    

        
    def test_remove_file_if_still_exists(self):
        self.remove_file()
        
    

        
    
        