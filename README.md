# IDS706-Python-Data-Science-YuhanXue

![format workflow](https://github.com/nogibjj/IDS706-Python-Data-Science-YuhanXue/actions/workflows/format.yml/badge.svg)
![install workflow](https://github.com/nogibjj/IDS706-Python-Data-Science-YuhanXue/actions/workflows/install.yml/badge.svg)
![lint workflow](https://github.com/nogibjj/IDS706-Python-Data-Science-YuhanXue/actions/workflows/lint.yml/badge.svg)
![test workflow](https://github.com/nogibjj/IDS706-Python-Data-Science-YuhanXue/actions/workflows/test.yml/badge.svg)

### Youtube link
Project walkthrough: [link](link)

### Project Overview
- stats.ipynb: show descriptive statistics on diabetes.csv and plot distributino graphs.
- stats.py: show descriptive statistics on diabetes.csv and plot distributino graphs.
- lib.py: shared functions used across stats.ipynb and stats.py.
- Makefile:
  - Install packages in requirements.txt
  - Lints code with Ruff
  - Format with Python black
  - Run tests
- test_script.py: test the correctness of functions in stats.py
- test_lib.py: test the correctness of functions in lib.py
- requirements.txt: Python packages required to support all functions.