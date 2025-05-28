from . import db
from datetime import datetime

class Dues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fcp_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_paid = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    month_paid_for = db.Column(db.String(50), nullable=False)

class Claim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    claim_type = db.Column(db.String(100), nullable=False)
    beneficiary = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_filed = db.Column(db.DateTime, default=datetime.utcnow)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    purpose = db.Column(db.String(255), nullable=False)
    interest_agreed = db.Column(db.Boolean, default=False)
    date_issued = db.Column(db.DateTime, default=datetime.utcnow)