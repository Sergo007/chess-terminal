#!/bin/bash

#brew install pyenv
#pyenv install -l
#pyenv install 3.9.5
#pyenv global 3.9.5
python -m pip install --upgrade pip
python -m pip install virtualenv
python -m venv venv
source venv/bin/activate
pip install -r src/requirements.txt
