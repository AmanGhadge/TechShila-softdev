import grpc
from concurrent import futures
import time
# import the generated classes
import comProto_pb2_grpc as comProto_pb2_grpc
import comProto_pb2 as comProto_pb2

import remoteFunctions
import environ
import hashlib

env = environ.Env(
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# topcommand service in proto file
class BidirectionalServiceSendCommand(comProto_pb2_grpc.commandServiceServicer):
    # used to set commands
    def topCommand(self, request, context):
        response = comProto_pb2.commandMessage()
        print(str(response.id))
        request.passcode=hashPass(request.passcode)
        # call set Command.
        if request.one=='':
            remoteFunctions.createSession(request.id,request.passcode)
        else:
            comdict = remoteFunctions.setCommand(
            request.id, request.passcode, request.one, request.uidLatest)
            # last 5 commands stored in database.
            response.one = comdict[0]
            response.two = comdict[1]
            response.three = comdict[2]
            response.four = comdict[3]
            response.five = comdict[5]
            return response


class BidirectionalServiceGetCommands(comProto_pb2_grpc.getCommandsServiceServicer):
    # used to get commands
    def getCommands(self, request, context):
        response = comProto_pb2.commandMessage()
        print(str(response.id))
        request.passcode=hashPass(request.passcode)
        trackID = request.uidLatest
        # call set Command.
        i = 3
        while i > 1:
            print(trackID)
            # TODO : Break loop in 30 seconds and re-develop it by client side ping.
            if trackID == '-1':
                break
            comdict = remoteFunctions.setCommand(
                request.id, request.passcode, request.one, request.uidLatest)
            # if no uid is send treat uidLatest as trackID
            if trackID == '':
                trackID = comdict[5]
                continue
            # if uid sent is and is equal to uidLatest means the latest commands are already sent.
            if (trackID == comdict[5]):
                time.sleep(2)
                continue
            # last 4 commands stored in database and uidLatest
            response.one = comdict[0]
            response.two = comdict[1]
            response.three = comdict[2]
            response.four = comdict[3]
            response.five = comdict[5]
            trackID = comdict[5]
            yield response
            time.sleep(2)
        


class BidirectionalServiceSendResponse(comProto_pb2_grpc.sendResponseServicer):
    # To save response send by PC.
    def setCommandResponse(self, request, context):
        remoteFunctions.saveResponse(request.id, request.passcode,
                     request.command,request.response, request.uid)
        response = comProto_pb2.latestCommand()
        response.uid = request.uid
        return response


class BidirectionalServiceGetResponse(comProto_pb2_grpc.getResponseServicer):
    # To get response of a command by a client(Phone).
    def getCommandResponse(self, request, context):
        request.passcode=hashPass(request.passcode)
        trackID = request.uid
        i = 3
        while i > 1:
            # TODO : Break loop in 30 seconds and re-develop it by client side ping.
            if trackID == '-1':
                break
            list_of_response = remoteFunctions.returnResponses(
                request.id, request.passcode, request.uid)
            if(len(list_of_response) == 0):
                time.sleep(2)
                continue
            if(((list_of_response[-1:])[0]) == trackID):
                time.sleep(2)
                continue
            response = comProto_pb2.latestCommand()
            trackID = (list_of_response[-1:])[0]
            response.resList.extend(list_of_response)
            yield response
            time.sleep(2)

# server start
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    comProto_pb2_grpc.add_commandServiceServicer_to_server(
        BidirectionalServiceSendCommand(), server)

    comProto_pb2_grpc.add_getCommandsServiceServicer_to_server(
        BidirectionalServiceGetCommands(), server)

    comProto_pb2_grpc.add_sendResponseServicer_to_server(
        BidirectionalServiceSendResponse(), server)

    comProto_pb2_grpc.add_getResponseServicer_to_server(
        BidirectionalServiceGetResponse(), server)

    print('Starting server. Listening on port ')
    print(str(env('port_grpc')))
    server.add_insecure_port('[::]:'+env('port_grpc'))
    server.start()
    server.wait_for_termination()

# Hashing Passcodes
def hashPass(password):
    p=password.encode()
    return hashlib.sha256(p).hexdigest()


# Executed when invoked directly
if __name__ == '__main__':
    serve()
