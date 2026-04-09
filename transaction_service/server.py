import grpc
from concurrent import futures

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import banking_pb2
import banking_pb2_grpc

class TransactionService(banking_pb2_grpc.TransactionServiceServicer):

    def Transfer(self, request, context):

        account_channel = grpc.insecure_channel('localhost:50051')
        account_stub = banking_pb2_grpc.AccountServiceStub(account_channel)

        notification_channel = grpc.insecure_channel('localhost:50052')
        notification_stub = banking_pb2_grpc.NotificationServiceStub(notification_channel)

        # debit
        account_stub.UpdateBalance(
            banking_pb2.UpdateBalanceRequest(
                account_id=request.from_account,
                amount=-request.amount
            )
        )

        # credit
        account_stub.UpdateBalance(
            banking_pb2.UpdateBalanceRequest(
                account_id=request.to_account,
                amount=request.amount
            )
        )

        notification_stub.SendNotification(
            banking_pb2.NotificationRequest(
                message=f"Transfer of {request.amount} completed"
            )
        )

        return banking_pb2.TransferResponse(message="Transfer successful")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    banking_pb2_grpc.add_TransactionServiceServicer_to_server(
        TransactionService(), server
    )
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Transaction Service running on 50053")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()