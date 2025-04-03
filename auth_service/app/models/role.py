from sqlalchemy import Column, Integer, String, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from app.config.db import Base
from datetime import *

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    role_name = Column(String(200), unique=True, nullable=False)  # Specify length
    createdAt = Column(DateTime, default = datetime.utcnow)
    updatedAt = Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    users = relationship("UserRole", back_populates="role")


