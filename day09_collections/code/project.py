import math
import os
import re
import time
from datetime import date
from pathlib import Path


def pattern_search():
    path = "ProyectoDia9/"
    pattern = r"N[a-zA-Z]{3}-\d{5}"
    pattern_list = []
    for directory, subdirectories, files in os.walk(path):
        subdirectories.sort()
        files.sort()

        for f in files:
            file_path = Path(directory, f)
            with open(file_path, "r") as my_file:
                text = my_file.read()
            match = re.search(pattern, text)
            if match:
                pattern_list.append(f"{f}\t {match.group()}")
    patterns = "\n".join(pattern_list)
    patterns_found = len(pattern_list)
    return patterns, patterns_found


def display_info(today, patterns, patterns_found, duration):
    info = f"""
----------------------------------------------------
Fecha de búsqueda: {today}
ARCHIVO\t\t NRO. SERIE
-------------\t ----------
{patterns}
Números encontrados: {patterns_found}
Duración de la búsqueda: {duration} segundos
----------------------------------------------------
"""
    print(info)


def main():
    start = time.time()
    patterns, patterns_found = pattern_search()
    end = time.time()

    duration = math.ceil(end - start)

    today = date.today()
    today = today.strftime("%Y/%m/%d")
    display_info(today, patterns, patterns_found, duration)


main()
