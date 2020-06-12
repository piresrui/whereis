import os
import re
from typing import List, Callable, Union

from lib.utils import Colors


# TODO
# Add .gitignore capabilities


def create_pattern(pattern: str) -> Callable[[str], Union[List[str], None]]:
    """
    Creates Pattern based on flags
    :param pattern: String with regex pattern
    :return: Pattern matcher
    """

    def match(string_to_split: str) -> Union[List[str], None]:
        """
        Splits string on at max 1 occurence of pattern.
        """
        matches = re.split(f"({pattern})", string_to_split, maxsplit=1)
        return matches if len(matches) > 1 else None

    def match_regular(string_to_match: str) -> Union[List[str], None]:
        """
        If string matches return matcher function.
        Returns nothing if no match
        """
        if pattern in string_to_match:
            return match(string_to_match)

    # Searches through string for non alphanumeric char
    # If match then it is a regex
    if re.search("[^a-zA-Z0-9]", pattern):
        return match
    return match_regular


def walk(src: str, pattern: str, symlinks: bool = False, hidden=False, vcs=False):
    matcher = create_pattern(pattern=pattern)

    """
        Walks given directory in top down fashion, meaning current dir files /
        get returned first.
    """
    for path, directories, files in os.walk(src, topdown=True, followlinks=symlinks):

        if not hidden:
            directories[:] = [f for f in directories if not f.startswith(".")]

        for file in files:
            match = matcher(file)
            if match:
                yield path, file, match


class ColorPrinter:

    @classmethod
    def print(cls, path: str, to_color: str):
        print(os.path.join(path, f"{Colors.GREEN}{to_color}{Colors.ENDC}"))


def run(src, pattern):
    for path, file, _ in walk(src=src, pattern=pattern):
        ColorPrinter.print(path, file)
