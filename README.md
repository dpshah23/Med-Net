# Med Net : A Interactive Platform For Remote Assistance


## Table of Contents
1. [Introduction](#introduction)
2. [Problem Statement](#problem-statement)
3. [Features](#features)
4. [Tech Stack](#tech-stack)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Templates](#templates)
8. [Flow of the System](#flow-of-the-system)
9. [Contributors](#contributors)
10. [Photos](#photos)

---

## Introduction
MedNet is a comprehensive telehealth platform designed to facilitate virtual healthcare services. It supports video conferencing, appointment scheduling, health record integration, and secure messaging between doctors and patients. MedNet aims to make healthcare more accessible and efficient, providing both patients and doctors with tools for seamless communication, consultations, and follow-ups.

---

## Problem Statement
*Problem Statement for Hackathon*

We aim to create a telehealth platform that bridges the gap between patients and doctors by enabling remote consultations and medical services. MedNet will support essential features such as video conferencing, appointment scheduling, health record integration, and a messaging system for secure doctor-patient communication.

### Requirements
- *User Roles*:
  - Support for two types of users: Doctors and Patients.
  - Users must sign up with roles and provide relevant information.

- *Core Features*:
  - *Video Conferencing*: Enable real-time video calls between doctors and patients.
  - *Appointment Scheduling*: Patients can schedule consultations, while doctors can manage their availability.
  - *Health Records*: Allow secure storage and sharing of health records.
  - *Messaging*: Provide a secure chat system for doctor-patient communication.
  - *Feedback System*: Patients can rate their consultations.

---

## Features
1. *Doctor and Patient Sign-Up*: Different forms for doctors and patients, gathering relevant personal and professional information.
2. *Appointment Management*: Doctors can set available slots, and patients can book appointments accordingly.
   - Notifications sent via email for upcoming appointments.
3. *Health Record Management*: Patients can share medical records securely with doctors. Doctors can update health records after each consultation.
4. *Real-Time Communication*: Integrated video conferencing for consultations. Secure messaging for post-consultation queries and updates.
5. *Feedback and Rating System*: Patients can provide feedback after consultations

---

## Tech Stack

- *Backend*: 
  - Django: Web framework for backend development.
  - PostgreSQL : Relational database for data storage.
  - WebRTC: For video conferencing.
  - Gemini API: For intelligent Q&A support (if applicable).

- *Frontend*: 
  - HTML5, CSS3, JavaScript: Frontend technologies for UI/UX.

- *Deployment Plans*:
  - Docker: Containerization for easy deployment.
  - Akash Network: For hosting and scalability.

- *Authentication*:
  - Custom Authentication System: Role-based authentication for doctors and patients.

---

## Installation

To get a local copy of Med-Net-Main up and running, follow these steps:

### Prerequisites
- Python 3.8+: Ensure Python is installed.
- PostgreSQL: Make sure PostgreSQL is installed and running.

### Installation Steps
1. Clone the repository:

    bash
    git clone [https://github.com/dpshah23/Med-Net](https://github.com/dpshah23/Med-Net)
    cd Med-Net-Main
    

2. Build the Docker image:

    bash
    docker-compose build
    

3. Configure the database:
   - Update mednet/settings.py with your MySQL database credentials.

4. Run the development server:

    bash
    docker-compose up
    

5. Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Usage

Once the server is running, you can:

- *Sign Up*: Create a doctor or patient account.
- *Schedule Appointments*: Patients can book consultations with available doctors.
- *Upload Health Records*: Patients can upload medical records for doctor review.
- *Video Consultations*: Doctors and patients can conduct video calls for consultations.
- *Post-Consultation Feedback*: Patients can leave feedback after a consultation.

---

## Templates

- base.html: Base template with common UI elements.
- login.html: User login form.
- signup.html: Registration form for doctors and patients.
- dashboard.html: User dashboard showing appointments and messages.
- appointment.html: Appointment booking and management interface.
- video_call.html: Video conferencing interface.
- feedback.html: Patient feedback form.

---

## Flow of the System

The system is designed to provide an intuitive telehealth experience:

- *Home Page*: Introduction to the platform's features and login/sign-up options.
- *User Sign-Up*: Users can register as either a doctor or patient, providing relevant details.
- *Appointment Scheduling*: Patients book appointments, and doctors can manage their availability.
- *Health Records*: Patients can upload health records, and doctors can view and update them after consultations.
- *Real-Time Video Consultations*: Doctors and patients can conduct video consultations using integrated WebRTC.
- *Messaging*: Secure chat functionality for follow-up questions and ongoing care.

---

## Contributors

- Team Leader:--Nakshi Shah
- Frontend Worked:--
  Kukshi Shah.
  Vedant Tuvar.
  Paripurna Tiwari.
- Backend Worked:--
  Deep Shah.
  Nakshi Shah.

---

## Photos

### Home Page
  ![WhatsApp Image 2024-09-29 at 15 34 39_78b9a3c7](https://github.com/user-attachments/assets/893b2166-3356-421e-b713-716eb252d591)

### Chatbot
  ![WhatsApp Image 2024-09-29 at 15 35 41_f3fae656](https://github.com/user-attachments/assets/b1676d2e-bcc9-42d7-a73b-463261293e1b)

### Patient Dashboard
  ![WhatsApp Image 2024-09-29 at 15 40 48_d5b4ce48](https://github.com/user-attachments/assets/ef9e6cda-7acd-4e13-ad41-2b11ffaf63e9)

### Video Call
  ![WhatsApp Image 2024-09-29 at 15 45 09_8a6892bc](https://github.com/user-attachments/assets/77c0f367-0f9c-46e9-991d-963b46a309d1)

### One-to-One Messaging
  ![Screenshot 2024-09-29 155654](https://github.com/user-attachments/assets/ff8f78f5-45cd-4e89-874c-e6e2d44ade87)



  
