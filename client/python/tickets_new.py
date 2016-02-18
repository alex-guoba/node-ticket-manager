#!/usr/bin/env python
#coding: utf-8


from ticket_worker import tickets_client

def new_ticket(start, end):
    client = tickets_client.TicketsClient('http://localhost:3456', 
            '56bdaf90e35e63a42188e77e', 'e6a32029-b2c4-4a2a-8271-bebb05a66838',
            'dev', '123')

    for i in xrange(start, end):
        title = 't_%d' % i
        category = 'SNM'
        content = {'seq': i, 'from': u"连姆?尼森所扮演的硬汉特工布赖恩与前妻诺尔破镜重圆".encode('utf-8')} 
        description = u"飓风营救_".encode('utf-8') + str(i)
        owner_id = 'Southen New Media'
        result =  client.new(title, category, content, description, owner_id = owner_id)
        import json
        print json.dumps(result, indent=4)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '%s startseq endseq' % sys.argv[0]
        sys.exit(0)
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    new_ticket(start, end)
