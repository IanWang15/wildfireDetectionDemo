#!/bin/sh

for i in {1..31}
do
    python queryERA5.py ${i}
done
