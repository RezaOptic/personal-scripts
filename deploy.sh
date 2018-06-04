#!/usr/bin/env bash

ADDR=$1
REPO=$2
BRANCH=$3

echo $ADDR
echo $BRANCH
echo $REPO


if [ -d $REPO ]; then
    cd $REPO
    git checkout $BRANCH
    git pull
    docker-compose up -d --build

else
    git clone $ADDR
    cd $REPO
    docker-compose up -d --build
fi
