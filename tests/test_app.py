from app import print_duties_to_terminal
from app import create_html_document
from data.themes import *
from data.filenames import html_file_name

import os

class TestPrintFunction:
    def test_check_print_output(self, capsys):
        print_duties_to_terminal(full_apprenticeship)
        captured = capsys.readouterr()

        assert duty_3.plainText() in captured.out
        assert duty_8.plainText() in captured.out
        assert duty_13.plainText() in captured.out
    
    def test_check_print_output_specified_duties_only(self, capsys):
        print_duties_to_terminal(automate)
        captured = capsys.readouterr()
        
        assert duty_5.plainText() in captured.out
        assert duty_7.plainText() in captured.out
        assert duty_10.plainText() in captured.out   
        assert duty_1.plainText() not in captured.out
        assert duty_8.plainText() not in captured.out
        assert duty_13.plainText() not in captured.out
    
    def test_check_print_output_bootcamp_duties(self, capsys):
        print_duties_to_terminal(bootcamp)
        captured = capsys.readouterr()

        assert duty_1.plainText() in captured.out
        assert duty_3.plainText() in captured.out
        assert duty_13.plainText() in captured.out
        assert duty_8.plainText() not in captured.out
        assert duty_10.plainText() not in captured.out
    
    def test_check_print_output_security_duties(self, capsys):
        print_duties_to_terminal(security)
        captured = capsys.readouterr()

        assert duty_9.plainText() in captured.out
        assert duty_3.plainText() not in captured.out
        assert duty_13.plainText() not in captured.out
        assert duty_8.plainText() not in captured.out
        assert duty_1.plainText() not in captured.out
    
        
        

title_section = "<h1>Devops Engineer: Occupation Duties</h1>"

def remove_file(filename):
        if os.path.exists(filename):
            os.remove(filename)
            

class TestCreateHTMLDocumentAllDuties:
    
    def test_html_doc_is_created(self):
        create_html_document(html_file_name, full_apprenticeship)
        assert os.path.exists(html_file_name)
        remove_file(html_file_name)

    
    def test_html_doc_includes_title(self):
        create_html_document(html_file_name, full_apprenticeship)
        with open(html_file_name) as html_file:
            assert title_section in html_file.read()
        remove_file(html_file_name)
    
    def test_html_doc_includes_duties_as_list_element(self):
               
        create_html_document(html_file_name, full_apprenticeship) 
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert duty_2.htmlListElement() in file_contents
            assert duty_3.htmlListElement() in file_contents
            assert duty_3.htmlListElement() in file_contents
        remove_file(html_file_name)

    def test_ul_tags_in_file_contents(self):
        create_html_document(html_file_name, full_apprenticeship)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert "<ul>" in file_contents
            assert "</ul>" in file_contents
        remove_file(html_file_name)
    
    def test_html_file_contains_two_ul_tags(self):
        create_html_document(html_file_name, full_apprenticeship)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert file_contents.count("<ul>") == 1
            assert file_contents.count("</ul>") == 1
        remove_file(html_file_name)
    
    def _test_html_file_contains_26_li_tags(self):
        create_html_document(html_file_name, full_apprenticeship)
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
        create_html_document(html_file_name, deeper)
        assert os.path.exists(html_file_name)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert title_section in file_contents
            assert file_contents.count("<ul>") == 1
            assert file_contents.count("</ul>") == 1
            assert file_contents.count("<li>") == 1
            assert file_contents.count("</li>") == 1
            assert duty_11.htmlListElement() in file_contents
            assert duty_1.htmlListElement() not in file_contents
            assert duty_5.htmlListElement() not in file_contents
        remove_file(html_file_name)
    
    def test_create_html_doc_with_houston_duties(self):
        create_html_document(html_file_name, houston)
        assert os.path.exists(html_file_name)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert title_section in file_contents
            assert file_contents.count("<ul>") == 1
            assert file_contents.count("</ul>") == 1
            assert file_contents.count("<li>") == 4
            assert file_contents.count("</li>") == 4
            assert duty_6.htmlListElement() in file_contents
            assert duty_7.htmlListElement() in file_contents
            assert duty_10.htmlListElement() in file_contents
            assert duty_12.htmlListElement() in file_contents
            assert duty_2.htmlListElement() not in file_contents
            assert duty_8.htmlListElement() not in file_contents
            assert duty_13.htmlListElement() not in file_contents    
        remove_file(html_file_name)
        
    def test_create_html_doc_with_bootcamp_duties(self):
        create_html_document(html_file_name, bootcamp)
        assert os.path.exists(html_file_name)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert title_section in file_contents
            assert file_contents.count("<ul>") == 1
            assert file_contents.count("</ul>") == 1
            assert file_contents.count("<li>") == 5
            assert file_contents.count("</li>") == 5
            assert duty_1.htmlListElement() in file_contents
            assert duty_3.htmlListElement() in file_contents
            assert duty_13.htmlListElement() in file_contents
            assert duty_5.htmlListElement() not in file_contents
            assert duty_7.htmlListElement() not in file_contents
            assert duty_10.htmlListElement() not in file_contents    
        remove_file(html_file_name)
        
    def test_create_html_doc_with_assemble_duties(self):
        create_html_document(html_file_name, assemble)
        assert os.path.exists(html_file_name)
        with open(html_file_name) as html_file:
            file_contents = html_file.read()
            assert title_section in file_contents
            assert file_contents.count("<ul>") == 1
            assert file_contents.count("</ul>") == 1
            assert file_contents.count("<li>") == 1
            assert file_contents.count("</li>") == 1
            assert duty_8.htmlListElement() in file_contents
            assert duty_1.htmlListElement() not in file_contents
            assert duty_7.htmlListElement() not in file_contents
            assert duty_9.htmlListElement() not in file_contents    
        remove_file(html_file_name)
    
    def test_remove_file_if_still_exists(self):
        remove_file(html_file_name)
        assert not os.path.exists(html_file_name)
        
        
        