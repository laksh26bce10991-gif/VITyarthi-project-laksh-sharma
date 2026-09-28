class UserManager:
    """Handles user registration, authentication, and user profile management (CRUD)."""
    def __init__(self):
        # Dictionary storing users: {username: {"password": pwd, "scores": [(score, total, pct)]}}[cite: 1]
        self.users = {}

    def register_user(self, username, password):
        """Creates a new user profile (Create operation)[cite: 1]."""
        if username in self.users:
            return False, "User already exists!"
        self.users[username] = {"password": password, "scores": []}
        return True, "Registration successful!"

    def authenticate_user(self, username, password):
        """Validates credentials (Read operation)[cite: 1]."""
        if username in self.users and self.users[username]["password"] == password:
            return True
        return False

    def record_score(self, username, score, total):
        """Updates user quiz attempt records (Update operation)[cite: 1]."""
        if username in self.users:
            percentage = (score / total) * 100
            self.users[username]["scores"].append((score, total, percentage))

    def get_user_history(self, username):
        """Retrieves history for reports (Read operation)[cite: 1]."""
        return self.users.get(username, {}).get("scores", [])