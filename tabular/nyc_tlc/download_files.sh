#!/usr/bin/env bash

# check that output directory is supplied
if [[ $1 -eq 0 ]] ; then
    echo 'Must specify output directory e.g. `./download_files.sh <output_dir>`'
    exit 1
fi
wget https://www.dropbox.com/s/qxvp1nxzautn0e0/eval.csv?dl=1 -O $1/eval.csv
wget https://www.dropbox.com/s/ykhvr387m94v0cn/ref.csv?dl=1 -O $1/ref.csv
wget https://www.dropbox.com/s/1afv0x225rm0oc6/test.csv?dl=1 -O $1/test.csv
wget https://www.dropbox.com/s/iuwmlaxcl3xghwg/model.catb?dl=1 -O $1/model/model_extras/model.catb
