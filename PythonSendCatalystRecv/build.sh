#!/bin/bash

source ../envs/derecho_env_gnu.sh
rm -rf build install
ESMX_Builder -v --cmake-args="-DCMAKE_BUILD_TYPE=Debug"
