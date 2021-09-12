import csv
import re
import pandas as pd


# pre-processing the data
def clean_text(row, options):

    if options['lowercase']:
        row = row.lower()

    if options['remove_url']:
        row = row.replace('http\S+|www.\S+', '')

    if options['remove_mentions']:
        row = re.sub("@[A-Za-z0-9]+","@USER",row)

    if options['remove_english']:
        row = re.sub("[A-Za-z0-9]+","",row)

    if options['add_USER_tag']:
        row = re.sub("@","@USER",row)

    if options['remove_specials']:
        row = re.sub('[+,-,_,=,/,<,>,!,#,$,%,^,&,*,\",:,;,.,' ',\t,\r,\n,\',|]','',row)

    return row

clean_config = {
    'remove_url': True,
    'remove_mentions': True,
    'decode_utf8': True,
    'lowercase': True,
    'remove_english':True,
    'remove_specials':True,
    'add_USER_tag':True
    }
