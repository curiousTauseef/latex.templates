#!/bin/bash

for file in `ls *.pdf`
do
    echo 'cropping '$file
    pdfcrop $file $file
done
