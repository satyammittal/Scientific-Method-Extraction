#!/usr/bin/env bash
c="_text"
j=$1
if [ "$#" -eq  "0" ]
   then
     j="PAKDD-3year"
 else
     j=$1
fi
echo "PDF Folder:" $j
echo "Text Folder:Text"
t="./Text/"
mkdir -p Text 
for i in ./$j/*.pdf
do 
    pdfname="$(echo $i | rev | cut -d "/" -f 1 | rev)"
    echo $t$pdfname$c
    python pdf2txt.py -o "$t$pdfname$c" -t text "$i"
    echo "Converting :"  $pdfname 
done
python ver2.py $t
python phase31.py

