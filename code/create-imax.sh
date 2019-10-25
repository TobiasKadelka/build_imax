#!/usr/bin/env bash

# This script creates the imax-dataset.

# create a dataset and go into that Folder.
datalad create -c bids $1/IMAX
cd $1/IMAX

datalad install -d . -s git@github.com:TobiasKadelka
/build_imax.git code/build_imax
datalad save code -m "installed the code for creating the DTA-dataset as a bids-dataset."
