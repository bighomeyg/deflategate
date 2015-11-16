#!/bin/sh
/opt/local/libexec/gnubin/timeout -sKILL 59m python ~/Desktop/twitter/twitter_streaming.py > ~/Desktop/twitter/deflategate_$(date +\%Y\%m\%d\%H\%M\%S).txt
