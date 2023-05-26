import models
import schemas
from sqlalchemy.orm import Session


def get_profile(username: str, db: Session) -> schemas.Profile:
    return db.query(models.User).filter(models.User.username == username).first().profile[0]
