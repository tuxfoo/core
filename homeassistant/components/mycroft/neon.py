from websocket import create_connection, WebSocket


class MycroftAPI(object):
    def __init__(self, mycroft_ip):
        self.mycroft_ip = mycroft_ip
        self.url = "ws://" + self.mycroft_ip + ":8181/core"
        try:
            self._ws = create_connection(self.url)
        except OSError:
            print("Could not connect, verify ip.")
            return None

    def speak_text(self, text):
        mycroft_speak = ('"{}"'.format(text))
        mycroft_type = '"speak"'
        mycroft_data = '{"expect_response": false, "utterance": %s}, ' \
                       '"context": null' % mycroft_speak
        message = '{"type": ' + mycroft_type + \
                  ', "data": ' + mycroft_data + '}'
        self._ws.send(message)
        response = "Message Sent to Mycroft Instance: {}"\
            .format(self.mycroft_ip)
        return response

    def mute_speaker(self, mute):
        """
        Used to mute speaker on enclosure

        Args:
            mute (boolean): True or False - True to mute, False to unmute

        """
        if mute is True:
            mycroft_type = '"enclosure.system.mute"'
            mute_speaker = 'mute'
        else:
            mycroft_type = '"enclosure.system.unmute"'
            mute_speaker = 'unmute'
        message = '{"type": ' + mycroft_type + '}'
        self._ws.send(message)
        response = "Sent command to mycroft to %s speaker" % mute_speaker
        return response