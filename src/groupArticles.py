import pandas as pd

keyword = "computer"
data = pd.read_csv("../data/newsCorpora.csv", delimiter = "\t", names = ["id", "headline", "url", "website-name", "dontknow", "dontknow2", "domain", "timestamp"])

data = data[data.headline.map(lambda headline: keyword in headline)]
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

headlines = []
urls = []
anger = []
joy = []
sadness = []
fear = []
disgust = []

for id, article in data.iterrows():
	try:
		response = natural_language_understanding.analyze(
		  url=article["url"],
		  features=Features(
		  emotion=EmotionOptions()))
		headlines.append(article["headline"])
		urls.append(article["url"])
		anger.append(response["emotion"]["document"]["emotion"]["anger"])
		joy.append(response["emotion"]["document"]["emotion"]["joy"])
		sadness.append(response["emotion"]["document"]["emotion"]["sadness"])
		fear.append(response["emotion"]["document"]["emotion"]["fear"])
		disgust.append(response["emotion"]["document"]["emotion"]["disgust"])		
	except:
		print "error"


results = pd.DataFrame({"headline" : headlines, "url" : urls, "anger" : anger, "joy" : joy, "sadness" : sadness, "fear" : fear, "disgust" : disgust})
print(results.sort_values(by = "joy", ascending = False)["headline"])

