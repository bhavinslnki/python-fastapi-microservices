import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.config.db import engine
from sqlalchemy.orm import Session
from app.models.role import Role
from app.models.user import User
from app.models.user_role import UserRole
from datetime import datetime
from passlib.hash import bcrypt

def seed_data():
    session = Session(engine)

    if session.query(Role).count() == 0:
        roles = [Role(role_name="admin"), Role(role_name="manager"), Role(role_name="employee")]
        session.add_all(roles)
        session.commit()
        print("Roles seeded!")

    if session.query(User).filter_by(email="admin123@gmail.com").first() is None:
        admin_user = User(
            email="admin123@gmail.com",
            first_name="the",
            last_name="admin",
            password=bcrypt.hash("admin@123"),
            otp=123456,
            phone_number="1234567890",
            createdAt=datetime.utcnow(),
            updatedAt=datetime.utcnow()
        )
        session.add(admin_user)
        session.commit()

        admin_role = session.query(Role).filter_by(role_name="admin").first()
        if admin_role:
            user_role = UserRole(user_id=admin_user.id, role_id=admin_role.id)
            session.add(user_role)
            session.commit()
            print("Admin user assigned to Admin role!")

    session.close()

if __name__ == "__main__":
    seed_data()


