import sys, json

# data = json.load(sys.stdin)
# for station in data["data"]:
#    print(json.dumps(station))

from rospy_message_converter import json_message_converter
from std_msgs.msg import String
# json_str = '{"data": "Hello"}'
# message = json_message_converter.convert_json_to_ros_message('std_msgs/String', json_str)


json_buf = ''
for line in sys.stdin:
    if line.startswith('{'):
        if len(json_buf) > 1:
            print "buf = %s" % (json_buf)
            # data = json.loads(json_buf)
            # data['tunnelts'] = data['timeStamp']
            # del data['timeStamp']
            # print "type = %s" % (type(data))
            # print "data = %s" % (data)
            json_message_converter.convert_json_to_ros_message('std_msgs/String', json_buf)
            # json_message_converter.convert_json_to_ros_message(json_buf)
        # reset buffer
        json_buf = line
    else:
        json_buf += line
    # print line


