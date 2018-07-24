#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# WPSeku - Wordpress Security Scanner
# by jack (78)

def readfile(path):
	return [lines.strip() for lines in open(path,'rb')]
