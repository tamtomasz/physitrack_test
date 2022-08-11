from typing import Tuple


class Element:

    def __init__(self, find_by, search_str):
        self._find_by = find_by
        self._search_str = search_str

    @property
    def find_by(self):
        return self._find_by

    @property
    def find_str(self):
        return self._search_str

    @property
    def locator(self) -> Tuple[str, str]:
        return self._find_by, self._search_str

