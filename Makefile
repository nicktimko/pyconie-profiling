.PHONY: nb

nb:
	jupyter notebook --JupyterApp.config_file_name=jupyter_notebook_config.py


aiohuff:
	python -m cProfile -o ahuff.profile aiohuffcodes.py \
		http://www.gutenberg.org/cache/epub/28885/pg28885.txt
