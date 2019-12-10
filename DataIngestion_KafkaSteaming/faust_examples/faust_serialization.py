# Please complete the TODO items in the code

from dataclasses import asdict, dataclass
import json

import faust


@dataclass
class ClickEvent(faust.Record):
    email: str
    timestamp: str
    uri: str
    number: int


@dataclass
class ClickEventSanitized(faust.Record):
    timestamp: str
    uri: str
    number: int


app = faust.App("exercise3", broker="kafka://localhost:9092")
clickevents_topic = app.topic("com.udacity.streams.clickevents", value_type=ClickEvent)

#
# TODO: Define an output topic for sanitized click events, without the user email
#
sanitized_topic = app.topic(
    "com.udacity.streams.clickevents.sanitized",
    key_type=str,
    value_type=ClickEventSanitized
)

@app.agent(clickevents_topic)
async def clickevent(clickevents):
    async for clickevent in clickevents:
        #
        # TODO: Modify the incoming click event to remove the user email.
        #       Create and send a ClickEventSanitized object.
        click_event_sanitize = ClickEventSanitized(
            timestamp=clickevent.timestamp,
            uri=clickevent.uri,
            number=clickevent.number,
        )


        print(click_event_sanitize)
        # TODO: Send the data to the topic you created above.
        await sanitized_topic.send(key=click_event_sanitize.uri, value=click_event_sanitize)

if __name__ == "__main__":
    app.main()
