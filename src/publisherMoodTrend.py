import pandas as pd

data = pd.read_csv("../data/newsCorpora.csv", delimiter = "\t", names = ["id", "headline", "url", "publisher", "dontknow", "dontknow2", "domain", "timestamp"])


publishers = ["Reuters", "Huffington Post", "Daily Mail", "Times of India", "NASDAQ", "USA Today"]
data = data[data.publisher.map(lambda publisher: publisher in publishers)]
data.reset_index(drop = True, inplace = True)

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EmotionOptions,EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='04212652-f78b-4b0c-bdbf-ea9bc87b5847',
  password='UPMKxSR8ZroF',
  version='2018-03-16',
  url='https://gateway-fra.watsonplatform.net/natural-language-understanding/api')


with open("articleMood.csv", "w") as f:
	
	for id, article in data.iterrows():
		try:
			response = natural_language_understanding.analyze(
			  url=article["url"],
			  features=Features(
			  emotion=EmotionOptions()))
			entry = str(article["id"])+";"+ \
				article["headline"]+";"+ \
				article["url"] +";"+ \
				article["publisher"]+";"+ \
				str(article["timestamp"])+";"+ \
				str(response["emotion"]["document"]["emotion"]["anger"])+";"+ \
				str(response["emotion"]["document"]["emotion"]["joy"])+";"+ \
				str(response["emotion"]["document"]["emotion"]["sadness"])+";"+ \
				str(response["emotion"]["document"]["emotion"]["fear"])+";"+ \
				str(response["emotion"]["document"]["emotion"]["disgust"])+"\n"
			f.write(entry)	
			print id
		except:
			print "error in article"+str(article["id"])
