#!/usr/bin/env python
#coding: utf-8


from ticket_worker import tickets_client

def assign(category):
    client = tickets_client.TicketsClient('http://localhost:3456', 
            '56bdaf90e35e63a42188e77e', 'e6a32029-b2c4-4a2a-8271-bebb05a66838',
            'dev', '123')

    print client.assign(category)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print '%s category' % sys.argv[0]
        sys.exit(0)
    assign(sys.argv[1])
