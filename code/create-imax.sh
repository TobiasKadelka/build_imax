#!/usr/bin/env bash

# This script creates the imax-dataset.

# create a dataset and go into that Folder.
datalad create -c bids $1/IMAX
cd $1/IMAX

# install the build-repo
datalad install -d . -s git@github.com:TobiasKadelka/build_imax.git code/build_imax
datalad save code -m "installed the code for creating the dataset."

python ./code/build_imax/code/create-imax.sh /data/BnB1/DATA/download_data/Zhou/IMAX/ > ./code/build_imax/code/convert.sh
chmod 775 ./code/build_imax/code/convert.sh
./code/build_imax/code/convert.sh
datalad save -r -m "creating the contents of the dataset."
