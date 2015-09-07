#!/bin/env python

import rospy
from dynamic_reconfigure import client as drc
from dynamic_reconfigure import find_reconfigure_services
from dynamic_reconfigure import get_parameter_names
import pprint

if __name__ == '__main__':
    rospy.init_node('test_dynrec_client')
    list_dynrecsrvs = find_reconfigure_services()
    print "Found Dynamic reconfigure servers: "
    print list_dynrecsrvs
    print "\nConnecting to first one."
    c = drc.Client(list_dynrecsrvs[0])
    print "Getting group descriptions:"
    group_desc = c.get_group_descriptions()
    print group_desc
    print "\nGet parameter descriptions"
    param_desc = c.get_parameter_descriptions()
    print param_desc
    print "\nGetting parameter names:"
    for param in param_desc:
        pprint.pprint(param)

    # print "\nGet configuration:"
    # conf = c.get_configuration()
    # print conf
