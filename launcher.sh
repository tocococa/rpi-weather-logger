#!/bin/bash
python3 logger.py
./server/darkhttpd/darkhttpd /public_index
