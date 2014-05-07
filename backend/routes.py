#!/usr/bin/env python2
from flask import Flask, abort, request, redirect, jsonify
import simplejson
from mpd import MPDClient


app = Flask(__name__)
app.config.update(Debug=True)
mpdurl = 'tmpd.shack'

@app.route('/')
def home():
        return("nothing to see here, move along")

@app.route('/btc')
def btc():
    apiURL = "https://btc-e.com/api/2/btc_usd/ticker"
    s = urllib2.urlopen(apiURL)
    r = s.read()
    r = r.strip()
    jsondata = r
    data = simplejson.loads(jsondata)
    return jsonify(btc = data['ticker']['last'],
                   high = data['ticker']['high'],
                   low = data['ticker']['low'])

@app.route('/mpd/play')
def play():
    client = MPDClient()
    client.timeout = 10
    client.idletimeout = None
    client.connect(mpdurl, 6600)
    client.play()
    client.close()
    client.disconnect()
    return jsonify(status='success', action='play')

@app.route('/mpd/pause')
def pause():
    client = MPDClient()
    client.timeout = 10
    client.idletimeout = None
    client.connect(mpdurl, 6600)
    client.pause()
    client.close()
    client.disconnect()
    return jsonify(status='success', action='pause')

@app.route('/mpd/status')
def mpd_status():
    client = MPDClient()
    client.timeout = 10
    client.idletimeout = None
    client.connect(mpdurl, 6600)
    answer = client.currentsong()
    state = client.status()
    client.close()
    client.disconnect()
    if 'artist' in answer:
        return jsonify(artist = answer['artist'],
                   title = answer['title'],
                   status = state['state'],
                   stream = 'false')
    elif 'name' in answer:
        return jsonify(name=answer['name'],
                       title=answer['title'],
                       stream='true',
                       status = state['state'])
    elif 'file' in answer:
        return jsonify(title=answer['file'],
                       status = state['state'],
                       stream='undef')
    else:
        return jsonify(error='unknown playback type')
    return jsonify(error='unknown playback type')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

