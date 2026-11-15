# TaskFlow – DevOps & GitOps Project

## Description

TaskFlow is a simple task management web application developed as part of a DevOps and GitOps learning project.

Users can:
- View the list of tasks.
- Add new tasks.
- Store tasks in a PostgreSQL database.

The project focuses on containerization, orchestration, CI/CD, and GitOps practices.

## Technologies

- **Application:** Python, Flask
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose
- **Orchestration:** Kubernetes, Minikube
- **CI/CD:** GitHub Actions
- **Container Registry:** GitHub Container Registry (GHCR)
- **GitOps:** Argo CD

## Project Structure

```text
TaskFlow-DevOps-GitOps/
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── database/
│   └── init.sql
├── kubernetes/
├── argocd/
├── .github/
│   └── workflows/
├── docker-compose.yml
└── README.md
```

## Run the Application with Docker Compose

### Prerequisites

- Docker Desktop
- Docker Compose

### Start the application

```bash
docker compose up --build
```

Open the application in your browser:

http://localhost:5000

### Stop the application

```bash
docker compose down
```

To stop the containers and delete the database volume:

```bash
docker compose down -v
```

**Warning:** The last command deletes the stored database data.

## Database Configuration

The application uses PostgreSQL.

The development configuration is:

- Database: `taskflow`
- User: `taskflow`
- Password: `taskflow123`

These are demonstration credentials only and must not be used in production.

## Project Objectives

1. Build a simple Flask application.
2. Containerize the application with Docker.
3. Run the application and database with Docker Compose.
4. Deploy the application to Kubernetes using Minikube.
5. Automate the build and image publishing process with GitHub Actions.
6. Use Argo CD to synchronize Kubernetes manifests from GitHub.

## Project Status

- [x] Flask application created.
- [x] PostgreSQL database configured.
- [x] Dockerfile created.
- [x] Docker Compose deployment tested.
- [ ] Kubernetes deployment.
- [ ] GitHub Actions CI pipeline.
- [ ] Publish Docker image to GHCR.
- [ ] Argo CD GitOps deployment.
