#!/usr/bin/env python
from basic_app import create_app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=8080)
