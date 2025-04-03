from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Index
from sqlalchemy.orm import relationship
from app.config.db import Base
from datetime import *

class UserRole(Base):
    __tablename__ = 'user_roles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'),nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'),nullable=False)
    createdAt = Column(DateTime, default = datetime.utcnow)
    updatedAt = Column(DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    user = relationship("User", back_populates="roles")
    role = relationship("Role", back_populates="users")

       # Add indices for user_id and role_id
    __table_args__ = (
        Index('user_id', 'user_id'),   # Index for user_id
        Index('role_id', 'role_id'),   # Index for role_id
    )

