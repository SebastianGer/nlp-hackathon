import pandas as pd
import datetime 
import matplotlib.pyplot as plt

data = pd.read_csv("../data/articleMoodCorrected.csv", delimiter = chr(30), names = ["id", "headline", "url", "publisher", "timestamp", "anger", "joy", "sadness", "fear", "disgust"])


data.timestamp = data.timestamp.map(lambda x: datetime.datetime.utcfromtimestamp(x/1000))


print(data[["publisher", "anger", "joy", "sadness", "fear", "disgust"]].groupby(["publisher"]).mean())

plt.figure(1)
plt.plot(data.loc[lambda data: data.publisher == "NASDAQ"].timestamp, data.loc[lambda data: data.publisher == "NASDAQ"].joy, 'b', data.loc[lambda data: data.publisher == "Reuters"].timestamp, data.loc[lambda data: data.publisher == "Reuters"].joy, 'g', data.loc[lambda data: data.publisher == "Daily Mail"].timestamp, data.loc[lambda data: data.publisher == "Daily Mail"].joy, 'r', data.loc[lambda data: data.publisher == "Huffington Post"].timestamp, data.loc[lambda data: data.publisher == "Huffington Post"].joy, 'y', data.loc[lambda data: data.publisher == "Times of India"].timestamp, data.loc[lambda data: data.publisher == "Times of India"].joy, 'purple')
plt.ylabel('joy')
plt.annotate(data.loc[data['joy'].idxmax()].headline, xy=(data.loc[data['joy'].idxmax()].timestamp, data.joy.max()), xytext=(data.loc[data['joy'].idxmax()].timestamp, data.joy.max()), horizontalalignment="center")
plt.annotate(data.loc[data['joy'].idxmin()].headline, xy=(data.loc[data['joy'].idxmin()].timestamp, data.joy.min()), xytext=(data.loc[data['joy'].idxmin()].timestamp, data.joy.min()), horizontalalignment="center")
plt.xlabel('time')
plt.legend(['NASDAQ','Reuters','Daily Mail','Huffington Post','Times of India'])

plt.figure(2)
plt.plot(data.loc[lambda data: data.publisher == "NASDAQ"].timestamp, data.loc[lambda data: data.publisher == "NASDAQ"].anger, 'b', data.loc[lambda data: data.publisher == "Reuters"].timestamp, data.loc[lambda data: data.publisher == "Reuters"].anger, 'g', data.loc[lambda data: data.publisher == "Daily Mail"].timestamp, data.loc[lambda data: data.publisher == "Daily Mail"].anger, 'r', data.loc[lambda data: data.publisher == "Huffington Post"].timestamp, data.loc[lambda data: data.publisher == "Huffington Post"].anger, 'y', data.loc[lambda data: data.publisher == "Times of India"].timestamp, data.loc[lambda data: data.publisher == "Times of India"].anger, 'purple')
plt.ylabel('anger')
plt.annotate(data.loc[data['anger'].idxmax()].headline, xy=(data.loc[data['anger'].idxmax()].timestamp, data.anger.max()), xytext=(data.loc[data['anger'].idxmax()].timestamp, data.anger.max()), horizontalalignment="center")
plt.annotate(data.loc[data['anger'].idxmin()].headline, xy=(data.loc[data['anger'].idxmin()].timestamp, data.anger.min()), xytext=(data.loc[data['anger'].idxmin()].timestamp, data.anger.min()), horizontalalignment="center")
plt.xlabel('time')
plt.legend(['NASDAQ','Reuters','Daily Mail','Huffington Post','Times of India'])

