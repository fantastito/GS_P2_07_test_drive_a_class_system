"""
1
Create instaices of entries with entry Class
Add them to instance of diary class
Check that diary.all returns entries

"""

from lib.diary import *
from lib.diary_entry import *

def test_create_and_add_diary_entry():
    diary = Diary()
    entry_1 = DiaryEntry('Test title 1', 'Contents string 1')
    diary.add(entry_1)
    assert diary.all() == [entry_1]