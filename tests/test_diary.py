"""
1
Create instances of entries with entry Class
Add them to instance of diary class
Check that diary.all returns entries

"""

from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_create_and_add_diary_entry():
    diary = Diary()
    entry_1 = DiaryEntry('Test title 1', 'Contents string 1')
    diary.add(entry_1)
    assert diary.all() == [entry_1]


"""
2
Create instances of entries with entry Class
Add them to instance of diary class
Check work count of all entries

"""
def test_check_word_count():
    diary = Diary()
    for i in range(8):
        diary.add(DiaryEntry(f'Title {i}', f'Contents {i}'))
    actual_result = diary.count_words()
    expected_result = 16
    assert actual_result == expected_result

"""
3
Create instances of entries with entry Class
Add them to instance of diary class
Check the reading time for all diary entries

"""
def test_check_reading_time():
    diary = Diary()
    for i in range(8):
        diary.add(DiaryEntry(f'Title {i}', f'Contents {i}'))
    actual_result = diary.reading_time(2)
    expected_result = 8
    assert actual_result == expected_result

"""
4
Create instances of entries with entry Class
Add them to instance of diary class
Decide reading time and wpm, 
return the most time appropriate diary entry

"""
def test_check_best_entry_for_reading_time():
    diary = Diary()
    for i in range(8):
        diary.add(DiaryEntry(f'Title {i + 1}', f'Contents {i + 1} ' * (i + 1)))
    actual_result = diary.reading_time(2)
    expected_result = 8
    assert actual_result == expected_result