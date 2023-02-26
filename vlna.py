import sys
import re

# Description of the algorithm:
# Vlna is used to replace spaces between words with non-breaking spaces in Czech language texts.
# 1. Replace all spaces after prefixes with tilde (~)
# 2. Replace all spaces after prefixes at the end of line with tilde (~) and newline (\n)

def vlna(input_string: str, prefixes: str = "AaIiKkSsVvUuOoZz0123456789") -> str:
    def change_inline_regex(input_string: str, prefixes: str):
        # https://regex101.com/r/M9eVqS/1
        regex = r"\b([" + prefixes + "])[ ]+(?=\w)"
        subst = "\\g<1>~"
        return re.sub(regex, subst, input_string, 0, re.MULTILINE)

    def change_end_of_line_regex(input_string: str, prefixes: str):
        # https://regex101.com/r/w86443/3
        regex = r"\b([" + prefixes + "])[ ]*\n[ ]*^"
        subst = "\\g<1>~\\n"
        return re.sub(regex, subst, input_string, 0, re.MULTILINE)

    inline_changes = change_inline_regex(input_string, prefixes)
    end_of_line_changes = change_end_of_line_regex(inline_changes, prefixes)

    return end_of_line_changes

if __name__ == '__main__':
    # python vlna.py AaIiKkSsVvUuOoZz0123456789 < input.tex > output.tex
    if len(sys.argv) > 1:
        prefixes = sys.argv[1]
    else:
        print("Usage: python vlna.py AaIiKkSsVvUuOoZz0123456789 < input.tex > output.tex")
        print("No prefixes given as argument, using default prefixes: AaIiKkSsVvUuOoZz0123456789")
        prefixes = "AaIiKkSsVvUuOoZz0123456789"

    input_string = sys.stdin.read()
    result:str = vlna(input_string, prefixes)

    if result:
        print(result)