# 🏦 Distributed Banking System using Microservices & gRPC (Python)

This project demonstrates a **Distributed Computing Mini Project** implementing **Microservices Architecture using gRPC in Python**. The system simulates a basic banking environment with independent services communicating over **gRPC**.

---

# 📌 Project Overview

The system consists of three independent microservices:

* **Account Service** – Manages account creation and balance
* **Transaction Service** – Handles money transfers between accounts
* **Notification Service** – Sends notifications for transactions
* **API Gateway (REST)** – Single entry point for client requests

Each service runs independently and communicates using **gRPC**, demonstrating distributed system principles.

---

# 🏗️ Architecture

```
Client / Postman / Curl
        |
        v
   API Gateway (Flask REST)
        |
        v
   Transaction Service (gRPC)
      /            \
     v              v
Account Service   Notification Service
```

---

# ⚙️ Technologies Used

* Python 3.x
* gRPC
* Protocol Buffers (protobuf)
* Flask (API Gateway)
* REST API
* Microservices Architecture

---

# 📁 Project Structure

```
bankms/
│
├── protos/
│   └── banking.proto
│
├── account_service/
│   └── server.py
│
├── transaction_service/
│   └── server.py
│
├── notification_service/
│   └── server.py
│
├── gateway/
│   └── server.py
│
├── banking_pb2.py
├── banking_pb2_grpc.py
├── requirements.txt
└── README.md
```

---

# 🔌 Where gRPC is Used

This project uses **gRPC for inter-service communication**.

### 1. Transaction Service → Account Service

Used to:

* Debit sender account
* Credit receiver account

Method Used:

* `UpdateBalance()`

---

### 2. Transaction Service → Notification Service

Used to:

* Send transaction alert

Method Used:

* `SendNotification()`

---

### 3. API Gateway → Account Service

Used to:

* Create account
* Get account balance

Methods Used:

* `CreateAccount()`
* `GetBalance()`

---

### 4. API Gateway → Transaction Service

Used to:

* Transfer money

Method Used:

* `Transfer()`

---

# 🧠 How gRPC Works in this Project

1. All services share a **common protobuf file** (`banking.proto`)
2. Proto file defines:

   * Services
   * RPC methods
   * Request/Response messages
3. Python gRPC code is generated using:

```
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/banking.proto
```

4. Generated files:

* `banking_pb2.py`
* `banking_pb2_grpc.py`

5. Services create **gRPC servers**

Example:

```
server = grpc.server(...)
```

6. Other services create **gRPC clients (stubs)**

Example:

```
channel = grpc.insecure_channel('localhost:50051')
stub = banking_pb2_grpc.AccountServiceStub(channel)
```

7. RPC call executed

```
stub.UpdateBalance(...)
```

---

# 🧾 gRPC Services & Methods

## Account Service

| Method        | Description              |
| ------------- | ------------------------ |
| CreateAccount | Creates new bank account |
| GetBalance    | Returns account balance  |
| UpdateBalance | Credits/Debits amount    |

---

## Transaction Service

| Method   | Description                      |
| -------- | -------------------------------- |
| Transfer | Transfers money between accounts |

---

## Notification Service

| Method           | Description             |
| ---------------- | ----------------------- |
| SendNotification | Sends transaction alert |

---

# ▶️ Steps to Run the Project

## 1. Clone Repository

```
git clone <your-repo-url>
cd bankms
```

---

## 2. Create Virtual Environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Generate gRPC Files (if not present)

```
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/banking.proto
```

---

## 5. Start Microservices (Open 4 Terminals)

### Terminal 1 — Account Service

```
python account_service/server.py
```

### Terminal 2 — Notification Service

```
python notification_service/server.py
```

### Terminal 3 — Transaction Service

```
python transaction_service/server.py
```

### Terminal 4 — API Gateway

```
python gateway/server.py
```

---

# 🧪 API Testing

## Create Account

POST [http://localhost:3000/create](http://localhost:3000/create)

```
{
  "name": "User",
  "balance": 1000
}
```

---

## Get Balance

GET [http://localhost:3000/balance/{account_id}](http://localhost:3000/balance/{account_id})

---

## Transfer Money

POST [http://localhost:3000/transfer](http://localhost:3000/transfer)

```
{
  "from": "account1",
  "to": "account2",
  "amount": 200
}
```

---

# 🎯 Distributed Computing Concepts Demonstrated

* Microservices Architecture
* gRPC Communication
* Service-to-Service Communication
* API Gateway Pattern
* Independent Deployment
* Loose Coupling
* Protocol Buffers Serialization
* Multi-service orchestration

---

# 🚀 Future Improvements (Optional)

* Docker containerization
* Database integration (PostgreSQL)
* Authentication service
* Load balancing
* Service discovery
* UI Dashboard

---

# 👨‍💻 Author

Distributed Computing Mini Project
Microservices using gRPC in Python
