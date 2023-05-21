from utils.utils import output, sorted_by_datetime

for l in reversed(range(len(sorted_by_datetime()))):
    output(sorted_by_datetime()[l])