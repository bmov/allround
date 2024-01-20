import os


def read_file(path):
    if not os.path.isfile(path):
        return None

    f = open(path, 'r')
    data = f.read()
    f.close()
    return data


def write_file(path, txt):
    if not os.path.isfile(path):
        return False

    f = open(path, 'w')
    f.write(txt)
    f.close()
    return True
