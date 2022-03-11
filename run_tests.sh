#!/bin/bash

path="$( dirname "$( which "$0" )" )"

pytest $path/tests --cov=pyfred --cov-report html:cov_html --cov-report term
