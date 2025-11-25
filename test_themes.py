from themes import print_duties_to_terminal
from themes import create_html_document
from duties_and_names import *

import os

class TestPrintFunction:
    def test_check_capsys(self, capsys):
        print_duties_to_terminal(all_duties)
        captured = capsys.readouterr()

        assert duty_3.plainText() in captured.out
        assert duty_8.plainText() in captured.out
        assert duty_13.plainText() in captured.out

title_section = "<h1>Devops Engineer: Occupation Duties</h1>"

def remove_file(filename):
        if os.path.exists(filename):
            os.remove(filename)
            

class TestCreateHTMLDocumentAllDuties:
    
    def test_html_doc_is_created(self):
        create_html_document(html_file_name, all_duties)
        assert os.path.exists(html_file_name)
        remove_file(html_file_name)

    
    def test_html_doc_includes_title(self):
        create_html_document(html_file_name, all_duties)
        with open(html_file_name) as html_file:
            assert title_section in html_file.read()
        remove_file(html_file_name)
    
    def test_html_doc_includes_duties_as_list_element(self):
               
        create_html_document(html_file_name, all_duties) 
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert duty_2.htmlListElement() in file_contents
            assert duty_3.htmlListElement() in file_contents
            assert duty_3.htmlListElement() in file_contents
        remove_file(html_file_name)

    def test_ul_tags_in_file_contents(self):
        create_html_document(html_file_name, all_duties)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert "<ul>" in file_contents
            assert "</ul>" in file_contents
        remove_file(html_file_name)
    
    def test_html_file_contains_two_ul_tags(self):
        create_html_document(html_file_name, all_duties)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert file_contents.count("<ul>") == 1
            assert file_contents.count("</ul>") == 1
        remove_file(html_file_name)
    
    def _test_html_file_contains_26_li_tags(self):
        create_html_document(html_file_name, all_duties)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert file_contents.count("<li>") == 13
            assert file_contents.count("</li>") == 13
        remove_file(html_file_name)
    

    def test_remove_file_if_still_exists(self):
        remove_file(html_file_name)
        assert not os.path.exists(html_file_name)
        

class TestCreateHTMLDocumentSpecifiedDuties:
    
    def test_create_html_doc_with_single_duty(self):
        create_html_document(html_file_name, [duty_4])
        assert os.path.exists(html_file_name)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert title_section in file_contents
            assert file_contents.count("<ul>") == 1
            assert file_contents.count("</ul>") == 1
            assert file_contents.count("<li>") == 1
            assert file_contents.count("</li>") == 1
            assert duty_4.htmlListElement() in file_contents
            assert duty_1.htmlListElement() not in file_contents
            assert duty_5.htmlListElement() not in file_contents
        remove_file(html_file_name)
    
    def test_remove_file_if_still_exists(self):
        remove_file(html_file_name)
        assert not os.path.exists(html_file_name)
        
        
        