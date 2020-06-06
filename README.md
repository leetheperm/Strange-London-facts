# Strange London Facts

Very simple Alexa skill that tells strange facts about London.

## Invocation

```
Alexa, open strange London facts
```

## Intents

```
                [    "name": "StrangeLondonFacts",
                    "slots": [],
                    "samples": [
                        "What weird facts are there about London",
                        "Tell me strange things about London",
                        "Tell me weird London-based facts",
                        "tell me strange london facts",
                        "tell me weird facts about London",
                        "Tell me something strange about London",
                        "tell me a strange fact about London"
                    ]
```

## Code

import required modules. In this case only radom was needed and is part of Python's standard library.

```
import random
````

Create a list to contain facts

```
factoids =[ "A samurai sword, a stuffed puffer fish, a human skull, and a coffin have all been left on the Tube",
"You used to be able to pay for entry to London Zoo with an animal",
"There was nearly a 60 foot stone pineapple at the top of St Paul's Cathedral",
"Feeding pigeons in Trafalgar Square has been banned since 2003",
"Harrods sold cocaine until 1916",
"London isn't actually that rainy",
...
]
```
Create a class that will handle your requests

```
class StrangeLondonFactsIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("StrangeLondonFacts")(handler_input)

    def handle(self, handler_input):
        speak_output = random.choice(factoids)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
```

add class methods to the builder

```
sb.add_request_handler(StrangeLondonFactsIntentHandler())
```

make sure it's in order as they are called from top to bottom

```
sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(StrangeLondonFactsIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
```
