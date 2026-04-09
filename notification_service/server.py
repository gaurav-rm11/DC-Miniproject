import grpc
from concurrent import futures

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import banking_pb2
import banking_pb2_grpc

class NotificationService(banking_pb2_grpc.NotificationServiceServicer):

    def SendNotification(self, request, context):
        print("NOTIFICATION:", request.message)
        return banking_pb2.NotificationResponse(status="sent")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    banking_pb2_grpc.add_NotificationServiceServicer_to_server(
        NotificationService(), server
    )
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Notification Service running on 50052")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()