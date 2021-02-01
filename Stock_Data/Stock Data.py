import csv


GOOG = "GOOG.csv"
GOOG_2 = "GOOG_2.csv"

NKE = "NKE.csv"
NKE_2 = "NKE_2.csv"

TSLA = "TSLA.csv"
TSLA_2 = "TSLA_2.csv"


with open(GOOG, 'r', newline='') as f, open(GOOG_2, 'w', newline='') as data:
     writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=',')
     writer.writerows(line.split() for line in f)

try:
     import pandas as pd
     new_val = pd.read_csv('GOOG_2.csv', sep=',', usecols=['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
     new_val['Change'] = (new_val['Close'] - new_val['Open']) / new_val['Open']
     new_val.to_csv('Result_2.csv', index=False)
except:
     print("Incorrect process result")
finally:
    f.close()

    with open(NKE, 'r', newline='') as f, open(NKE_2, 'w', newline='') as data:
        writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=',')
        writer.writerows(line.split() for line in f)

try:
    import pandas as pd

    new_val = pd.read_csv('NKE_2.csv', sep=',', usecols=['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
    new_val['Change'] = (new_val['Close'] - new_val['Open']) / new_val['Open']
    new_val.to_csv('Result_2_NKE.csv', index=False)
except:
    print("Incorrect process result")
finally:
    f.close()

    with open(TSLA, 'r', newline='') as f, open(TSLA_2, 'w', newline='') as data:
        writer = csv.writer(data, delimiter=',', quoting=csv.QUOTE_NONE, escapechar=',')
        writer.writerows(line.split() for line in f)

try:
    import pandas as pd

    new_val = pd.read_csv('TSLA_2.csv', sep=',', usecols=['Date', 'Open', 'High', 'Low', 'Close', 'AdjClose', 'Volume'])
    new_val['Change'] = (new_val['Close'] - new_val['Open']) / new_val['Open']
    new_val.to_csv('Result_2_TSLA.csv', index=False)
except:
    print("Incorrect process result")
finally:
    f.close()