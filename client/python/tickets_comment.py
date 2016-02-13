#!/usr/bin/env python
#coding: utf-8


from ticket_worker import tickets_client

def comment(tid, content):
    client = tickets_client.TicketsClient('http://localhost:3456', 
            '56b416949a574a9f7d607179', '6d064823-eae8-441d-8c76-3344cf9b1fb0',
            'dev', '123')

    print client.comment(tid, content)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '%s tid content' % sys.argv[0]
        sys.exit(0)
    tid = sys.argv[1]
    content = sys.argv[2]

    comment(tid, content)
