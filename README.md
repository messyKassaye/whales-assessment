# Todo API with Django Rest Framework, Celery, Redis, and Docker

This project is a simple Todo application API built using:
- Django Rest Framework (DRF) for backend API
- SimpleJWT for authentication (access and refresh tokens)
- Celery + Redis for background tasks (email reminders)
- Docker and Docker-Compose for containerization

---

## Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/messyKassaye/whales-assessment.git
cd todoapi
```

### 2. Install Docker
Make sure you have both installed:

- Install Docker

- Install Docker Compose


### 3. Build and start the container
```bash
docker-compose up --build
```

### This will start:

- Django app (on http://localhost:8000)

- Redis server (for Celery)

- Celery worker (to handle background tasks)


### Authenticatio
### We use SimpleJWT for authentication.

- Register: http://localhost:8000/api/register/
```json
{
  "username": "john",
  "password": "secret123",
  "email": "john.doe@gmail.com"
}
```

- Login (get access and refresh tokens): http://localhost:8000/api/login
```json
{
  "username": "john",
  "password": "secret123",
}
```

### Task Creation and update


- Create task: http://localhost:8000/api/tasks/
```json
{
	"title":"Django whales",
	"description":"Completed this Todo API assessment ASAP",
	"completed":"false",
   "deadline": "2025-04-26T14:30:00"
}
```

- Get all my task: http://localhost:8000/api/tasks/
```json
[
	{
		"id": 2,
		"title": "Django assessement",
		"description": "is Django completed",
		"deadline": "2025-04-26T14:30:00Z",
		"priority": "medium",
		"is_completed": false
	},
	{
		"id": 3,
		"title": "Final test",
		"description": "Final test",
		"deadline": "2025-04-26T14:30:00Z",
		"priority": "medium",
		"is_completed": false
	}
]
```

### Background Email Reminders
### Celery runs a periodic task.
- celery background reminder using email found under /tasks/tasks.py
- It checks for tasks with a deadline within the next 24 hours.

- It sends an email reminder to the task owner.

### How it works:
- Periodic task scheduled using Celery beat or simple loop.

- If any task's deadline is within 24 hours, send an email reminder.

