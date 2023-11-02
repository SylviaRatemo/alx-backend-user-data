#!/usr/bin/env python3
"""
filtered_logger.py
Task 0: Regex-int
"""
import re
from typing import List


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}

def filter_datum(fields: List[str], redaction:str, message:str, separator:str) -> str:
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(map(re.escape, fields), re.escape(separator)), replace(redaction), message)
