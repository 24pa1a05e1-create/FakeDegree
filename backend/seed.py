from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Certificate, Base

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add sample certificate
cert1 = Certificate(
    cert_id="CERT123",
    student_name="Rahul Kumar",
    course="B.Tech CSE",
    year="2022",
    institution="XYZ University"
)

cert2 = Certificate(
    cert_id="CERT456",
    student_name="Anita Sharma",
    course="MBA",
    year="2023",
    institution="ABC Institute"
)

session.add(cert1)
session.add(cert2)
session.commit()

print("Sample certificates inserted!")
