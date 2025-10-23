from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",                # 👈 Change to your MySQL username
        password="sanjeev2006",   # 👈 Change to your MySQL password
        database="insurance_db"
    )

# ---------------- HOME PAGE ----------------
@app.route('/')
def index():
    return render_template('index.html')

# ---------------- ADD CUSTOMER ----------------
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO customers (name, dob, gender, email, phone, address)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, dob, gender, email, phone, address))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_customer.html')

# ---------------- ADD POLICY ----------------
@app.route('/add_policy', methods=['GET', 'POST'])
def add_policy():
    if request.method == 'POST':
        policy_name = request.form['policy_name']
        policy_type = request.form['policy_type']
        premium_amount = request.form['premium_amount']
        coverage_amount = request.form['coverage_amount']
        term_years = request.form['term_years']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO policies (policy_name, policy_type, premium_amount, coverage_amount, term_years)
            VALUES (%s, %s, %s, %s, %s)
        """, (policy_name, policy_type, premium_amount, coverage_amount, term_years))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_policy.html')

# ---------------- ASSIGN POLICY ----------------
@app.route('/assign_policy', methods=['GET', 'POST'])
def assign_policy():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT customer_id, name FROM customers")
    customers = cur.fetchall()
    cur.execute("SELECT policy_id, policy_name FROM policies")
    policies = cur.fetchall()

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        policy_id = request.form['policy_id']
        issue_date = request.form['issue_date']
        expiry_date = request.form['expiry_date']

        cur.execute("""
            INSERT INTO customer_policies (customer_id, policy_id, issue_date, expiry_date, status)
            VALUES (%s, %s, %s, %s, 'Active')
        """, (customer_id, policy_id, issue_date, expiry_date))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    cur.close()
    conn.close()
    return render_template('assign_policy.html', customers=customers, policies=policies)

# ---------------- ADD PAYMENT ----------------
@app.route('/add_payment', methods=['GET', 'POST'])
def add_payment():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT cp.customer_policy_id, c.name, p.policy_name 
        FROM customer_policies cp
        JOIN customers c ON cp.customer_id = c.customer_id
        JOIN policies p ON cp.policy_id = p.policy_id
    """)
    customer_policies = cur.fetchall()

    if request.method == 'POST':
        customer_policy_id = request.form['customer_policy_id']
        payment_date = request.form['payment_date']
        amount = request.form['amount']
        payment_mode = request.form['payment_mode']

        cur.execute("""
            INSERT INTO payments (customer_policy_id, payment_date, amount, payment_mode)
            VALUES (%s, %s, %s, %s)
        """, (customer_policy_id, payment_date, amount, payment_mode))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    cur.close()
    conn.close()
    return render_template('add_payment.html', customer_policies=customer_policies)

# ---------------- ADD CLAIM ----------------
@app.route('/add_claims', methods=['GET', 'POST'])
def add_claims():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT cp.customer_policy_id, c.name, p.policy_name
        FROM customer_policies cp
        JOIN customers c ON cp.customer_id = c.customer_id
        JOIN policies p ON cp.policy_id = p.policy_id
    """)
    customer_policies = cur.fetchall()

    if request.method == 'POST':
        customer_policy_id = request.form['customer_policy_id']
        claim_date = request.form['claim_date']
        claim_amount = request.form['claim_amount']
        reason = request.form['reason']
        status = request.form['status']

        cur.execute("""
            INSERT INTO claims (customer_policy_id, claim_date, claim_amount, reason, status)
            VALUES (%s, %s, %s, %s, %s)
        """, (customer_policy_id, claim_date, claim_amount, reason, status))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('view_claims'))

    cur.close()
    conn.close()
    return render_template('add_claims.html', customer_policies=customer_policies)

# ---------------- VIEW CLAIMS ----------------
@app.route('/view_claims')
def view_claims():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT cl.claim_id, c.name AS customer_name, p.policy_name, cl.claim_date, cl.claim_amount, cl.reason, cl.status
        FROM claims cl
        JOIN customer_policies cp ON cl.customer_policy_id = cp.customer_policy_id
        JOIN customers c ON cp.customer_id = c.customer_id
        JOIN policies p ON cp.policy_id = p.policy_id
    """)
    claims = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('view_claims.html', claims=claims)

# ---------------- ADD AGENT ----------------
@app.route('/add_agent', methods=['GET', 'POST'])
def add_agent():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        branch = request.form['branch']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO agents (name, email, phone, branch)
            VALUES (%s, %s, %s, %s)
        """, (name, email, phone, branch))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_agent.html')

# ---------------- MAP AGENT TO CUSTOMER ----------------
@app.route('/map_agent', methods=['GET', 'POST'])
def map_agent():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT agent_id, name FROM agents")
    agents = cur.fetchall()
    cur.execute("SELECT customer_id, name FROM customers")
    customers = cur.fetchall()

    if request.method == 'POST':
        agent_id = request.form['agent_id']
        customer_id = request.form['customer_id']

        cur.execute("""
            INSERT INTO agent_customers (agent_id, customer_id)
            VALUES (%s, %s)
        """, (agent_id, customer_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    cur.close()
    conn.close()
    return render_template('map_agent.html', agents=agents, customers=customers)

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)
