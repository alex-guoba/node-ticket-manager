#!/usr/bin/env python
#coding: utf-8


from ticket_worker import tickets_client

def comment(tid, content):
    client = tickets_client.TicketsClient('http://localhost:3456', 
            '56bdaf90e35e63a42188e77e', 'e6a32029-b2c4-4a2a-8271-bebb05a66838',
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
