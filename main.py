from utils.utils import output, sorted_by_datetime, get_transactions
from utils.constants import JSON_DATA_PATH

for ele in reversed(range(len(sorted_by_datetime(JSON_DATA_PATH)))):
    output(sorted_by_datetime(JSON_DATA_PATH)[ele])
