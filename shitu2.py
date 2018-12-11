from aip import AipImageClassify
import json
""" 你的 APPID AK SK """
APP_ID = '您的APP_ID'
API_KEY = '您的API_KEY'
SECRET_KEY = '您的SECRET_KEY'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('fuck.jpg')

""" 调用通用物体识别 """
client.advancedGeneral(image);

""" 如果有可选参数 """
options = {}
options["baike_num"] = 1

""" 带参数调用通用物体识别 """
msg = client.advancedGeneral(image, options)
print(msg['result'][0]['root'])
print(msg['result'][0]['baike_info']['description'])
