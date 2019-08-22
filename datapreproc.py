
records = [json.loads(line) for line in open(url)]
records_updated = [json.loads(json.dumps(records[0]['stationBeanList']))]
citidata = pd.DataFrame(records_updated[0])
citidata.head()
dt = pd.Timestamp(citidata['lastCommunicationTime'][0])
