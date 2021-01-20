import re
import pandas
rx_dict = {
    'school': re.compile(r'School = (?P<school>.*)\n'),
    'grade': re.compile(r'Grade = (?P<grade>\d+)\n'),
    'name_score': re.compile(r'(?P<name_score>Name|Score)'),
}
