import grpc
from concurrent import futures
import system_control_pb2
import system_control_pb2_grpc
import subprocess
import psycopg2

class SystemControlService(system_control_pb2_grpc.SystemControlServicer):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def authenticate(self, user_token):
        # Check user_token in PostgreSQL
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE token = %s", (user_token,))
        return cursor.fetchone() is not None

    def Shutdown(self, request, context):
        if not self.authenticate(request.user_token):
            return system_control_pb2.Response(success=False, message="Unauthorized")
        subprocess.run(["shutdown", "/s", "/t", "0"])  # Windows shutdown command
        return system_control_pb2.Response(success=True, message="Computer is shutting down")

    def Sleep(self, request, context):
        if not self.authenticate(request.user_token):
            return system_control_pb2.Response(success=False, message="Unauthorized")
        subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0", "1", "0"])  # Windows sleep command
        return system_control_pb2.Response(success=True, message="Computer is in sleep mode")

    def WakeUp(self, request, context):
        if not self.authenticate(request.user_token):
            return system_control_pb2.Response(success=False, message="Unauthorized")
        # Trigger Wake-on-LAN (requires MAC address)
        mac_address = self.get_mac_address(request.computer_id)
        send_wake_on_lan(mac_address)
        return system_control_pb2.Response(success=True, message="Wake-on-LAN signal sent")

def send_wake_on_lan(mac):
    import socket
    import struct
    # Create magic packet
    mac_bytes = bytes.fromhex(mac.replace(":", ""))
    magic_packet = b'\xff' * 6 + mac_bytes * 16
    # Send packet
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, ('<broadcast>', 9))  # Port 9 is standard for WOL

if __name__ == "__main__":
    db_conn = psycopg2.connect("dbname=control_system user=admin password=pass")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    system_control_pb2_grpc.add_SystemControlServicer_to_server(SystemControlService(db_conn), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
