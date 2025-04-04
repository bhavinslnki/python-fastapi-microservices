# Auth Service API

## Overview
This authentication service is built using Python and FastAPI. It provides user management features including registration, login, and OTP verification.

---

## Setup Instructions

### 1. Clone the Repository
```sh
$ git clone https://github.com/bhavinslnki/python-fastapi-microservices.git
$ cd auth-service
```

### 2. Create and Activate Virtual Environment
```sh
$ python -m venv venv
$ source venv/bin/activate  # On macOS/Linux
$ venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Run the Server
```sh
$ uvicorn app.main:app --reload
```

---

## API Endpoints

### 1. Admin Login
```sh
curl --location 'http://localhost:5001/api/v1/admin/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"admin123@gmail.com",
    "password":"admin@123"
}'
```

### 2. Employee Registration
```sh
curl --location 'http://localhost:5001/api/v1/employee/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "dummy_employee@gmail.com", 
    "password": "employee@123",
    "first_name": "John",
    "last_name": "Doe", 
    "phone_number": "9876543210"
}'
```

### 3. Employee Login
```sh
curl --location --request GET 'http://localhost:5001/api/v1/employee/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "dummy_employee@gmail.com", 
    "password": "employee@123"
}'
```

### 4. Employee OTP Verification
```sh
curl --location 'http://localhost:5001/api/v1/employee/send-otp' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"dummy_employee@gmail.com" 
}'
```

```sh
curl --location 'http://localhost:5001/api/v1/employee/verify-otp' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "dummy_employee@gmail.com", 
    "otp": 123456
}'
```

### 5. Manager Registration
```sh
curl --location 'http://localhost:5001/api/v1/manager/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "dummy_manager@gmail.com", 
    "password": "manager@123",
    "first_name": "Alice",
    "last_name": "Smith", 
    "phone_number": "9123456789"
}'
```

### 6. Manager Login
```sh
curl --location --request GET 'http://localhost:5001/api/v1/manager/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "dummy_manager@gmail.com", 
    "password": "manager@123"
}'
```

### 7. Manager OTP Verification
```sh
curl --location 'http://localhost:5001/api/v1/manager/send-otp' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"dummy_manager@gmail.com" 
}'
```

```sh
curl --location 'http://localhost:5001/api/v1/manager/verify-otp' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "dummy_manager@gmail.com", 
    "otp": 654321
}'
```

---

## Environment Variables
Create a `.env` file and add:
```
DATABASE_URL=mysql+pymysql://user:password@localhost/db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## License
