#!/bin/bash

USAGE="Usage: $0 <sitename> <username> <groupname>"

if [ "$#" -ne "3" ];
then
    echo $USAGE
    exit 1
fi

SITENAME=$1
USERNAME=$2
GROUPNAME=$3

for file in *template*
do
    cat $file | sed "s/SITENAME/$SITENAME/g" | \
        sed "s/USERNAME/$USERNAME/g" | \
        sed "s/GROUPNAME/$GROUPNAME/g" \
        > `echo $file | sed "s/template/$SITENAME/g"`
done

