# vlna - Czech typography tool
Vlna is used to replace spaces between words with non-breaking spaces in Czech language texts.
The idea is based on [vlna](http://ftp.linux.cz/pub/tex/local/cstug/olsak/vlna/) tool written by  Petr Olšák.

## Installation
```bash
python3 vlna.py AaIiKkSsVvUuOoZz0123456789 < input.tex > output.tex
```
- `AaIiKkSsVvUuOoZz0123456789` - add ~ after these characters (optional)
- input.tex - input file
- output.tex - output file (optional) - if not set, output is printed to stdout


## Example
Replace file will be printed to stdout.
```bash
python3 vlna.py AaIiKkSsVvUuOoZz0123456789 < ./test-data/soc/test.tex
```

Replace file will be saved to `test_output_soc.tex`.
```bash
python3 vlna.py AaIiKkSsVvUuOoZz0123456789 < ./test-data/soc/test.tex > test_output_soc.tex
```