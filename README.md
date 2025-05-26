## 🖼️ Project Overview

Here is how the project looks:

![Screenshot 1](https://github.com/user-attachments/assets/373805d4-2859-4610-84e8-7aee60895d89)
![Screenshot 2](https://github.com/user-attachments/assets/fd506367-3261-4e3e-ba18-1edfe3774859)

---

## 🚀 How to Install and Run the Project

Follow these steps to get the project up and running using Docker and Docker Compose.

---

### ✅ 1. Prerequisites

Make sure you have the following installed on your machine:

* [Docker Desktop](https://www.docker.com/products/docker-desktop) (includes Docker Compose)

---

### ✅ 2. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### ✅ 3. Configure Environment Variables

Create a `.env` file in the project root if required. Example:

```env
DEBUG=1
SECRET_KEY=your-secret-key
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

> 💡 Tip: Check if a `.env.example` file exists and copy it:
>
> ```bash
> cp .env.example .env
> ```

---

### ✅ 4. Build and Start the Containers

Run the following command to build and start all containers:

```bash
docker-compose up --build
```

> 🕐 This may take a few minutes during the first setup.

---

### ✅ 5. Apply Migrations & Create Superuser

In a new terminal, run:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
