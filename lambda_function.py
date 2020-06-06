# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import random

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

factoids =[ "A samurai sword, a stuffed puffer fish, a human skull, and a coffin have all been left on the Tube",
"You used to be able to pay for entry to London Zoo with an animal",
"There was nearly a 60 foot stone pineapple at the top of St Paul's Cathedral",
"Feeding pigeons in Trafalgar Square has been banned since 2003",
"Harrods sold cocaine until 1916",
"London isn't actually that rainy",
"London hides a network of subterranean rivers",
"Bedlam Asylum used to be one of the city’s most visited attractions",
"Underneath the MoD building in Whitehall is Henry VIII's wine cellar",
"There is a memorial to a Nazi dog in London",
"London went through a period called the Gin Craze",
"The Underground has its own breed of mosquito",
"Henry VIII was born in Greenwich",
"Jerry Springer was born in a London Underground station",
"Karl Marx wrote Das Kapital in one of the British Museum’s rooms while getting very drunk",
"Newham, Waltham Forest, Redbridge, and Barking and Dagenham were all Viking Turf",
"Henry III was given a polar bear as a present and he kept it in the Tower of London",
"An elephant walked across the Thames when it froze over",
"The police never caught Jack the Ripper and his identity is unknown",
"Winnie the Pooh was a real bear at London Zoo",
"Aldgate Station has 1,000 bodies buried underneath it",
"London has had several other names - Lowonidonjon, Londinium, Ludenwic, and Ludenburg",
"There is a city called London in Canada on the River Thames",
"It is illegal to enter the House of Parliaments in armor",
"Great Ormond Street Hospital owns the copyright to Peter Pan",
"Until 1994 there were no roads in the City of London",
"The last execution at the Tower of London was in 1941",
"London is the only city in the world that has hosted the Olympics three times",
"A tidal wave of beer swept through London and killed eight people", 
"First on our list of facts about London is the cultural diversity. As one of the most diverse cities in the world, London houses over 8 million residents, who collectively speak over 300 languages, including Bengali, Gujarati, Punjabi, Cantonese, Mandarin, Hokkien and of course English.",
"Big Ben is arguably London’s most famous landmark. Surprisingly, it is actually meant to go by the name ‘The Clock Tower’, while ‘Big Ben’ is the name of the bell. Feel free to bore your friends and family with that fact if you ever do a tour of London.",
"Despite being a popular theory, it is not illegal to die in the Houses of Parliament. Although it is still illegal to enter the Houses of Parliament wearing a suit of armour.",

"The identity of Jack the Ripper, London’s most notorious serial killer, has never been discovered. Authorities at the time and ‘mystery solvers’ since the killings have suspected a number of different people, however, including Prince Albert, Lewis Carroll and Queen Victoria’s doctor; Sir William Gull.",

"The Great Plague killed roughly 25 million people, which was around a third of the entire population of Europe in the 15th Century. This particularly affected London because of the narrow streets and lack of sanitation. During this time, men known as Searchers shouted out ‘Bring out your dead’ all through the summer of 1665. They carted away dead bodies and threw them in mass burial pits. Some of which Londoners are still discovering to this day.",

"Charles II’s ordered for six ravens to be placed in the Tower of London to protect it. Apparently, six ravens are still kept in the tower today and they must remain there at all times due to superstitious reasons. For extra measures, each raven has a wing clipped, they even have a spare raven handy in case one flies away.",

"When the London Underground was first proposed, engineers suggested filling the tunnels with water and using barges to float people from station to station, or getting an army of horses to pull the carriages around in the dark. Evidently, they decided to opt for trains.",

"The Great Fire in 1666 devastated London. While the fire reduced large parts of the city to ruins, the verified death toll was only six people. However, the real number is unknown, as many more died from indirect causes. Monument, the 203ft stone obelisk located 203 ft away from where the fire broke out, commemorates those who died.",

"In order for a person to become a black cab driver, they must complete a rigorous test called ‘The Knowledge’, which involves memorising every single street in the capital. Cab drivers can spend years trying to learn it all. Some even walk around every part of the city as a way of lodging all the side streets and back alleys in their brains.",

"In a city filled with grand monuments and huge statues, it’s nice to know London has an official smallest statue. Located on Philpot Lane, the statue of two tiny mice eating cheese is dedicated to two builders who fell during construction of The Monument after an argument over a missing sandwich, that they blamed on each other but was actually the fault of a mice infestation.",

"One of Christopher Wren’s original ideas for St Paul’s Cathedral proposed a 60 foot stone Pineapple in place of the now iconic dome. It’s a shame it didn’t happen, London’s skyline could have done with a tropical feel.",

"Although she has many other royal residences, the Queen still sometimes resides in Buckingham Palace. When she’s home, you can see her royal flag flying from the flagpole. This flag, which is called the Royal Standard, must only be flown from buildings where the Queen is present.",

"Cleopatra’s Needle, the Egyptian artefact located on the Victoria Embankment, was erected in 1838. During this time many things were placed underneath, including a map of London, a copy of the Bible, some daily newspapers, a rupee and 12 photographs of the best looking English women of the time.",

"Trafalgar Square was once renowned for housing thousands of feral pigeons, which tourists often fed or posed with. In 2003, London Mayor Ken Livingstone banned feeding them or selling feed near the square. They even went as far as using a hawk to keep them at bay, which evidently turned out to be successful.",

"London has had a plethora of famous residnets such as Karl Marx, Charles Darwin, Sylvia Plath, Charles Dickens, Brian Harvey, Jimi Hendrix, Wolfgang Amadeus Mozart, Florence Nightingale and 100’s of others. Blue plaques now hang where these people lived.",

"The Millennium Dome is so big that it can fit the Great Pyramids of Giza comfortably under the roof! The structure is 365m in diameter; and 52m high in the middle; with 12 supporting poles, symbolising days, weeks and months of the year.",

"London boasts over 170 museums, from the massive British Museum, London’s most popular tourist attraction, to the tiny Fan Museum in Greenwich.",

"Possibly the most disturbing in our facts about London is that 1000 bodies apparently lie under Aldgate station, near Urbanest’s Tower Bridge property. Searchers most likely buried them there en-mass after the Great Plague.",

"The London Eye was not the first big wheel in London. In fact, The Great Wheel earns this title. This wheel was constructed in 1895 for the Empire of India Exhibition. It was then sadly demolished in 1907, 91 years before construction started on the London Eye.",

"Religious Churchmen of the Victorian era were worried that the building of the London Underground would 'disturb the devil'.",

"The junction of Marble Arch and Edgware Road hides such a dark past. It's the site of Tyburn Tree, London's infamous public gallows where an estimated 50,000 people have been hanged.",

"On March 8th 1750, an earthquake struck the streets of London. Residents are said to have seen houses fall into the ground beneath them and fish shooting out of the River Thames.",

"There are actually many hidden waterways. The Fleet River still runs from below the cellars of the Cheshire Cheese pub on Fleet Street.",
"Electric Avenue was Britain's first electrified market street back in the 1880s, as part of Brixton Market. The Avenue is, of course, also the namesake and setting of the Eddy Grant song.",
"Aldgate tube station is built on top of a plague pit where some 1,000 bodies were buried during the Bubonic Plague outbreak of 1665.",
"Aldwych tube station was closed in 1994 and has since been used as a film location for films such as Atonement, Superman IV and Patriot Games. It also features in The Prodigy's famous Firestarter music video",
"Scientists discovered a new species of mosquito on the London Underground. They named it Culex pipiens f. molestus and found that it survives off of the blood of rats, mice and maintenance workers.",
"There's a huge military refuge under the streets of Whitehall. The entrance is at the telephone exchange in Craig's Court.",
"At least seven people died by falling or jumping from the Fire of London's commemorative monument. More than the recorded deaths from the fire itself.",
"The first performance of a Punch and Judy show at Covent Garden was recorded in Samuel Pepys's diary on 9 May, all the way back in 1662. It's believed that a similar puppet show has been seen there every year since.",
"The nursery rhyme Pop Goes the Weasel refers to the act of pawning one's suit after spending all one's cash in the pubs of Clerkenwell.",
"Pubs such as the Fox and Anchor in Smithfield and the Market Porter in Borough are licensed to serve alcohol with breakfast from 7am. This isn't for a swift one before work but instead, it's traditionally to fit in with the hours worked by market porters.",
"The only true home shared by all four of the Beatles (besides a yellow submarine) was a flat at 57 Green Street near Hyde Park, where they lived in the autumn of 1963.",
"London was the first city in the world to reach a population of more than one million, in 1811. It remained the largest city in the world until it was overtaken by Tokyo in 1957.",
"Postman's Park, behind Bart's hospital, is one of London's great hidden contemplative spots. It is full of memorials to ordinary people who committed heroic acts and is famously featured in the film, Closer.",
"The only London theatre not to close during the Second World War was The Windmill in Soho, offering a variety show that mixed comedy acts with semi-nude female tableaux. These days, it's a table-dancing club.",
"The Millennium Dome in Greenwich is the largest structure of its kind in the world. Believe it or not, it's big enough to house the Great Pyramid of Giza or the Statue of Liberty inside. Only one at a time though.",
"Elephant and Castle derives its name from a craftsmen's guild, whose sign featured an elephant. This was due to the ivory handles of the knives they made, not elephant craft.",
"Mayfair is quite literally named after a fair that used to be held in the area every May and Piccadilly after a kind of stiff collar made by a tailor who lived in the area in the 17th century.",
"Lots of modern Londoners would be proud to be labelled as a 'cockney' - but for many years, it was actually a great insult!",
"It is illegal in London to have sex on a parked motorcycle, beat a carpet in a public park or impersonate a Chelsea pensioner - the latter offence is still even punishable by death.",
"Marble Arch was designed by John Nash in 1828 as the entrance to Buckingham Palace, but it was moved to Hyde Park when Queen Victoria expanded the palace. It even contains a tiny office once used as a police station.",
"There's a 19th century time capsule under the base of Cleopatra's Needle, the 68ft, 3,450-year-old obelisk on the banks of the Thames at Embankment. Inside, you'll find a set of British currency, a very old and probably unreliable railway guide, a Bible and 12 portraits of the prettiest English ladies.",
"The tiered design of St Bride's Church in Fleet Street is believed to have been the inspiration for the tiered wedding cake that these days, we all know so well.",
"The Houses of Parliament are home to 1,000 rooms, 100 staircases, 11 courtyards, 8 bars and 6 restaurants. Of course, none of these places are open to the general public.",
"Of the 51 British Prime Ministers who have held office since 1751, only one has ever been assassinated: Spencer Perceval was shot at the House of Commons in 1812.",
"London's smallest house is just 3½ foot wide, forming part of the Tyburn Convent in Hyde Park Place where 20 nuns live.",
"East London is forever immortalised on film and is one of London's most popular locations. It's played host to everything from Oliver! to A Clockwork Orange and Full Metal Jacket. What's more, the naval buildings of Greenwich stood in for Washington in Patriot Games.",
    ]


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


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hello World!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(StrangeLondonFactsIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()