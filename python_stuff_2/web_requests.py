#!/usr/bin/python3

import requests 

#"Data" code taken from pastebin's website under the API header

def main():
  
    # your source code here 
    source_code = "Hello World!"
  
    # data to be sent to api 
    data = {'api_dev_key':'7f1a6068fb808168c71175f8a776fc1b', 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python'} 
  
    # sending post request and saving response as response object 
    r = requests.post("http://pastebin.com/api/api_post.php", data = data) 
  
    # extracting response text  
    pastebin_url = r.text 
    print("The pastebin URL is:%s"%pastebin_url) 


if __name__ == "__main__":
    main()
