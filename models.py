from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float,CheckConstraint
from sqlalchemy.orm import relationship

from database import Base


class Dummy(Base):
    __tablename__="dummy"
    id=Column(Integer(),primary_key=True,autoincrement=True)
    title=Column(String(20),unique=True,nullable=False)
    
class User(Base):
    __tablename__="users"
    user_id=Column(Integer(),primary_key=True,autoincrement=True)
    username=Column(String(20),unique=True,nullable=False,index=True)
    first_name=Column(String(20),unique=False,nullable=False)
    last_name=Column(String(20),unique=False,nullable=False)
    hashed_password=Column(String(100),unique=False,nullable=False)
    is_admin=Column(Boolean(),default=False,nullable=False)
    latitude=Column(Float(),nullable=True)
    longitude=Column(Float(),nullable=True)
    
    posts=relationship("Post",back_populates="creator")
    added_disasters=relationship("Disaster",back_populates="info_creator")
    missing_persons=relationship("Missing_Person",back_populates="creator")
    

class Disaster(Base):
    __tablename__="disasters"
    disaster_id=Column(Integer(),primary_key=True,autoincrement=True)
    title=Column(String(100),nullable=False,index=True)
    disaster_type=Column(String(20),CheckConstraint("disaster_type in ('cyclone','earthquake','fire','traffic_accident','flood')"),nullable=False)
    info_creation_time=Column(Integer(),nullable=False)
    description=Column(String(1000),nullable=True)
    latitude=Column(Float(),nullable=True)
    longitude=Column(Float(),nullable=True)
    info_creator_id=Column(Integer(),ForeignKey("users.user_id"),nullable=False)
    
    info_creator= relationship("User",back_populates="added_disasters")
    posts= relationship("Post",back_populates="disaster")
    missing_persons=relationship("Missing_Person",back_populates="disaster")
    
class Post(Base):
    __tablename__="posts"
    post_id=Column(Integer(),primary_key=True,autoincrement=True)
    title=Column(String(100),nullable=False)
    post_content=Column(String(1000),nullable=True)
    creation_time=Column(Integer(),nullable=False)
    volunteers_needed=Column(Integer(),nullable=True)
    creator_id=Column(Integer(),ForeignKey("users.user_id"),nullable=False)
    disaster_id=Column(Integer(),ForeignKey("disasters.disaster_id"),nullable=True)
    
    creator= relationship("User",back_populates="posts")
    tags=relationship("Post_Tag",back_populates="post")
    disaster=relationship("Disaster",back_populates="posts")
    
    
class Post_Tag(Base):
    __tablename__="post_tags"
    tag=Column(String(20),primary_key=True)
    post_id=Column(Integer(),ForeignKey("posts.post_id"),primary_key=True)
    
    post=relationship("Post",back_populates="tags")
  
 
class Missing_Person(Base):
    __tablename__="missing_persons"
    missing_person_id=Column(Integer(),primary_key=True,autoincrement=True)
    missing_person_name=Column(String(50),nullable=False)
    date_of_birth=Column(Integer(),nullable=True)
    ethnicity=Column(String(20),nullable=True)
    gender=Column(String(10),CheckConstraint("gender in ('male','female')"),nullable=True)
    weight_kg=Column(Integer(),CheckConstraint("weight_kg > 0"),nullable=True)
    height_cm=Column(Integer(),CheckConstraint("height_cm >0"),nullable=True)
    eye_color=Column(String(20),nullable=True)
    last_seen_time=Column(Integer(),nullable=True)
    blood_group=Column(String(20),nullable=True)
    status=Column(String(10),CheckConstraint("status in ('missing','dead','found')"),nullable=False)
    circumstances=Column(String(500),nullable=True)
    phone=Column(String(30),nullable=True)
    address=Column(String(200),nullable=True)
    identifying_marks=Column(String(500),nullable=True)
    creator_id=Column(Integer(),ForeignKey("users.user_id"),nullable=False)
    creation_time=Column(Integer(),nullable=False)
    disaster_id=Column(Integer(),ForeignKey("disasters.disaster_id"),nullable=True)
    
    creator= relationship("User",back_populates="missing_persons")
    disaster=relationship("Disaster",back_populates="missing_persons")
    


    