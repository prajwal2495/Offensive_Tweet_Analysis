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
    'lowercase': False,
    'remove_english':True,
    'remove_specials':True,
    'add_USER_tag':True
    }


def demoji(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U00010000-\U0010ffff"
                               "]+", flags=re.UNICODE)
    return(emoji_pattern.sub(r'', text))


def main():
    # csv file
    input_file = './CSV_Data/मुर्खा_2021-04-28_to_2021-05-03.csv'

    dataset = pd.read_csv(input_file)

    dataset_df = pd.DataFrame(dataset)

    dataset_df = dataset_df[["text"]]
    #print(dataset_df)

    #remove NaN
    dataset_df.dropna()

    #drop dupes
    dataset_df.drop_duplicates(subset=None, keep = True, inplace=True)


    #lowe case conversion
    dataset_df['text'] = dataset_df['text'].str.lower()

    # calling pre-processing function
    dataset_df['text'] = dataset_df['text'].apply(clean_text, args=(clean_config,))

    #stripping leading and trailing whitespaces
    dataset_df['text'] = dataset_df['text'].str.strip()

    #remove emojis - not working
    dataset_df.astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))

    #remove emojis - working
    dataset_df['text'] = dataset_df['text'].apply( lambda x : demoji(x))

    # convert df to csv
    dataset_df.to_csv('./CSV_Data/Murkha_pre_processed.csv',index = False)

if __name__ == "__main__":
    main()