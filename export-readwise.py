#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Export Readwise
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 🤖

# Documentation:
# @raycast.author 0x_
# @raycast.authorURL https://raycast.com/0x_

print("Hello World!")

import requests
import datetime
import os
import markdownify

base_readwise_url = "https://readwise.io/api/v2/auth/"
readwise_token = os.environ[''] 
base_mem_url = "https://api.mem.ai/v0/mems"


def main():
    print("Starting Export Operation")
        
    last_fetch_was_at = datetime.datetime.now() - datetime.timedelta(days=1)
    new_data = fetch_from_export_api()
    return
    
def fetch_from_export_api(updated_after=None):
    full_data = []
    next_page_cursor = None
    
    while True:
        params = {}
        if next_page_cursor:
            params['pageCursor'] = next_page_cursor
        if updated_after:
            params['updatedAfter'] = updated_after
        print("Making export api request with params " + str(params) + "...")
        response = requests.get(
            url="https://readwise.io/api/v2/export/",
            params=params,
            headers={"Authorization": f"Token {readwise_token}"}, verify=False
        )
        full_data.extend(response.json()['results'])
        next_page_cursor = response.json().get('nextPageCursor')
        if not next_page_cursor:
            break
    
    print("Exported " + str(len(full_data)) + " highlights from Readwise")
    
    # store in a file 
