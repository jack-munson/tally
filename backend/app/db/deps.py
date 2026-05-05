from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()  # Create the session
    try:
        yield db         # Provide it to your route
    finally:
        db.close()