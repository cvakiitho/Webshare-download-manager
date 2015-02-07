# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
from cgi import escape
from xml.etree import ElementTree
import time
import requests
from appwebshare.scripts import config


DOWNLOADING = {}
WST = []

# TODO: docstring
# TODO: idea :add size to overview,
# TODO: idea :add stop button,
# TODO: idea :check size left on disk before download,
# TODO: idea :html5 video grid after download


def login_to_webshare():
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    url = 'https://webshare.cz/api/login/'
    payload = {'username_or_email': config.NAME, 'password': config.PASSWORD, 'keep_logged_in': 1}
    r = requests.post(url, data=payload, headers=headers, verify=False)
    print r.text
    if r.status_code == 200:
        DOWNLOADING['VIP'] = 'OK'
    else:
        DOWNLOADING['VIP'] = 'NOT OK, status code: ' + str(r.status_code)
    root = ElementTree.fromstring(r.content)
    print root.find('token').text
    return root.find('token').text


def find_ident(search):
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    url = 'https://webshare.cz/api/search/'
    payload = {'what': escape(str(search)), 'category': '', 'sort': 'rating', 'offset': '0', 'limit': '25', 'wst': ''}
    r = requests.post(url, data=payload, headers=headers, verify=False)
    r.encoding = 'UTF-8'
    root = ElementTree.fromstring(r.content)
    for child in root.findall('file'):
        ident = child.find('./ident').text
        name = child.find('./name').text.encode('ascii', 'ignore')
        size = int(child.find('./size').text)
        if size < config.SIZE and (name[-4:] == '.mkv' or name[-4:] == '.avi' or name[-4:] == '.mp4'):
            return {ident: name}
    print "no video file found" # TODO share error to view


def get_link(id_name_dict):
    global WST
    try:
        ident = id_name_dict.keys()[0]
        name = id_name_dict.values()[0]
    except AttributeError:
        print 'no ident error'
        return 'no ident'
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    url = 'https://webshare.cz/api/file_link/'
    if not WST:
        print 'login calling'
        WST.append(login_to_webshare())
    payload = {'ident': ident, 'wst': WST[len(WST)-1]}
    r = requests.post(url, data=payload, headers=headers, verify=False)
    root = ElementTree.fromstring(r.content)
    return {root.find('link').text: name}


def download(link, name):
    print link
    with open(config.DIR + name, 'wb') as f:
        start = time.clock()
        r = requests.get(link, stream=True)
        total_length = r.headers.get('content-length')
        dl = 0
        DOWNLOADING[name] = [0,0]
        if total_length is None:  # no content length header
            f.write(r.content)
            f.flush()
        else:
            for chunk in r.iter_content(1024):
                if dl and DOWNLOADING[name][1]:
                    del DOWNLOADING[name]
                    del DOWNLOADING['VIP']
                    return 'download stopped'
                dl += len(chunk)
                if chunk:
                    f.write(chunk)
                    f.flush()
                    speed = dl/(time.clock() - start)
                    DOWNLOADING[name][0] = str(int(speed/1000)) + 'KB/s' + '     ' + str(int(((int(total_length) - dl)/speed))) + 's left'
    del DOWNLOADING[name]
    del DOWNLOADING['VIP']