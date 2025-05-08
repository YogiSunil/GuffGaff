# GuffGaff 🎉

**GuffGaff** is a social web application designed to make daily life more engaging through interactive challenges and communication. It encourages users to step out of routine by participating in fun, meaningful daily tasks, planning virtual movie nights with friends, and staying connected via real-time chat.

Built with Flask and designed for simplicity and speed, GuffGaff aims to combine productivity, entertainment, and social connection in one place.

---

## 🌟 Key Features

### 🧑‍🤝‍🧑 User System & Authentication
- Sign up and log in securely with hashed passwords.
- Session management with Flask-Login.
- Profile management (planned for future).

### ✅ Social Challenges
- Users can create and join daily or weekly challenges.
- Track participation and completion.
- Like or comment on others' challenge completions (future feature).

### 🎬 Movie Night Planner
- Schedule movie nights with friends or groups.
- Suggest and vote on movie options.
- Get reminders when movie nights are near.

### 💬 Chat System
- One-on-one messaging.
- Group chat for challenge or movie groups.
- (Optional for future) Real-time using WebSockets.

### 📈 Dashboard & Activity Feed
- View active challenges, upcoming movie nights, and recent messages.
- User dashboard to track personal progress and history.

---

## 🚧 Future Enhancements

GuffGaff is designed with flexibility in mind. Here are features that can be added later:

### Social & Engagement
- Friend system or follower model.
- Leaderboards and badges for top participants.
- Post reactions and comments on challenge completions.
- User-generated content sharing (photos, videos).

### Communication
- Real-time chat with WebSockets or Firebase.
- Voice and video calling.
- Push notifications and email reminders.

### Challenges
- Streak tracking and goal setting.
- AI-based challenge recommendations based on interests.
- Admin-approved public challenges to highlight social causes.

### Admin Panel
- Admin view for moderating content.
- Challenge and movie night approval or curation.

---

## 🛠️ Tech Overview

- **Flask** for back-end development.
- **Flask-WTF** for form handling.
- **Flask-Login** for user sessions.
- **SQLAlchemy** as ORM for database interactions.
- **Jinja2** templating for frontend rendering.
- Designed for deployment on platforms like **Heroku** or **Render**.

---

## 👥 Audience

- Students looking to build consistency and motivation through daily tasks.
- Friends who want a central space to hang out virtually.
- Anyone seeking a lightweight platform to challenge themselves socially and personally.

---

## 📄 License

Open-source under the [MIT License](LICENSE). Contributions welcome!

---

## 🙌 Made With

- ❤️ by a Computer Science student aiming to blend learning with creativity.
- 🧠 Inspired by platforms like Discord, Habitica, and Duolingo challenges.

---

## 🚀 Getting Started

To run GuffGaff locally on your machine, follow these simple steps:

### ✅ Prerequisites

Make sure you have the following installed:

- Python 3.8+
- pip (Python package installer)
- Git (to clone the repo)
- Virtualenv (recommended)

### 🧩 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/GuffGaff.git
cd GuffGaff
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

Create a `.env` file in the root directory and add:

```env
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///guffgaff.db
```

5. Initialize the database:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. Run the development server:

```bash
flask run
```

7. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to explore GuffGaff!

---

## 🌐 Deployment

To deploy GuffGaff to a platform like Heroku:

1. Install the Heroku CLI and log in:

```bash
heroku login
```

2. Create a new Heroku app:

```bash
heroku create guffgaff
```

3. Add a PostgreSQL database:

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. Push your code to Heroku:

```bash
git push heroku main
```

5. Set environment variables on Heroku:

```bash
heroku config:set FLASK_APP=app FLASK_ENV=production SECRET_KEY=your_secret_key
```

6. Run database migrations on Heroku:

```bash
heroku run flask db upgrade
```

7. Open your app in the browser:

```bash
heroku open
```

Enjoy using GuffGaff!