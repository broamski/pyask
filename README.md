## pyASK (Python Alexa Skills Kit)

Library to help build Alexa Skills Kits in Lambda.

```python
r = Response(should_end=False)
r.set_output_speech(speech_type="SSML", speech_text="Hello There")
r.set_card(card_type="Simple", cart_title="Hey", card_content="Here are the details.")
r.set_reprompt(speech_type="SSML", speech_text="Want to do this again?")

return r.response_body
```
