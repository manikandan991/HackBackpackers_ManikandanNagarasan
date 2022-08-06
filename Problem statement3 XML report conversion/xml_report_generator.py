import requests

url = "https://www.convertcsv.io/api/v1/xml2csv"
test_file = open("wf_src_idw_cntry_multi_def_cd.xml", "rb")

r = requests.post(url, headers={'Authorization': 'Token 88c72f33004b132b5963e06b258e60a00f5551f3'}, 
                     files = {"form_field_name": test_file})
print(post)

if r.status_code == 200:
    with open("temp_out.save","wb") as f:
        f.write(r.content)