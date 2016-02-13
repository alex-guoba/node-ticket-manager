#!/usr/bin/env python
#coding: utf-8


from ticket_worker import tickets_client

def complete(tid):
    client = tickets_client.TicketsClient('http://localhost:3456', 
            '56b416949a574a9f7d607179', '6d064823-eae8-441d-8c76-3344cf9b1fb0',
            'dev', '123')
    print client.complete(tid)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print '%s tid' % sys.argv[0]
        sys.exit(0)
    tid = sys.argv[1]

    complete(tid)
