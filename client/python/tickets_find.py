#!/usr/bin/env python
#coding: utf-8


from ticket_worker import tickets_client

def find(key, value):
    client = tickets_client.TicketsClient('http://localhost:3456', 
            '56b416949a574a9f7d607179', '6d064823-eae8-441d-8c76-3344cf9b1fb0',
            'dev', '123')

    parameters = {key:value}
    print client.find(parameters)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print '%s key value' % sys.argv[0]
        sys.exit(0)

    key = sys.argv[1]
    value = sys.argv[2]

    find(key, value)
