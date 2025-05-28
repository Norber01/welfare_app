from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from .models import Dues, Claim, Loan
from . import db

main = Blueprint('main', __name__)

@main.route('/add-dues', methods=['GET', 'POST'])
@login_required
def add_dues():
    if request.method == 'POST':
        fcp_name = request.form['fcp_name']
        amount = request.form['amount']
        date_paid = request.form['date_paid']
        month_paid_for = request.form['month_paid_for']
        new_dues = Dues(fcp_name=fcp_name, amount=amount, date_paid=date_paid, month_paid_for=month_paid_for)
        db.session.add(new_dues)
        db.session.commit()
        flash('Dues entry added successfully!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('add_dues.html')

@main.route('/add-claim', methods=['GET', 'POST'])
@login_required
def add_claim():
    if request.method == 'POST':
        claim_type = request.form['claim_type']
        beneficiary = request.form['beneficiary']
        amount = request.form['amount']
        new_claim = Claim(claim_type=claim_type, beneficiary=beneficiary, amount=amount)
        db.session.add(new_claim)
        db.session.commit()
        flash('Claim submitted successfully!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('add_claim.html')

@main.route('/add-loan', methods=['GET', 'POST'])
@login_required
def add_loan():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        purpose = request.form['purpose']
        interest_agreed = True if request.form.get('interest_agreed') == 'on' else False
        new_loan = Loan(name=name, amount=amount, purpose=purpose, interest_agreed=interest_agreed)
        db.session.add(new_loan)
        db.session.commit()
        flash('Loan entry added successfully!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('add_loan.html')