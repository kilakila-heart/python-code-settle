import os

def compress_img(dir):
    for f in os.listdir(dir):
        _f = dir+'/'+f;
        if os.path.isdir(_f):
            scandir(_f)
        else:
            if os.path.isfile(_f):
                _ext = _f.split('.')[-1].lower();
                if _ext == 'png' or _ext == 'jpg' or _ext == 'jpeg' or _ext == 'gif':
                    print 'convert '+_f+' -quality 10 '+_f
                    os.system('convert '+_f+' -quality 10 '+_f)
    pass

print compress_img("1")
