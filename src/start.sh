#! /bin/bash
set -xe

python ./manage.py db upgrade
python run.py
