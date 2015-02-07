# -*- coding: UTF=8 -*-
__author__ = 'Tomas Hartmann'
import threading
import time
from flask import render_template, request, redirect, url_for, session
import webshare
import files
import os
from appwebshare.scripts import config
from appwebshare import app


@app.route("/")
def index():
    if 'username' in session:
        return render_template('index.html', DOWNLOADING=webshare.DOWNLOADING, DOWNLOADED=files.get_file_list())
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', loginstatus=" ")

    if request.method == 'POST' and request.form['username'] == config.LOGIN and \
            request.form['password'] == config.PASS:
        session.pop('tries', None)
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    if 'tries' in session:
        session['tries'] += 1
        if session['tries'] > 10:
            render_template('login.html', loginstatus="too many logins - try again in 3 minutes")
            time.sleep(180)
            session['tries'] = 1
            return render_template('login.html', loginstatus=" ")
        elif session['tries'] > 2:
            return render_template('login.html', loginstatus="wrong")
    else:
        session['tries'] = 1
        return render_template('login.html', loginstatus="wrong")


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    session.pop('tries', None)
    return redirect(url_for('index'))


@app.route("/search/", methods=['GET'])
def search():
    global WST
    if 'username' in session:
        search = request.args.get('search')
        if len(search) > 1:
            linknamedict = webshare.get_link(webshare.find_ident(search))
            link = linknamedict.keys()[0]
            if link[:10] != 'http://vip':
                WST = ''
                linknamedict = webshare.get_link(webshare.find_ident(search))
                link = linknamedict.keys()[0]
                webshare.DOWNLOADING['VIP'] = 'Not a VIP link, trying again'
            name = linknamedict.values()[0]
            download_thread = threading.Thread(target=webshare.download, args=(link, name))
            download_thread.start()
        return redirect(url_for('index'))
    return redirect(url_for('login'))


@app.route('/delete/<filename>')
def delete_file(filename):
    os.remove(config.DIR + filename)
    return redirect(url_for('index'))


@app.route('/stop/<filename>')
def stop_file(filename):
    print filename
    webshare.DOWNLOADING[filename][1] = 1
    return redirect(url_for('index'))