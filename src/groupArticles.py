import sys
import pandas as pd

keyword = "test"
data = pd.read_csv("../data/newsCorpora.csv", delimiter = "\t", names = ["id", "headline", "url", "website-name", "dontknow", "dontknow2", "domain", "timestamp"])

data = data[data.headline.map(lambda headline: keyword in headline)]

