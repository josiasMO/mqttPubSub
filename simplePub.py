import paho.mqtt.client as mqtt

mqttc = mqtt.Client("C1")
mqttc.connect("test.mosquitto.org", 1883)
mqttc.publish("topic/yourTopic", "Hello world")
mqttc.loop(2)
