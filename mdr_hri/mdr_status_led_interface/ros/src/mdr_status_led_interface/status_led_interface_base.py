import rospy

from std_msgs.msg import ColorRGBA


class StatusLedInterfaceBase(object):
    def __init__(self):
        self.status_led_request_topic = rospy.get_param("~status_led_request_topic",
                                                        "/change_status_led")
        self.status_led_topic = rospy.get_param("~status_led_topic",
                                                "/light/change_status_led")

        self.status_led_sub = rospy.Subscriber(self.status_led_request_topic,
                                               ColorRGBA,
                                               self.change_status_led)

    def change_status_led(self, msg):
        rospy.loginfo("[STATUS_LED_INTERFACE] Ignoring request")
