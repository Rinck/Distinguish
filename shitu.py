
import requests
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YYlbOyEWriMgYfgFMtrTn2hh&client_secret=CcGkXme1r1AykXyU0vyTACkBeOPZO9sz'
request=requests.post(host)
token = json.loads(request.text)["access_token"]


"更多api地址请参考百度云开发文档"
"这里用动物识别,因为我喜欢识别猫猫的图片哈哈"
url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/animal?'
url = url + 'access_token=' + token

header = {}
header['Content-Type'] = 'application/x-www-form-urlencoded'

options = {}
options["top_num"] = 3
options["baike_num"] = 5


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

"填写正确的图片地址,此处的cat.jpg位于项目根目录"
image = get_file_content('cat.jpg')

msg = requests.post(url,header,image)
