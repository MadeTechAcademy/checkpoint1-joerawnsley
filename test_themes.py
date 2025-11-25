from themes import print_duties_to_terminal
from themes import create_html_document
from duties import *

import os

class TestPrintFunction():
    def test_check_capsys(self, capsys):
        print_duties_to_terminal()
        captured = capsys.readouterr()

        assert duty_3.plainText() in captured.out
        assert duty_8.plainText() in captured.out
        assert duty_13.plainText() in captured.out


class TestCreateHTMLDocument():
    html_list_name = "list_of_duties.html"
    
    def remove_file(self):
        if os.path.exists(self.html_list_name):
            os.remove(self.html_list_name)
            assert not os.path.exists(self.html_list_name)
    
    def test_html_doc_is_created(self):
        create_html_document(all_duties)
        assert os.path.exists(self.html_list_name)
        self.remove_file()

    
    def test_html_doc_includes_title(self):
        create_html_document(all_duties)
        title_section = "<h1>Devops Engineer: Occupation Duties</h1>"
        with open(self.html_list_name) as html_file:
            assert title_section in html_file.read()
        self.remove_file()
    
    def test_html_doc_includes_duties_as_list_element(self):
               
        create_html_document(all_duties) 
        with open(self.html_list_name) as html_file:
            file_contents = html_file.read()
            assert duty_2.htmlListElement() in file_contents
            assert duty_3.htmlListElement() in file_contents
            assert duty_3.htmlListElement() in file_contents
        self.remove_file()

    def test_ul_tags_in_file_contents(self):
        create_html_document(all_duties)
        with open(self.html_list_name) as html_file:
            file_contents = html_file.read()
            assert "<ul>" in file_contents
            assert "</ul>" in file_contents
        self.remove_file()
    
    def test_html_file_contains_two_ul_tags(self):
        create_html_document(all_duties)
        with open(self.html_list_name) as html_file:
            file_contents = html_file.read()
            assert file_contents.count("<ul>") == 1
            assert file_contents.count("</ul>") == 1
        self.remove_file()
    
    def _test_html_file_contains_26_li_tags(self):
        create_html_document(all_duties)
        with open(self.html_list_name) as html_file:
            file_contents = html_file.read()
            assert file_contents.count("<li>") == 13
            assert file_contents.count("</li>") == 13
        self.remove_file()
    

        
    def test_remove_file_if_still_exists(self):
        self.remove_file()
        
    

        
    
        