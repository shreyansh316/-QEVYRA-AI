# QEVYRA AI

> **One AI workspace for conversation, research, building, creation, and intelligent workflows.**

QEVYRA AI is a next-generation AI workspace being built to bring multiple AI capabilities into one unified platform.

Instead of treating chat, research, coding, building, memory, and AI tools as separate products, QEVYRA is designed around a single principle:

> **One AI that understands what you're doing.**

---

## 🚧 Project Status

**Status:** Active development — clean rebuild

**Current milestone:** Phase 08 completed

The project is being rebuilt from the ground up with a production-oriented architecture, incremental development phases, automated testing, database migrations, containerized infrastructure, and Git-based checkpoints.

### Completed

* [x] Repository foundation
* [x] Ubuntu development environment
* [x] Node.js 22
* [x] Python 3.14 backend environment
* [x] FastAPI backend foundation
* [x] Docker infrastructure
* [x] PostgreSQL
* [x] Redis
* [x] SQLAlchemy async database layer
* [x] Alembic database migrations
* [x] User database model
* [x] Argon2 password hashing
* [x] JWT authentication
* [x] User registration
* [x] User login
* [x] Duplicate-account protection
* [x] Invalid-password protection
* [x] Authentication API testing
* [x] GitHub repository workflow

### Currently building

* [ ] Protected user/session endpoints
* [ ] Conversation system
* [ ] Message system
* [ ] AI model routing
* [ ] AI provider integrations
* [ ] Memory system
* [ ] Web/research system
* [ ] QEVYRA web interface
* [ ] Builder/coding mode

---

# Vision

QEVYRA AI is designed as a unified AI workspace rather than a collection of disconnected AI tools.

A future QEVYRA workflow could look like:

```text
"I need to prepare for tomorrow's DBMS exam.
Use my notes, find useful study resources,
identify my weak topics, and create a
two-hour revision plan."
```

QEVYRA should understand the complete task and coordinate the required capabilities.

---

# Core Product

The long-term platform is planned around several interconnected capabilities.

### AI Conversation

Natural conversations with context-aware AI.

### Research

Search, evidence collection, source comparison, and research-oriented answers.

### Study

Learning assistance, notes, resources, revision planning, and educational workflows.

### Builder

AI-assisted coding, application development, debugging, and project building.

### Product Research

Product discovery, comparison, specifications, pricing research, and decision support.

### Memory

Long-term context and user-controlled information that helps QEVYRA understand ongoing work.

### Notebook / Knowledge Library

A personal knowledge workspace for documents, notes, papers, books, and project information.

### Creation

Future support for image, video, and other creative generation workflows.

### Voice

Future voice interaction for natural conversations and hands-free workflows.

---

# Architecture

The project is being developed as a modular system.

```text
                         QEVYRA AI
                             │
              ┌──────────────┴──────────────┐
              │                             │
          Web Client                   API Backend
              │                             │
              │                         FastAPI
              │                             │
              │              ┌──────────────┼──────────────┐
              │              │              │              │
              │          Authentication   Services      Routes
              │              │
              │           JWT + Argon2
              │              │
              │       ┌──────┴──────┐
              │       │             │
              │   PostgreSQL      Redis
              │
              └───────────────────────────────────────────┘
```

Future architecture will add:

```text
                    QEVYRA AI
                        │
              ┌─────────┴─────────┐
              │                   │
           Frontend            Backend
              │                   │
              │          ┌────────┴────────┐
              │          │                 │
              │       AI Router         Core API
              │          │
              │    ┌─────┼─────┐
              │    │     │     │
              │  OpenAI APInex xKiro
              │          │
              │      UnoRouter
              │
              ├── Chat
              ├── Research
              ├── Study
              ├── Builder
              ├── Product
              ├── Notebook
              └── Create
```

---

# Technology Stack

## Backend

* Python 3.14
* FastAPI
* Uvicorn
* SQLAlchemy
* asyncpg
* Alembic
* Pydantic Settings
* PyJWT
* pwdlib
* Argon2
* HTTPX
* Redis client

## Database

* PostgreSQL
* Redis

## Infrastructure

* Docker
* Docker Compose
* Ubuntu Linux

## Development

* Git
* GitHub
* Python virtual environment
* Node.js 22
* npm

---

# Current Backend Structure

```text
apps/api/
│
├── alembic/
│   ├── versions/
│   │   └── c612ee4acc3c_create_users_table.py
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── auth.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── database.py
│   │   └── redis.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── auth.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── auth.py
│   │
│   └── main.py
│
├── tests/
│
├── alembic.ini
└── requirements.txt
```

---

# Authentication

The current backend includes a complete initial authentication foundation.

## Registration

```http
POST /api/auth/register
```

Supports:

* Email validation
* Password validation
* Optional full name
* Secure password hashing
* PostgreSQL user creation
* JWT generation

## Login

