import random
import csv

PHRASE = 0
SRS = 1
TAG = 2
ALL = 'All'
WORDS_FILE_PATH = 'words.csv'

def get_random_words(contains, tag):
    rows = []

    with open(WORDS_FILE_PATH, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) # skip the header

        for row in reader:
            if contains in str(row) and (tag == ALL or tag.lower() == row[TAG].strip()):
                rows.append(row)

    random.shuffle(rows)

    return [row for row in rows]


def mark_answer(phrase, is_correct):
    mark = 'X'

    if is_correct:
        mark = '✓'

    with open(WORDS_FILE_PATH, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        rows = list(csv_reader)

    with open(WORDS_FILE_PATH, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=',', lineterminator='')

        for row in rows:
            if row[0] == phrase:
                row[4] += mark

            csv_writer.writerow(row)

            if row != rows[-1]:
                csv_writer.writerow('\n')
