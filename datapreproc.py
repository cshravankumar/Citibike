import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt 

records = [json.loads(line) for line in open(url)]
records_updated = [json.loads(json.dumps(records[0]['stationBeanList']))]
citidata = pd.DataFrame(records_updated[0])
citidata.head()
dt = pd.Timestamp(citidata['lastCommunicationTime'][0])
