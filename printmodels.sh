#!/bin/bash
cur_date=$(date)
parent_dir=${PWD%/*}
source ${parent_dir}/bin/activate
python manage.py printmodels 2>"${cur_date}.log"
deactivate

