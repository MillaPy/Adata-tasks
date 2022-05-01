from flask import *
from pathlib import Path
import xmltodict
from urllib.request import urlopen
import json, time, os, requests
import xml.etree.cElementTree as e
from dict2xml import dict2xml
from dicttoxml import dicttoxml
from json2xml import json2xml
from json2xml.utils import *

# creation of api app
app = Flask(__name__)

# create an empty endpoint
@app.route('/', methods=['GET'])
def homepage():
    # json is saved somewhere else
    # home = str(Path.home())
    # json_file_path = os.path.join(home, r"Desktop\my own study\my working dir\adata\testjson.json")
    # with open(json_file_path) as json_format_file:
    #     data_json = json.load(json_format_file)
    # json_dump = json.dumps(data_json)

    # or we have sample json on hand
    data_json_file = {"fullname": "George",
                    "characteristics":
                    {
                    "sex": "male",
                    "age": 27
                    },
                    "skills": ["smart", "strong"],
                    "experience":
                    [
                    {
                    "position": "developer",
                    "workplace": "netflix",
                    "salary": "7000"
                    },
                    {
                    "position": "engineer",
                    "workplace": "facebook",
                    "id_card": 56117,
                    "Country": "Scotland"
                      }
                      ]
                      }
    # dumps on wed page
    json_dump = json.dumps(data_json_file)

    return json_dump

@app.route('/user/', methods=['GET']) # user/?user=USER_NAME
def requestpage():
    user_query = str(request.args.get('user'))
    # store the URL in url as parameter for urlopen
    url = 'http://2eff-5-76-238-187.ngrok.io'
    response = requests.get(url)
    json_data_text = response.json()

    # convert to json to xml with special libs
    def json2xml(data_json_file):
        json_to_dict = readfromstring(data_json_file)
        data_json2xml = dict2xml(json_to_dict)
        print('Çonverted JSON to XMl:\n', data_json2xml)
        return data_json2xml

    xml_data = json2xml(json_data_text)
    tree = e.fromstring(xml_data)
    xml_dump = e.dump()

    # or convert with other function, where is not returned xml, but posted and use post method
    # def json2xml1(json_obj, line_padding=""):
    #     result_list = list()
    #     json_obj_type = type(json_obj)
    #
    #     if json_obj_type is list:
    #         for sub_elem in json_obj:
    #             result_list.append(json2xml1(sub_elem, line_padding))
    #
    #         return "\n".join(result_list)
    #
    #     if json_obj_type is dict:
    #         for tag_name in json_obj:
    #             sub_obj = json_obj[tag_name]
    #             result_list.append("%s<%s>" % (line_padding, tag_name))
    #             result_list.append(json2xml1(sub_obj, "\t" + line_padding))
    #             result_list.append("%s</%s>" % (line_padding, tag_name))
    #
    #         return "\n".join(result_list)
    #
    #     return "%s%s" % (line_padding, json_obj)
    #
    # xml_json_data = json.loads(json_data_text)
    # print(json2xml1(xml_json_data))
    # xml = json2xml1(xml_json_data)
    # r = requests.post(url, data=xml, headers='')

    return xml_dump


if __name__ == '__main__':
    app.run(port=7777)