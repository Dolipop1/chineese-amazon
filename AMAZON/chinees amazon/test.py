from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product = Column(String(30), nullable=False)
    owner = Column(String(40), nullable=False)
    price = Column(Float, nullable=False)

    def __str__(self):
        return f'product:{self.product}; owner: {self.owner} Price: {self.price}'
    
engine = create_engine('sqlite:///products.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


products1 = products(product='Westinghouse Outdoor Power Equipment 12500 Peak Watt Tri-Fuel Home Backup Portable Generator, Remote Electric Start, Transfer Switch Ready, Gas, Propane, and Natural Gas Powered', owner='Mark Smith', price=1149.99)
session.add(products1)
session.commit()

products2 = products(product='SAMSUNG Galaxy S24 Ultra Cell Phone, 256GB AI Smartphone, Unlocked Android, 50MP Zoom Camera, Long Battery Life, S Pen, US Version, 2024, Titanium Gray', owner='Samsung', price=1299.99)
session.add(products2)
session.commit()

products3 = products(product='Amazon Fire TV 55" Omni QLED Series 4K UHD smart TV, Dolby Vision IQ, Fire TV Ambient Experience, local dimming, hands-free with Alexa', owner='Apple', price=599.99)
session.add(products3)
session.commit()

result = session.query(products).all()
for row in result:
    print(row)