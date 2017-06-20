from twisted.web.client import Agent
from twisted.internet.task import react
from twisted.internet.protocol import Protocol
from twisted.internet.defer import inlineCallbacks, Deferred

from untwisted.ssl import CustomPolicyForHTTPS


@inlineCallbacks
def main(reactor):
  customPolicy = CustomPolicyForHTTPS()
  agent = Agent(reactor, customPolicy)
  response = yield agent.request(
    "GET", "https://google.com"
  )
  done = Deferred()

  class CaptureString(Protocol):
    def dataReceived(self, data):
      print("Received:", data)

    def connectionLost(self, reason):
      done.callback(None)

  response.deliverBody(CaptureString())
  yield done


react(main)
