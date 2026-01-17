# 🚖 Ride Hailing Backend Service

The system supports customer onboarding, driver onboarding, ride booking, driver assignment, trip completion, and a mocked payment flow.

---

## 📌 Tech Stack

- **Language:** Python 3.13
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **DB Driver:** psycopg2
- **API Documentation:** Swagger (OpenAPI)
- **Architecture:** Controller → Service → Repository

---

## 🧱 Architecture Overview




### Key Design Principles
- Clear separation of concerns
- One transaction per request
- Database-level locking for concurrency safety
- Minimal, assignment-aligned implementation

---

## 🗄️ Database Schema (Core Tables)

### customers
- id
- name
- phone
- email
- city

### drivers
- id
- name
- phone
- vehicle_number
- vehicle_type
- current_city
- is_available
- latitude
- longitude

### rides
- id
- customer_id
- driver_id
- pickup_lat
- pickup_lng
- drop_lat
- drop_lng
- status
- accepted

### payments
- id
- ride_id
- amount
- status
- created_at

---

## 🚀 How to Run the Project

### 1️⃣ Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt


DB_HOST=localhost
DB_PORT=5432
DB_NAME=ride_hailing
DB_USER=postgres
DB_PASSWORD=your_password


uvicorn main:app --reload
