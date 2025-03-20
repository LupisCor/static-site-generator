import os, shutil

def copy_static(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    
    lst = os.listdir(src)
    for pth in lst:
        from_path = os.path.join(src, pth)
        to_path = os.path.join(dst, pth)

        print(f" * {from_path} -> {to_path}")

        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_static(from_path, to_path)