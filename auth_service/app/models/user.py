from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Boolean
from sqlalchemy.orm import relationship
from app.config.db import Base
from datetime import *

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(String(255), nullable = False)
    first_name = Column(String(255), nullable = False)
    last_name = Column(String(255), nullable = False)
    password = Column(String(255), nullable = False)
    phone_number = Column(String(255), nullable = False)
    otp = Column(Integer ,nullable = True)
    otp_expires_at = Column(DateTime, nullable=True)
    is_verify = Column(Boolean, default=False)
    createdAt = Column(DateTime, default = datetime.utcnow)
    updatedAt = Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    roles = relationship("UserRole", back_populates="user")


    def set_otp(self):
            import random
            self.otp = int(random.randint(100000, 999999))
            self.otp_expires_at = datetime.utcnow() + timedelta(minutes=2) 