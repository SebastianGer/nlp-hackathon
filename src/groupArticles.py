import pandas as pd

keyword = "test"
data = pd.read_csv("../data/newsCorpora.csv", delimiter = "\t", names = ["id", "headline", "url", "website-name", "dontknow", "dontknow2", "domain", "timestamp"])

data = data[data.headline.map(lambda headline: keyword in headline)]
data.reset_index(drop = True, inplace = True)

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username='04212652-f78b-4b0c-bdbf-ea9bc87b5847',
  password='UPMKxSR8ZroF',
  version='2018-03-16',
  url='https://gateway-fra.watsonplatform.net/natural-language-understanding/api')

response = natural_language_understanding.analyze(
  url=data["url"][0],
  features=Features(
    entities=EntitiesOptions(
      emotion=True,
      sentiment=True,
      limit=2),
    keywords=KeywordsOptions(
      emotion=True,
      sentiment=True,
      limit=2)))

print(json.dumps(response, indent=2))
