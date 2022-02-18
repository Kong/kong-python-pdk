#!/bin/bash

sphinx-apidoc -o ./source/ ../kong_pdk/pdk/kong/ -f

make html
