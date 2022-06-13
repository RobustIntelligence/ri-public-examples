#!/usr/bin/env bash
wget https://www.dropbox.com/s/80lk5l2ycsu432w/eval.csv?dl=1 -O $1/eval.csv
wget https://www.dropbox.com/s/ioac4g66l3gunzt/ref.csv?dl=1 -O $1/ref.csv
wget https://www.dropbox.com/s/riq51qxgjw4dfne/test.csv?dl=0 -O $1/test.csv
wget https://www.dropbox.com/s/cvk8q1ce3ad98w0/model.catb?dl=1 -O $1/model/model_extras/model.catb
