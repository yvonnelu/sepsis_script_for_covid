import sys
sys.path.append('../../../')

import os
from io import BytesIO
import requests
import zipfile
from urllib.request import urlopen


def main():
    base_dir = '../../../data/sepsis/raw'
    assert os.path.isdir(base_dir), 'Please make a directory at {ROOT}/data/sepsis/raw'

    # Two save dirs
    save_loc_a = base_dir + '/raw/training_set_A'
    save_loc_b = base_dir + '/raw/training_setB'
    url_a = 'https://archive.physionet.org/users/shared/challenge-2019/training_setA.zip'
    url_b = 'https://archive.physionet.org/users/shared/challenge-2019/training_setB.zip'

    locs = [(save_loc_a, url_a), (save_loc_b, url_b)]

    for save_loc, url in locs:
        if os.path.exists(save_loc):
            continue

        if not os.path.exists(save_loc):
            r = urlopen(url)
            z = zipfile.ZipFile(BytesIO(r.read()))
            z.extractall(base_dir)


if __name__ == '__main__':
    main()
