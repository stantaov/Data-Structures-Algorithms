from os import listdir
from os.path import isfile, join, isdir



def find_files(suffix, path):
    """
    This function takes a path and suffix and 
    finds all files with specified suffix

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []
    dirs = []
    if isdir(path) is False:
        return False
    else:
        for file in listdir(path):
            if isfile(join(path, file)) and file.endswith(suffix):
                files.append(join(path, file))
        for dir in listdir(path):
            if isdir(join(path, dir)):
                dirs.append(dir)
    
        for dir in dirs:
            output =  find_files(suffix, join(path,dir))
            if output:
                for file in output:
                    if file.endswith(suffix):
                        files.append(join(path, file))

    return files


if __name__ == "__main__":

    # Test 1 (finding files with .c extension in the testdir)
    print("Test 1 (finding files with .c extension in the testdir)")
    suffix = ".c"
    path = "/Users/stanislav/Downloads/testdir"
    print(find_files(suffix, path))
    assert find_files(suffix, path) == ['/Users/stanislav/Downloads/testdir/t1.c','/Users/stanislav/Downloads/testdir/subdir3/subsubdir1/b.c', '/Users/stanislav/Downloads/testdir/subdir5/a.c', '/Users/stanislav/Downloads/testdir/subdir1/a.c']
    print("#"*60)
    # Test 2 (no path, should return False)
    print("Test 2 (no path, should return False)")
    suffix = ".c"
    path = ""
    print(find_files(suffix, path))
    assert find_files(suffix, path) == False 
    print("#"*60)
    # Test 3 (finding fiels with .com extension in the testdir, should return empty list)
    print("Test 3 (finding fiels with .com extension in the testdir, should return empty list)")
    suffix = ".com"
    path = "/Users/stanislav/Downloads/testdir"
    print(find_files(suffix, path))
    assert find_files(suffix, path) == []
    print("#"*60)