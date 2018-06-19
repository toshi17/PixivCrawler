
# coding: utf-8


from pixivpy3 import *
import json
from time import sleep
import os

api = PixivAPI()
f = open('client.json', 'r')
client_info = json.load(f)
f.close()
api.login(client_info['pixiv_id'], client_info['password'])


json_result = api.search_works("デフォルメ", page=1, per_page=30, mode='text')
# print(json_result)

if not os.path.exists("./pixiv_images"):
    os.mkdir("./pixiv_images")
saving_directory_path = "./pixiv_images/"

aapi = AppPixivAPI()
separator = '------------------------------------------------------------'

total_works = json_result.pagination.total
total_pages = json_result.pagination.pages
for page_no in range(1, total_pages):
    json_result = api.search_works("デフォルメ", page=page_no, mode='text')
    
    per_page_works = json_result.pagination.per_page
    for work_no in range(0, per_page_works):
        illust = json_result.response[work_no]
        print('Procedure: %d/%d' % (work_no + 1 + (page_no - 1) * 30, total_works))
        print('Title: %s' % illust.title)
        print(separator)
        aapi.download(illust.image_urls.large, saving_directory_path)
        sleep(1)

print('\nThat\'s all.')



