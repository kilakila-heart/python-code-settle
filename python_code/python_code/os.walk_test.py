# coding:utf-8*
import os
import os.path
for root, dirs, files in os.walk("/outerpan/Lab_CalTech_101/imag/train"):
    # print root
    # print dirs
    print files
    print dirs
    for name in files:
        print root + '/' + name
