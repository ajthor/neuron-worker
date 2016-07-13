
from docker import Client

import time
import zerorpc
import msgpack

dockerClient = Client(base_url='unix://var/run/docker.sock')

class Builder(object):
    def build(self, args):
        print(args)
        args['weeble'] = 'wooble'
        return args

    def validate(self, args):
        print("Hmm.. Looks good.")
        return True

srvr = zerorpc.Server(Builder())
srvr.bind("tcp://0.0.0.0:4197")
srvr.run()

# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")
#
# while True:
#     #  Wait for next build command.
#     message = socket.recv()
#
#     # Validate build command.
#
#     # Build docker container for testing.
#     container = cli.create_container(
#         image='busybox:latest',
#         command='/bin/sleep 30')
#
#     response = cli.start(container=container.get('Id'))
#
#     # Send response back to client.
#     socket.send(response)