plt.figure(3)
plt.plot(data.loc[lambda data: data.publisher == "NASDAQ"].timestamp, data.loc[lambda data: data.publisher == "NASDAQ"].sadness, 'b', data.loc[lambda data: data.publisher == "Reuters"].timestamp, data.loc[lambda data: data.publisher == "Reuters"].sadness, 'g', data.loc[lambda data: data.publisher == "Daily Mail"].timestamp, data.loc[lambda data: data.publisher == "Daily Mail"].sadness, 'r', data.loc[lambda data: data.publisher == "Huffington Post"].timestamp, data.loc[lambda data: data.publisher == "Huffington Post"].sadness, 'y', data.loc[lambda data: data.publisher == "Times of India"].timestamp, data.loc[lambda data: data.publisher == "Times of India"].sadness, 'purple')
plt.ylabel('sadness')
plt.annotate(data.loc[data['sadness'].idxmax()].headline, xy=(data.loc[data['sadness'].idxmax()].timestamp, data.sadness.max()), xytext=(data.loc[data['sadness'].idxmax()].timestamp, data.sadness.max()), horizontalalignment="center")
plt.annotate(data.loc[data['sadness'].idxmin()].headline, xy=(data.loc[data['sadness'].idxmin()].timestamp, data.sadness.min()), xytext=(data.loc[data['sadness'].idxmin()].timestamp, data.sadness.min()), horizontalalignment="center")
plt.xlabel('time')
plt.legend(['NASDAQ','Reuters','Daily Mail','Huffington Post','Times of India'], loc = 2)

plt.figure(4)
plt.plot(data.loc[lambda data: data.publisher == "NASDAQ"].timestamp, data.loc[lambda data: data.publisher == "NASDAQ"].fear, 'b', data.loc[lambda data: data.publisher == "Reuters"].timestamp, data.loc[lambda data: data.publisher == "Reuters"].fear, 'g', data.loc[lambda data: data.publisher == "Daily Mail"].timestamp, data.loc[lambda data: data.publisher == "Daily Mail"].fear, 'r', data.loc[lambda data: data.publisher == "Huffington Post"].timestamp, data.loc[lambda data: data.publisher == "Huffington Post"].fear, 'y', data.loc[lambda data: data.publisher == "Times of India"].timestamp, data.loc[lambda data: data.publisher == "Times of India"].fear, 'purple')
plt.ylabel('fear')
plt.annotate(data.loc[data['fear'].idxmax()].headline, xy=(data.loc[data['fear'].idxmax()].timestamp, data.fear.max()), xytext=(data.loc[data['fear'].idxmax()].timestamp, data.fear.max()), horizontalalignment="center")
plt.annotate(data.loc[data['fear'].idxmin()].headline, xy=(data.loc[data['fear'].idxmin()].timestamp, data.fear.min()), xytext=(data.loc[data['fear'].idxmin()].timestamp, data.fear.min()), horizontalalignment="center")
plt.xlabel('time')
plt.legend(['NASDAQ','Reuters','Daily Mail','Huffington Post','Times of India'])

plt.figure(5)
plt.plot(data.loc[lambda data: data.publisher == "NASDAQ"].timestamp, data.loc[lambda data: data.publisher == "NASDAQ"].disgust, 'b', data.loc[lambda data: data.publisher == "Reuters"].timestamp, data.loc[lambda data: data.publisher == "Reuters"].disgust, 'g', data.loc[lambda data: data.publisher == "Daily Mail"].timestamp, data.loc[lambda data: data.publisher == "Daily Mail"].disgust, 'r', data.loc[lambda data: data.publisher == "Huffington Post"].timestamp, data.loc[lambda data: data.publisher == "Huffington Post"].disgust, 'y', data.loc[lambda data: data.publisher == "Times of India"].timestamp, data.loc[lambda data: data.publisher == "Times of India"].disgust, 'purple')
plt.ylabel('disgust')
plt.annotate(data.loc[data['disgust'].idxmax()].headline, xy=(data.loc[data['disgust'].idxmax()].timestamp, data.disgust.max()), xytext=(data.loc[data['disgust'].idxmax()].timestamp, data.disgust.max()), horizontalalignment="center")
plt.annotate(data.loc[data['disgust'].idxmin()].headline, xy=(data.loc[data['disgust'].idxmin()].timestamp, data.disgust.min()), xytext=(data.loc[data['disgust'].idxmin()].timestamp, data.disgust.min()), horizontalalignment="center")
plt.xlabel('time')
plt.legend(['NASDAQ','Reuters','Daily Mail','Huffington Post','Times of India'])

plt.show()





