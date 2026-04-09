import grpc
from concurrent import futures

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import banking_pb2
import banking_pb2_grpc
import uuid

accounts = {}

class AccountService(banking_pb2_grpc.AccountServiceServicer):

    def CreateAccount(self, request, context):
        account_id = str(uuid.uuid4())
        accounts[account_id] = request.initial_balance
        return banking_pb2.AccountResponse(
            account_id=account_id,
            message="Account created"
        )

    def GetBalance(self, request, context):
        balance = accounts.get(request.account_id, 0)
        return banking_pb2.BalanceResponse(balance=balance)

    def UpdateBalance(self, request, context):
        accounts[request.account_id] += request.amount
        return banking_pb2.BalanceResponse(
            balance=accounts[request.account_id]
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    banking_pb2_grpc.add_AccountServiceServicer_to_server(
        AccountService(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Account Service running on 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()