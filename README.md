# Downloading the PhysioNet 2019 Sepsis Dataset
This repository contains scripts for downloading and reformatting the data used in the 2019 PhysioNet Sepsis prediction challenge. 

First create a folder at ``data/sepsis/raw`` (symlink if needed, the raw data is around 300mb and the reformatted 500mb). Run the script ``src.data.sepsis.download`` followed by ``src.data.sepsis.convert_data``. This will create a dataframe in ``data/sepsis/interim/df.pkl`` containing the raw data. 

Some (very) brief example notebooks are given in ``notebooks`` that can be used once the data has been downloaded and converted. 
