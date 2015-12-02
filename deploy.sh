#!/bin/bash

echo "Building Python packages and deploying to S3 bucket"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIST_DIR=$DIR/dist


if [ -z "$AWS_ACCESS_KEY_ID" ]; then
    echo "Need to set AWS_ACCESS_KEY_ID env var"
    exit 1
fi

if [ -z "$AWS_SECRET_ACCESS_KEY" ]; then
    echo "Need to set AWS_SECRET_ACCESS_KEY env var"
    exit 1
fi

if [ -z "$AWS_S3_BUCKET" ]; then
    echo "Need to set AWS_S3_BUCKET env var"
    exit 1
fi

set -ex

pip install awscli
rm -rf $DIST_DIR
python setup.py sdist -d $DIST_DIR

ORIGINAL_PACKAGE=`ls $DIST_DIR/bareon-api-*.tar.gz`
LATEST_PACKAGE=$DIST_DIR/bareon-api-latest.tar.gz

cp $ORIGINAL_PACKAGE $LATEST_PACKAGE
aws s3 cp $ORIGINAL_PACKAGE s3://$AWS_S3_BUCKET
aws s3 cp $LATEST_PACKAGE s3://$AWS_S3_BUCKET
