def find_files(path, expr=None):
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            if expr:
                if expr(dirpath, f):
                    yield os.path.join(dirpath, f)
            else:
                yield os.path.join(dirpath, f)


def is_c_file(dirpath, filename):
    return any([filename.lower().endswith(c) for c in ['.c', '.s']])

