# -*- coding: utf-8 -*-

# Max-Planck-Gesellschaft zur Förderung der Wissenschaften e.V. (MPG) is
# holder of all proprietary rights on this computer program.
# You can only use this computer program if you have closed
# a license agreement with MPG or you get the right to use the computer
# program from someone who is authorized to grant you that right.
# Any use of the computer program without a valid license is prohibited and
# liable to prosecution.
#
# Copyright©2019 Max-Planck-Gesellschaft zur Förderung
# der Wissenschaften e.V. (MPG). acting on behalf of its Max Planck Institute
# for Intelligent Systems. All rights reserved.
#
# Contact: ps-license@tuebingen.mpg.de

from lib.dataset import Dataset3D
from lib.core.config import MOVI_DIR

class MoVi(Dataset3D):
    def __init__(self, set, seqlen, overlap=0.5, debug=False):
        db_name = 'movi'

        # during testing we don't need data augmentation
        # but we can use it as an ensemble
        is_train = set == 'train' or set == 'all'
        overlap = overlap if is_train else 0.
        print(f'{db_name} Dataset overlap ratio: ', overlap)
        super(MoVi, self).__init__(
            set=set,
            folder=MOVI_DIR,
            seqlen=seqlen,
            overlap=overlap,
            dataset_name=db_name,
            debug=debug,
        )
        print(f'{db_name} - number of dataset objects {self.__len__()}, setting :{set}')