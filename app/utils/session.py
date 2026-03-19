sessions = {}

def track_user(user):
    sessions[user] = sessions.get(user, 0) + 1
    
