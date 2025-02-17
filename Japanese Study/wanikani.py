import requests

def wanikani(phrase):
    url = 'https://api.wanikani.com/v2/subjects'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer xxxx'
    }

    params = {
        'slugs': phrase,
        'types': 'kanji,vocabulary'
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if data['total_count'] > 0:
        subject = data['data'][0]['data']
        meanings = get_on_meaning(subject['meanings'])
        on_readings = get_on_readings(subject['readings'])
        kun_readings = get_kun_readings(subject['readings'])
        document_url = subject['document_url']
        return meanings, on_readings, kun_readings, document_url


def get_on_meaning(data):
    meanings = []

    for meaning in data:
        meanings.append(meaning['meaning'].lower())

    return meanings


def get_on_readings(data):
    readings = []

    for reading in data:
        try:
            if reading['type'] == 'onyomi':
                readings.append(reading['reading'])
        except:
            readings.append(reading['reading'])

    return readings


def get_kun_readings(data):
    readings = []

    for reading in data:
        try:
            if reading['type'] == 'kunyomi':
                readings.append(reading['reading'])
        except:
            return None

    return readings


# 得
