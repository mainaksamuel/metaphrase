#!/usr/bin/env python3

import requests


def get_translation(source_language: str, target_language: str, text):

    url = "https://translate.google.com/translate_a/single?client=at&dt=t&" \
        "dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=" + target_language + "&ie=UTF-8" \
        "&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"

    payload = 'sl=' + source_language + '&tl=' + target_language + '&q=' + text

    headers = {
        'User-Agent': 'AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        translation = response.json()
    except Exception:
        print("Could not get a valid response. Perhaps the API has changed.")
    finally:
        response.close()

    return translation
