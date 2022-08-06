import requests
import subprocess
import os
import pandas as pd

files = os.system('curl -O -X POST "https://www.convertcsv.io/api/v1/xml2csv" -H "Authorization: Token 88c72f33004b132b5963e06b258e60a00f5551f3" -F "infile=@wf_src_idw_cntry_multi_def_cd.xml"')

# url = "https://www.convertcsv.io/api/v1/xml2csv"
# test_file = open("wf_src_idw_cntry_multi_def_cd.xml", "rb")

# r = requests.post(url, headers={'Authorization': 'Token 88c72f33004b132b5963e06b258e60a00f5551f3'}, 
#                      files = {"form_field_name": test_file})
# print(post)

# if r.status_code == 200:
#     with open("temp_out.save","wb") as f:
#         f.write(r.content)

temp_df = pd.read_csv("wf_src_idw_cntry_multi_def_cd.csv")


temp_df.columns.to_list()

# as observerd picked selective transfermation columns 
columns = ['MAPPING/0/TRANSFORMATION/0/TRANSFORMFIELD/0/_NAME',
'MAPPING/0/TRANSFORMATION/0/TRANSFORMFIELD/0/_PORTTYPE',
'MAPPING/0/INSTANCE/0/_DESCRIPTION',
'MAPPING/0/INSTANCE/0/_TRANSFORMATION_TYPE',
'MAPPING/0/CONNECTOR/0/_FROMFIELD',
'MAPPING/0/CONNECTOR/0/_TOFIELD',
'MAPPING/1/TRANSFORMATION/1/TABLEATTRIBUTE/0/_VALUE',
'MAPPING/1/TRANSFORMATION/2/TABLEATTRIBUTE/0/_VALUE',
'MAPPING/1/TRANSFORMATION/3/TABLEATTRIBUTE/0/_VALUE',
'MAPPING/1/TRANSFORMATION/7/TABLEATTRIBUTE/0/_VALUE']

df1 = temp_df[columns].dropna()
pd.set_option('display.max_colwidth', None)
display(df1)

df1.to_csv('result.csv', sep=',', encoding='utf-8')
