# -*- coding: utf-8 -*-
import os
class PASCALContextSegDataLayer(self):
    """
    Load (input image, label image) pairs from PASCAL-Context
    one-at-a-time while reshaping the net to preserve dimensions.

    The labels follow the 59 class task defined by

        R. Mottaghi, X. Chen, X. Liu, N.-G. Cho, S.-W. Lee, S. Fidler, R.
        Urtasun, and A. Yuille.  The Role of Context for Object Detection and
        Semantic Segmentation in the Wild.  CVPR 2014.

    Use this to feed data to a fully convolutional network.
    """

    def setup(self, bottom, top):
        """
        Setup data layer according to parameters:

        - voc_dir: path to PASCAL VOC dir (must contain 2010)
        - context_dir: path to PASCAL-Context annotations
        - split: train / val / test
        - randomize: load in random order (default: True)
