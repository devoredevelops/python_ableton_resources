import os
import re

from pathlib import Path


path = Path(os.getcwd()).resolve()

for f in path.iterdir():
    if f.name and str(f.name)[1] not in ["1", "2"]:

        f.rename(())


# write a regular expression to catch a group for this sequency of b1, b2, b03:
def regular():
    # create list of strings
    list_of_strings = ["b1 - ", "b11 - ", "b2 - ", "b20 - " "b3 - "]
    # create a regular expression to capture the group of b1, b2, b03
    import re

    if m := re.match(r"b\d{1,2}", list_of_strings, re.I):
        # add leading zero to single digit numbers
        leading_zero = m[1].zfill(2)
