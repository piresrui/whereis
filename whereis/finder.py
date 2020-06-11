import os
import re


# TODO
# Add .gitignore capabilities


def create_pattern(pattern: str) -> re.Pattern:
    """
    Creates Pattern based on flags
    :param pattern: String with regex pattern
    :return: Pattern matcher
    """
    try:
        return re.compile(pattern)
    except re.error as e:
        # TODO add proper error matching
        print(e)
        raise Exception("Failed pattern create")


def walk(dir: str, pattern: str, symlinks: bool = False, hidden=False, vcs=False):
    regex = re

    """
        Walks given directory in top down fashion, meaning current dir files /
        get returned first.
    """
    for path, directories, files in os.walk(dir, topdown=True, followlinks=symlinks):

        if not hidden:
            directories[:] = [f for f in directories if not f.startswith(".")]

        print(path, directories, files)
