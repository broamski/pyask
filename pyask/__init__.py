import sys


class Response(object):
    def __init__(self, version="1.0", should_end=True):
        self.response_body = {}
        self.response_body['version'] = version
        self.response_body['sessionAttributes'] = {}
        self.response_body['response'] = {}
        self.response_body['response']['shouldEndSession'] = should_end

    def _build_output_speech(self, speech_type=None, speech_text=None):
        output_speech = {}
        speech_types = ["PlainText", "SSML"]
        if speech_type not in speech_types:
            sys.exit("%s is not a valid speech type. Valid types are: %s" %
                     (speech_type, ', '.join(speech_types)))
        if speech_text is None or speech_text == "":
            sys.exit("You must provide a value for speech_text")
        output_speech['type'] = speech_type
        if speech_type == "SSML":
            if "<speak>" not in speech_text:
                speech_text = "<speak>%s</speak>" % (speech_text,)
            type_label = "ssml"
        if speech_type == "PlainText":
            type_label = "text"
        output_speech[type_label] = speech_text
        return output_speech

    def set_output_speech(self, speech_type=None, speech_text=None):
        output_speech = self._build_output_speech(
            speech_type=speech_type, speech_text=speech_text)
        self.response_body['response']['outputSpeech'] = output_speech

    def set_card(self, card_type=None, card_title=None, card_content=None):
        card = {}
        card_types = ["Simple", "LinkAccount"]
        if card_type not in card_types:
            sys.exit("%s is not a valid card type. Valid types are: %s" %
                     (card_type, ', '.join(card_types)))
        card['type'] = card_type
        if card_type == "LinkAccount":
            self.response_body['response']['card'] = card
            return
        card['title'] = card_title
        card['content'] = card_content
        self.response_body['response']['card'] = card

    def set_reprompt(self, speech_type=None, speech_text=None):
        output_speech = self._build_output_speech(
            speech_type=speech_type, speech_text=speech_text)
        self.response_body['response']['reprompt'] = {
            'outputSpeech': output_speech
        }
