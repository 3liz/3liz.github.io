#!/usr/bin/env python3

import json

from datetime import date
from os import path
from sys import argv

import requests

# This script downloads the statistics of localization of the project from Transifex.
# To be able to use it, you need to provide your user account token
# and run `python3 scripts/load_tx_stats.py <TX_TOKEN>` from the repo main folder.
# See https://transifex.github.io/openapi/index.html

LANGUAGE_MAP = {
    'bg': '🇧🇬',
    'cs': '🇨🇿',
    'da': '🇳🇱',
    'de': '🇩🇪',
    'el': '🇬🇷',
    'es': '🇪🇸',
    'es_AR': '🇦🇷',
    'fi': '🇫🇮',
    'fr': '🇫🇷',
    'he': '🇮🇱',
    'hu_HU': '🇭🇺',
    'id': '🇮🇩',
    'it': '🇮🇹',
    'ja': '🇯🇵',
    'ko': '🇰🇷',
    'nl': '🇳🇱',
    'no': '🇳🇴',
    'pl': '🇵🇱',
    'pl_PL': '🇵🇱',
    'pt': '🇵🇹',
    'pt_BR': '🇧🇷',
    'ro': '🇷🇴',
    'ru': '🇷🇺',
    'sk': '🇸🇰',
    'sl': '🇸🇮',
    'sr@Cyrl': '🇷🇸',
    'sv_SE': '🇸🇪',
    'uk_UA': '🇺🇦',
    'vi': '🇻🇳',
    'zh': '🇨🇳',
    'zh_TW': '🇹🇼',
}

# Catch the Transifex api token value (passed as argument to the python command)
if len(argv) <= 1:
    print("Missing transifex token argument")
    exit(1)

TX_TOKEN = argv[1]
#
# if len(argv) == 4:
#     ORGANIZATION = argv[2]
#     PROJECT = argv[3]
# else:
#     ORGANIZATION = 'qgis'
#     PROJECT = 'qgis-documentation'

ORGANIZATION = '3liz-1'
PROJECT = 'lizmap-locales'

headers = {'Authorization': f'Bearer {TX_TOKEN}'}
project_id = f"o:{ORGANIZATION}:p:{PROJECT}"

# Load target languages of the QGIS Documentation project from transifex
target_languages = requests.get(
    f"https://rest.api.transifex.com/projects/{project_id}/languages",
    headers=headers
    )
target_languages = target_languages.json()
# Where we store statistics of each language
language_rate = {}

# Fetch list of languages
for lang in target_languages['data']:
    code = lang['attributes']['code']
    language_rate[code] = {'name': lang['attributes']['name']}

# Add English to the list
language_rate['en'] = {'name': 'English'}
# print(language_rate, ' counts ', len(language_rate))

# Extract statistics for every single available languages,
# namely their number of translated strings
for lang in language_rate:
    # print('LANG  ', language_rate[lang]['name'])
    translated_strings = 0
    total_strings = 0

    resource_language_stats = requests.get(
        f"https://rest.api.transifex.com/resource_language_stats?"
        f"filter[project]={project_id}&filter[language]=l:{lang}",
        headers=headers)
    resource_language_stats = resource_language_stats.json()

    all_resources = resource_language_stats['data']

    # Walk through pagination
    while 'next' in resource_language_stats['links'].keys():
        resource_language_stats = requests.get(
            resource_language_stats['links']['next'],
            headers=headers
            ).json()
        all_resources.extend(resource_language_stats['data'])

    for resource in all_resources:
        translated_strings += resource['attributes']['translated_strings']
        total_strings += resource['attributes']['total_strings']

    language_rate[lang]['translated_strings'] = translated_strings
    language_rate[lang]['percentage'] = round(
        translated_strings * 100 / total_strings, 2)
    # Keep total count of available strings in 'en' only,
    # no need to store multiple times
    if lang == 'en':
        language_rate[lang]['total_strings'] = total_strings

# print(language_rate)

# Sort by language name for a better display in docs
language_rate = {k: v for k, v in sorted(
    language_rate.items(),
    key=lambda item: item[1]['percentage'], reverse=True)
}

# Stats for the whole project (== English source language)
# Number of target translation languages declared in Transifex for the project
nb_languages = len(language_rate) - 1
# Total number of strings in English to translate
total_strings = language_rate['en']['total_strings']
# translation percentage of the whole project, let's not count 'en'
total_translated_strings = sum(
    language_rate[lang]['translated_strings']
    for lang in language_rate if lang != 'en')
global_percentage = round(
    total_translated_strings*100/(total_strings * nb_languages), 2)

language_rate['en'].update(
    {'nb_languages': nb_languages,
     'translated_strings': total_translated_strings,
     'percentage': global_percentage
     }
    )

# print('all ', language_rate)


def load_overall_stats():
    """Format statistics of translation in the project"""

    text = (
        f"""
| Number of strings | Number of target languages | Overall Translation ratio |
|:-:|:-:|:-:|
{total_strings}|{nb_languages}|{global_percentage}
""")
    return text


def load_lang_stats(target_langs):
    """Format statistics of translated languages into a multi-column table"""

    text = "| Language | Translation ratio (%) |"
    text += "\n|:-:|:-:|\n"

    for lang in target_langs:
        if lang == 'en':
            continue

        text += f"{target_langs[lang]['name']} {LANGUAGE_MAP.get(lang, '')} |"
        text += f"[={target_langs[lang]['percentage']}% \"{target_langs[lang]['percentage']}\"]|\n"

    return text


# Store the stats as a table in a rst file
statsfile = path.join(path.dirname(__file__), '..', 'docs/lizmap-i18n-stats.md')
with open(statsfile, 'w') as f:
    f.write(f"""<!--
DO NOT EDIT THIS FILE DIRECTLY.
It is generated automatically by transifex_stats.py in the scripts folder.
-->

!!! tip
    Translations are available on [Transifex](https://www.transifex.com/3liz-1/lizmap-locales/), **no** development
    knowledge is required.

These statistics are about the Lizmap Web Client application **only**, for the **two current
maintained branches** and the **next** major version combined.

*Statistics updated: {date.today()}*
{load_overall_stats()}
{load_lang_stats(language_rate)}
""")
