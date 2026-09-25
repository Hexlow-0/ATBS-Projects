
import re

sentences = [
    "The meeting is on 03/15/2024 at noon.",
    "No date here.",
    "Her birthday is 11/02/1998, I think.",
]

date_match = re.compile('(\d\d)/(\d\d)/(\d\d\d\d)')

look_up_month = {1: 'Jan',
                2: 'Feb',
                3: 'Mar',
                4: 'Apr',
                5: 'May',
                6: 'Jun',
                7: 'Jul',
                8: 'Aug',
                9: 'Sep',
                10: 'Oct',
                11: 'Nov',
                12: 'Dec'
                }

for char in sentences:

    match = date_match.search(char)

    if match:
        month_num = int(match.group(1))
        print(f"Month: {look_up_month.get(month_num, month_num)} | Date: {match.group(2)} | Year: {match.group(3)}")
    else:
        print("No dates found")

