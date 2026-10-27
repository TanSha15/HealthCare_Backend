# Healthcare Backend API

Django and Django REST Framework backend with PostgreSQL and JWT authentication.

## Project Structure

```
HealthCareBackend/
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
├── healthcare/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── authentication/
│   ├── apps.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── patients/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── doctors/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
└── mappings/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    └── views.py
```

## Setup and Running

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```
SECRET_KEY=django-insecure-healthcare-backend-key-change-in-production
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=5432
```

3. Run database migrations:
```bash
python manage.py migrate
```

4. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### 1. Authentication APIs
- `POST /api/auth/register/` - Register a new user (`name`, `email`, `password`)
- `POST /api/auth/login/` - Authenticate user and receive JWT access/refresh tokens

### 2. Patient Management APIs (Authenticated)
- `POST /api/patients/` - Create a new patient record
- `GET /api/patients/` - List all patients created by the authenticated user
- `GET /api/patients/<id>/` - Retrieve details of a specific patient
- `PUT /api/patients/<id>/` - Update patient details
- `DELETE /api/patients/<id>/` - Delete a patient record

### 3. Doctor Management APIs (Authenticated)
- `POST /api/doctors/` - Create a new doctor record
- `GET /api/doctors/` - List all doctors
- `GET /api/doctors/<id>/` - Retrieve details of a specific doctor
- `PUT /api/doctors/<id>/` - Update doctor details
- `DELETE /api/doctors/<id>/` - Delete a doctor record

### 4. Patient-Doctor Mapping APIs (Authenticated)
- `POST /api/mappings/` - Assign a doctor to a patient (`patient`, `doctor`)
- `GET /api/mappings/` - Retrieve all patient-doctor mappings
- `GET /api/mappings/<patient_id>/` - Retrieve all doctors assigned to a specific patient
- `DELETE /api/mappings/<id>/` - Remove a doctor assignment
