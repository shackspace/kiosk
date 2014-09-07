#!/bin/bash

lpr -o DocCutType=0NoCutDoc -P 'Star_TSP143_' /opt/printbon/1.eps

/opt/printbon/simple.sh 2880 1 2>/dev/null | grep -Po 'code\" : "\d[^"]*' | grep -Po '\d*' | sed 's/./&-/5' | lpr -o cpi=10 -o DocCutType=0NoCutDoc -P 'Star_TSP143_'

lpr -P 'Star_TSP143_' /opt/printbon/2.eps
