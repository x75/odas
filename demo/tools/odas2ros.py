import sys, json, time

# data = json.load(sys.stdin)
# for station in data["data"]:
#    print(json.dumps(station))

import rospy
from rospy_message_converter import json_message_converter
from std_msgs.msg import String
from std_msgs.msg import Header

from odas_msgs.msg import odas, odassrc
# json_str = '{"data": "Hello"}'
# message = json_message_converter.convert_json_to_ros_message('std_msgs/String', json_str)

rospy.init_node('odaslive')

odaspub = rospy.Publisher('/odas', odas)

json_buf = ''
seqno = 0
for line in sys.stdin:
    if line.startswith('{'):
        if len(json_buf) > 1:
            # print "buf = %s" % (json_buf)
            data = json.loads(json_buf)
            # print "data = %s" % (data)
            h = Header(seq=seqno, stamp=data['timeStamp'], frame_id='odaslive')
            # print "header = %s" % (h)
            m_odassrc = [odassrc(**src) for src in data['src']]
            # print "m_odassrc = %s" % (m_odassrc)
            m_odas = odas(timeStamp=data['timeStamp'], src=m_odassrc)
            odaspub.publish(m_odas)
            # print "m_odas = %s" % (m_odas)
            # data['tunnelts'] = data['timeStamp']
            # del data['timeStamp']
            # print "type = %s" % (type(data))
            # json_message_converter.convert_json_to_ros_message('std_msgs/String', json_buf)
            # json_message_converter.convert_json_to_ros_message(json_buf)
        # reset buffer
        json_buf = line
    else:
        json_buf += line
    # print line
    seqno += 1


