from unittest import TestCase
from vlna import vlna


class Test(TestCase):
    def test_vlna_empty(self):
        input_string = ""
        result = vlna(input_string)
        self.assertEqual(result, "")
    def test_vlna_do_nothing(self):
        input_string = "Systém se skládá ze senzorové části"
        result = vlna(input_string)
        self.assertEqual(result, "Systém se skládá ze senzorové části")

    def test_vlna_inline(self):
        input_string = "stará o aktualizaci a o kontrolu správného chodu senzorů"
        result = vlna(input_string)
        self.assertEqual(result, "stará o~aktualizaci a~o~kontrolu správného chodu senzorů")

    def test_vlna_end_of_line_basic(self):
        input_string = ("chodu senzorů a\n"
                        "tady")
        result = vlna(input_string)
        self.assertEqual(result, ("chodu senzorů a~tady"))

    def test_vlna_end_of_line_advanced(self):
        input_string = ("chodu senzorů a\n"
                        " tady a\n"
                        "tu jsem.\n"
                        "Kolik je hodin u \n"
                        " nás doma.")
        result = vlna(input_string)
        self.assertEqual(result, ("chodu senzorů a~tady a~tu jsem.\n"
                                    "Kolik je hodin u~nás doma."))

    def vlna_test_folder(self, folder_name: str):
        # remove / from string
        folder_name = folder_name.replace("/", "")
        # open file with name test.tex and process it
        with open(f"test-data/{folder_name}/test.tex") as f:
            input_string = f.read()
        result = vlna(input_string)
        # compare result with file result.tex
        with open(f"test-data/{folder_name}/result.tex") as f:
            expected = f.read()
        self.assertEqual(result, expected)

    def test_vlna_document_soc(self):
        self.vlna_test_folder("soc")

    def test_vlna_document_pohadka(self):
        self.vlna_test_folder("pohadka")