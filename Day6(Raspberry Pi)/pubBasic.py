#file name : pubBasic.py
#/workspace/python/mqtt $
import paho.mqtt.publish as publish
publish.single(“temp”, 21.1, hostname=“localhost”)
