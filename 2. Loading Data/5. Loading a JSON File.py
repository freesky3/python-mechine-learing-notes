# 从网站获取
import pandas as pd
import requests
from io import StringIO
# GitHub 上 JSON 文件的 URL
json_file_url = 'https://github.com/clojure/data.json/blob/master/dev-resources/1000-strings.json'
# 使用 requests 获取 JSON 文件内容
response = requests.get(json_file_url)
# 确保请求成功
if response.status_code == 200:
    # 使用 StringIO 将获取的内容转换为文件对象
    json_file_content = StringIO(response.text)
    
    # 使用 pandas 的 read_json 函数读取 JSON 文件
    dataframe = pd.read_json(json_file_content)
    
    # 查看 DataFrame 的前几行
    print(dataframe.head(2))
else:
    print("Failed to retrieve the JSON file.")

print("{:=^50s}".format("Split Line"))

# 本地文件
import pandas as pd
# 假设你的JSON文件路径是正确的，并且文件格式是标准的JSON
json_file_path = r"D:\code-learning\python-learning\python辅助\text.json"
# 使用pandas的read_json函数加载JSON文件
dataframe = pd.read_json(json_file_path)
# 查看前两行数据
print(dataframe.head(2))