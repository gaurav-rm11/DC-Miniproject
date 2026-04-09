from flask import Flask, request, jsonify
import grpc

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import banking_pb2
import banking_pb2_grpc

app = Flask(__name__)

account_channel = grpc.insecure_channel('localhost:50051')
account_stub = banking_pb2_grpc.AccountServiceStub(account_channel)

transaction_channel = grpc.insecure_channel('localhost:50053')
transaction_stub = banking_pb2_grpc.TransactionServiceStub(transaction_channel)


@app.route('/create', methods=['POST'])
def create_account():
    data = request.json
    response = account_stub.CreateAccount(
        banking_pb2.CreateAccountRequest(
            name=data['name'],
            initial_balance=data['balance']
        )
    )
    return jsonify({"account_id": response.account_id})


@app.route('/balance/<account_id>')
def balance(account_id):
    response = account_stub.GetBalance(
        banking_pb2.BalanceRequest(account_id=account_id)
    )
    return jsonify({"balance": response.balance})


@app.route('/transfer', methods=['POST'])
def transfer():
    data = request.json
    response = transaction_stub.Transfer(
        banking_pb2.TransferRequest(
            from_account=data['from'],
            to_account=data['to'],
            amount=data['amount']
        )
    )
    return jsonify({"message": response.message})


if __name__ == '__main__':
    app.run(port=3000)