```http
POST /api/auth/login
```

Supports:

* Email/password authentication
* Argon2 password verification
* Account status validation
* JWT access-token generation

## Security

Passwords are never stored as plaintext.

The backend uses:

```text
Password
   ↓
Argon2
   ↓
Password hash
   ↓
PostgreSQL
```

JWT tokens are used for authenticated API access.

---

# Database

Current PostgreSQL schema includes:

```text
users
├── id
├── email
├── password_hash
├── full_name
├── is_active
├── is_verified
├── created_at
└── updated_at
```

Database migrations are managed through Alembic.

Example:

```bash
alembic upgrade head
```

Current migration:

```text
c612ee4acc3c_create_users_table
```

---

# Docker Infrastructure

Development infrastructure currently runs through Docker Compose.

```text
PostgreSQL
    Host port: 5433

Redis
    Host port: 6380
```

Services:

```text
qevyra-postgres
qevyra-redis
```

Both services include health checks.

---

# Local Development

## 1. Clone

```bash
git clone git@github.com:shreyansh316/-QEVYRA-AI.git
cd -QEVYRA-AI
```

## 2. Create Python environment

```bash
cd apps/api

python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 4. Start infrastructure

From the project root:

```bash
docker compose -f infra/docker/compose.yml up -d
```

## 5. Configure environment

Create the local environment file from the example:

```bash
cp .env.example .env
```

Never commit `.env`.

## 6. Run migrations

```bash
cd apps/api
alembic upgrade head
```

## 7. Start the API

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8002 --reload
```

API:

```text
http://localhost:8002
```

Swagger documentation:

```text
http://localhost:8002/docs
```

---

# Development Philosophy

QEVYRA is being built using incremental engineering phases.

Each phase follows:

```text
Design
   ↓
Implement
   ↓
Test
   ↓
Review
   ↓
Commit
   ↓
Push
   ↓
Verify
```

The project avoids building a large untested system all at once.

---

# Git Workflow

The development workflow is:

```text
Build
  ↓
Test
  ↓
Commit
  ↓
Push
  ↓
Verify
```

Important rules:

* Do not commit `.env`
* Do not commit API keys
* Do not commit passwords
* Do not commit private keys
* Do not force-push production history
* Keep commits focused on development phases
* Test important changes before pushing

---

# Roadmap

## Phase 01–08

### Foundation

* Repository
* Ubuntu environment
* Node.js
* Python
* FastAPI
* Docker
* PostgreSQL
* Redis
* Alembic
* Authentication

**Status: Complete**

## Phase 09+

### Identity & Sessions

* Protected routes
* Current-user endpoint
* JWT validation
* Session security
* Authentication middleware

### Conversation Engine

* Conversations
* Messages
* Conversation history
* Conversation deletion
* Chat context

### Memory Engine

* User memory
* Memory categories
* Importance
* Confidence
* Expiration
* Memory provenance
* User-controlled memory

### AI Router

Planned provider architecture:

```text
                  AI Router
                     │
        ┌────────────┼────────────┐
        │            │            │
      OpenAI       APInex       xKiro
        │            │            │
        └────────────┼────────────┘
                     │
                 UnoRouter
```

The exact provider/model configuration will be implemented and verified during the corresponding development phases.

### Research Engine

* Web search
* Evidence collection
* Source tracking
* Research mode
* Source comparison
* Freshness handling
* Answer verification

### QEVYRA Intelligence Layer

Long-term goals include:

```text
User request
     ↓
Task understanding
     ↓
Context
     ↓
Model routing
     ↓
Tool execution
     ↓
Evidence / verification
     ↓
Answer
     ↓
Memory / state update
```

### Frontend

Planned:

* Premium dark UI
* Chat workspace
* Research workspace
* Study workspace
* Builder workspace
* Product research workspace
* Notebook
* Creation workspace
* Settings
* Authentication
* Responsive design

### Future Platforms

* Web application
* Android application
* Cloud deployment
* Scalable infrastructure
* Background AI tasks
* Workflow automation

---

# Project Principle

QEVYRA should not feel like:

> "Ten AI tools placed inside one application."

It should feel like:

> **"One AI that understands what I'm trying to accomplish."**

---

# Security

Security is a core part of the architecture.

Current security measures include:

* Argon2 password hashing
* JWT authentication
* Environment-based secrets
* PostgreSQL
* Redis
* Database migrations
* Docker isolation
* Input validation with Pydantic
* Authentication error handling

Production security hardening will continue throughout development.

---

# Disclaimer

QEVYRA AI is an independent software project currently under active development.

Features described as planned or future functionality are not necessarily implemented yet.

---

# License

License information will be added as the project approaches its public release.

---

## Development Status

**QEVYRA AI — Building from the foundation up.**

```text
Phase 08 ✅
Authentication foundation complete.

Next:
Phase 09 → Secure user sessions
```
