# 📘 Software Requirements Specification (SRS)
## Student Management System — Module 1: Student Functionality

### 1. Introduction
This document outlines the Software Requirements Specification (SRS) for Module 1 of the Student Management System, focusing on functionalities for **student users**. This is a web-based application built using:

- **Frontend:** React
- **Backend:** FastAPI (Python)
- **Database:** MySQL
- **File Storage:** Files stored in directories, with paths saved in the database

### 2. Purpose
The purpose of this module is to provide students with a platform where they can:
- Register and manage their profiles
- Log in securely
- Upload necessary academic documents
- Search and access their data securely

### 3. Scope
This module includes only the student user functionality. Other user types (Professors, Office Staffs, Admins) will be developed in future modules.

### 4. Functional Requirements (FR)

| ID     | Description |
|--------|-------------|
| FR1    | Student shall be able to register using basic details (name, email, phone, password, department, roll number). |
| FR2    | Registration status shall initially be set to 'Pending'. Admin shall review the registration and set it to either 'Temporarily Registered' or 'Registration Complete'. |
| FR3    | Student shall be able to log in using email and password, but access to functionalities will depend on registration status. |
| FR4    | System shall validate credentials with hashed passwords stored in the database. |
| FR5    | Student shall be able to view and edit their profile. |
| FR6    | Student shall be able to upload academic documents (PDFs, JPGs, PNGs), based on their registration status. |
| FR7    | The system shall store uploaded files in a directory and save paths in the database. |
| FR8    | Student shall be able to search their data by keywords (e.g., course name, document type), if fully registered. |
| FR9    | Student shall receive feedback (e.g., confirmation or error messages) after each operation. |

### 5. Non-Functional Requirements (NFR)
- **Security:** Passwords stored using hashing algorithms.
- **Performance:** Must support concurrent access by multiple students.
- **Usability:** UI must be user-friendly and responsive.
- **Reliability:** System should recover from database or service failures gracefully.
- **Scalability:** Designed to support additional modules for other user roles.

---

### 6. UML Diagrams

#### 📦 Class Diagram
```plaintext
+-------------------+
|     Student       |
+-------------------+
| - id: int         |
| - name: str       |
| - email: str      |
| - phone: str      |
| - password_hash: str |
| - department: str |
| - roll_number: str|
| - status: str     | <--- Pending / Temporary / Complete
+-------------------+
| +register()       |
| +login()          |
| +editProfile()    |
| +uploadDoc()      |
| +searchData()     |
+-------------------+

+-------------------------+
|     Document            |
+-------------------------+
| - id: int               |
| - student_id: int       |
| - title: str            |
| - file_path: str        |
| - upload_date: datetime |
+-------------------------+
| +upload()               |
+-------------------------+
```

#### 📜 Sequence Diagram — Student Registration
```plaintext
Student -> React Frontend: Fill registration form
React Frontend -> FastAPI Backend: POST /register
FastAPI Backend -> MySQL: INSERT INTO students (status = 'Pending')
MySQL -> FastAPI Backend: Success/Failure
FastAPI Backend -> React Frontend: Registration submitted
React Frontend -> Student: Show success
Admin -> Admin Panel: Review new registrations
Admin -> FastAPI Backend: Approve or Reject Registration
FastAPI Backend -> MySQL: UPDATE students SET status = 'Temporary' or 'Complete'
```

#### 📜 Sequence Diagram — Upload Document
```plaintext
Student -> React Frontend: Choose file to upload
React Frontend -> FastAPI Backend: POST /upload-doc
FastAPI Backend -> Check registration status
FastAPI Backend -> Filesystem: Save file (only if status is Temporary or Complete)
FastAPI Backend -> MySQL: INSERT INTO documents (path, title, student_id)
MySQL -> FastAPI Backend: Success
FastAPI Backend -> React Frontend: File uploaded successfully / denied
```

#### 🎯 Use Case Diagram
```plaintext
        +----------------+
        |     Student     |
        +--------+-------+
                 |
  -----------------------------------------
  |            |           |              |
Register    Login    Upload Document   Search Data
  |            |           |              |
 View/Edit Profile     View Documents     
                 (Based on Registration Status)
```

---

### 7. Database Schema (Simplified)

#### Table: students
| Field         | Type       |
|---------------|------------|
| id            | INT (PK)   |
| name          | VARCHAR    |
| email         | VARCHAR    |
| phone         | VARCHAR    |
| password_hash | TEXT       |
| department    | VARCHAR    |
| roll_number   | VARCHAR    |
| status        | VARCHAR (Pending, Temporary, Complete) |

#### Table: documents
| Field        | Type       |
|--------------|------------|
| id           | INT (PK)   |
| student_id   | INT (FK)   |
| title        | VARCHAR    |
| file_path    | TEXT       |
| upload_date  | DATETIME   |

---

### 8. Technology Stack
- **Frontend:** React (JS/TS)
- **Backend:** Python (FastAPI)
- **Database:** MySQL
- **Storage:** Local file storage with path saved in DB

---

### 9. Future Scope
- Integration with other modules (Professors, Office Staffs, Admin)
- Notification system (email or in-app)
- Role-based dashboard
- Real-time data visualization of student activities

---


