# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import comProto_pb2 as comProto__pb2


class commandServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.topCommand = channel.unary_unary(
                '/commandService/topCommand',
                request_serializer=comProto__pb2.commandMessage.SerializeToString,
                response_deserializer=comProto__pb2.commandMessage.FromString,
                )


class commandServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def topCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_commandServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'topCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.topCommand,
                    request_deserializer=comProto__pb2.commandMessage.FromString,
                    response_serializer=comProto__pb2.commandMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'commandService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class commandService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def topCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/commandService/topCommand',
            comProto__pb2.commandMessage.SerializeToString,
            comProto__pb2.commandMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class getCommandsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getCommands = channel.unary_stream(
                '/getCommandsService/getCommands',
                request_serializer=comProto__pb2.commandMessage.SerializeToString,
                response_deserializer=comProto__pb2.commandMessage.FromString,
                )


class getCommandsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getCommands(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getCommandsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getCommands': grpc.unary_stream_rpc_method_handler(
                    servicer.getCommands,
                    request_deserializer=comProto__pb2.commandMessage.FromString,
                    response_serializer=comProto__pb2.commandMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'getCommandsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class getCommandsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getCommands(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/getCommandsService/getCommands',
            comProto__pb2.commandMessage.SerializeToString,
            comProto__pb2.commandMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class sendResponseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.setCommandResponse = channel.unary_unary(
                '/sendResponse/setCommandResponse',
                request_serializer=comProto__pb2.latestCommand.SerializeToString,
                response_deserializer=comProto__pb2.latestCommand.FromString,
                )


class sendResponseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def setCommandResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_sendResponseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'setCommandResponse': grpc.unary_unary_rpc_method_handler(
                    servicer.setCommandResponse,
                    request_deserializer=comProto__pb2.latestCommand.FromString,
                    response_serializer=comProto__pb2.latestCommand.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sendResponse', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class sendResponse(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def setCommandResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sendResponse/setCommandResponse',
            comProto__pb2.latestCommand.SerializeToString,
            comProto__pb2.latestCommand.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class getResponseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getCommandResponse = channel.unary_stream(
                '/getResponse/getCommandResponse',
                request_serializer=comProto__pb2.latestCommand.SerializeToString,
                response_deserializer=comProto__pb2.latestCommand.FromString,
                )


class getResponseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getCommandResponse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getResponseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getCommandResponse': grpc.unary_stream_rpc_method_handler(
                    servicer.getCommandResponse,
                    request_deserializer=comProto__pb2.latestCommand.FromString,
                    response_serializer=comProto__pb2.latestCommand.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'getResponse', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class getResponse(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getCommandResponse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/getResponse/getCommandResponse',
            comProto__pb2.latestCommand.SerializeToString,
            comProto__pb2.latestCommand.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)