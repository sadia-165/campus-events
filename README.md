# Campus Event Manager
Python + SQLite app: students register for campus events, with waitlists, notifications and feedback.

Modules: users, events, registration, observers (notifications), feedback.
Patterns: Factory (events), Strategy (registration policy), Observer (notifications).

    pip install -r requirements.txt
    python -m pytest --cov=app
