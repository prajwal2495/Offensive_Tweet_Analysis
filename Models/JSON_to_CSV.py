import json
import csv



with open("./JSON_Data/चुतिया/चुतिया_2021-09-06_to_2021-09-11.json") as json_file:
    json_data = json.load(json_file)

tweet_text = json_data["data"][0]["text"]


csv_file = open('json_data.csv','w')

csv_writer = csv.writer(csv_file)

count = 0

for text in tweet_text:
    if count == 0:
        header = text
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(text)

csv_file.close()