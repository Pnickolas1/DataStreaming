# Please complete the TODO items in this code
import faust
#
# TODO: Create the faust app with a name and broker
#       See: https://faust.readthedocs.io/en/latest/userguide/application.html#application-parameters
#
app = faust.App("hello-world-faust", broker="localhost:9092")

#
# TODO: Connect Faust to com.udacity.streams.clickevents
#       See: https://faust.readthedocs.io/en/latest/userguide/application.html#app-topic-create-a-topic-description
#
topic = app.topic("com.udacity.streams.purchases")

#
# TODO: Provide an app agent to execute this function on topic event retrieval
#       See: https://faust.readthedocs.io/en/latest/userguide/application.html#app-agent-define-a-new-stream-processor
#
@app.agent(topic)
async def clickevent(clickevents):
    async for click_event in clickevents:
        print(click_event)
    # TODO: Define the async for loop that iterates over clickevents
    #       See: https://faust.readthedocs.io/en/latest/userguide/agents.html#the-stream
    # TODO: Print each event inside the for loop


if __name__ == "__main__":
    app.main()


# kafka-topics --list --zookeeper localhost:2181
# python <file_name> worker