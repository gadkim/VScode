# parquet 확장자 를 csv 로 변경
# import pandas as pd
# df = pd.read_parquet('20220324T161144Z-00002.snappy.parquet')
# df.to_csv('20220324T161144Z-00002.snappy.csv')


import pandas as pd
df = pd.read_csv('eastarjet-billing-00001.csv')
df.to_parquet('eastarjet-billing-00001.parquet')

df = pd.read_csv('eastarjet-billing-00002.csv')
df.to_parquet('eastarjet-billing-00002.parquet')