#!/usr/bin/env PYTHONIOENCODING=UTF-8 python3
# -*- coding: utf-8 -*-

from pixivpy3 import *
import json
from time import sleep
import sys, io, re, os

# Directory for ownloaded images
save_dir = "images/"
# After download image, you should sleep a while
sleep_time = 1

def download_bookmark_illusts(illusts):
    for illust in illusts:
        print(illust.title)
        api.download(illust.image_urls.large, save_dir)
        sleep(sleep_time)

def read_client_info(client_json_filepath):
    f = open(client_json_filepath, "r")
    client_info = json.load(f)
    f.close()
    return client_info

if __name__ == "__main__":
    print('pixiv-favotter: Start!')

    # Read client info from file
    client_info = read_client_info("client.json")

    # Load Api
    api = AppPixivAPI()

    # Login
    api.login(client_info["pixiv_id"], client_info["password"])

    # Download bookmarks
    json_result = api.user_bookmarks_illust(client_info['user_id'])
    download_bookmark_illusts(json_result.illusts)

    # Download next page bookmarks if exist
    next_qs = api.parse_qs(json_result.next_url)
    while next_qs is not None:
        json_result = api.user_bookmarks_illust(**next_qs)
        download_bookmark_illusts(json_result.illusts)
        next_qs = api.parse_qs(json_result.next_url)

    print('pixiv-favotter: Finish')
