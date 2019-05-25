from aip import AipBodyAnalysis

""" APPID AK SK """
APP_ID = '16342649'
API_KEY = '2IiPBrApLr248VTZRfgyqzyZ'
SECRET_KEY = 'e95oYzG9AinSo2NuEp9GSn6vhZyr8Cnm'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)


def count_person_with_pic_path(path):
    image = get_file_content(path)
    return client.bodyAttr(image)


def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()



