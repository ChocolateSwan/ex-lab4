#!/usr/bin/env python3
from math import fabs
from librip.decorators import print_result
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
print(sorted(data, key = fabs), end = ' ')