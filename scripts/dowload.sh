#! /usr/bin/env sh

wget --quiet -O data/$SYMBOL.csv \
  http://chart.finance.yahoo.com/table.csv?s=$SYMBOL&a=8&b=18&c=2006&d=8&e=18&f=2016&g=d&ignore=.csv
