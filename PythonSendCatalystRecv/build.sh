#!/bin/bash

source ../envs/env_derecho_intel.sh
rm -rf build install
ESMX_Builder -v
