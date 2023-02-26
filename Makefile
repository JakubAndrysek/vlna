test:
	python3 -m unittest -v test/test_vlna.py

example_stdout:
	python3 vlna.py AaIiKkSsVvUuOoZz0123456789 < ./test-data/soc/test.tex

example_output_file:
	python3 vlna.py AaIiKkSsVvUuOoZz0123456789 < ./test-data/soc/test.tex > test_output_soc.tex