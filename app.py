import streamlit as st
import requests
import json
from datetime import datetime
import time
import re

# Page configuration
st.set_page_config(
    page_title="Bundle Pay - Send Money Safely Worldwide",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main > div {
        padding: 0;
    }
    
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        text-align: center;
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border: 1px solid #e1e8ed;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .cta-section {
        background: #f8f9fa;
        padding: 3rem 2rem;
        border-radius: 10px;
        text-align: center;
        margin: 2rem 0;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
        display: block;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        margin: 2rem 0;
    }
    
    .success-message {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    
    .error-message {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
        margin: 1rem 0;
    }
    
    .footer {
        background: #2c3e50;
        color: white;
        padding: 2rem;
        text-align: center;
        margin-top: 3rem;
        border-radius: 10px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e1e8ed;
        padding: 0.75rem;
    }
    
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #e1e8ed;
        padding: 0.75rem;
    }
    
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e1e8ed;
        padding: 0.75rem;
    }
</style>
""", unsafe_allow_html=True)

# N8N Webhook Configuration
N8N_WEBHOOK_URL = "https://your-n8n-instance.com/webhook/bundle-pay-form"  # Replace with your actual webhook URL

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    # Basic phone validation - adjust regex based on your requirements
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern, phone.replace(' ', '').replace('-', '')) is not None

def send_to_n8n(data):
    """Send form data to n8n webhook"""
    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        return response.status_code == 200, response
    except requests.exceptions.RequestException as e:
        return False, str(e)

# Header Section
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">💰 Bundle Pay</h1>
    <p class="hero-subtitle">Send Money Safely Worldwide - Fast, Secure, Affordable</p>
    <p style="font-size: 1.1rem; opacity: 0.8;">Join millions who trust Bundle Pay for international money transfers</p>
</div>
""", unsafe_allow_html=True)

# Stats Section
st.markdown("""
<div class="stats-container">
    <div class="stat-item">
        <span class="stat-number">25+</span>
        <span class="stat-label">Countries</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">2M+</span>
        <span class="stat-label">Happy Users</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">$50B+</span>
        <span class="stat-label">Transferred</span>
    </div>
    <div class="stat-item">
        <span class="stat-number">0.5%</span>
        <span class="stat-label">Low Fees</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("## Why Choose Bundle Pay?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🚀</div>
        <h3>Lightning Fast</h3>
        <p>Send money in seconds, not days. Most transfers complete within minutes.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔒</div>
        <h3>Bank-Level Security</h3>
        <p>256-bit encryption, 2FA, and regulatory compliance keep your money safe.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💡</div>
        <h3>Smart Rates</h3>
        <p>Get the best exchange rates with transparent, low fees. No hidden charges.</p>
    </div>
    """, unsafe_allow_html=True)

# Second row of features
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🌍</div>
        <h3>Global Reach</h3>
        <p>Send to 25+ countries across Africa, Asia, and Latin America.</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📱</div>
        <h3>Mobile First</h3>
        <p>Use our award-winning mobile app or web platform anywhere, anytime.</p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎧</div>
        <h3>24/7 Support</h3>
        <p>Get help when you need it with our round-the-clock customer support.</p>
    </div>
    """, unsafe_allow_html=True)

# Contact Form Section
st.markdown("## Get Started Today")
st.markdown("**Ready to send money worldwide? Fill out the form below and our team will contact you within 24 hours.**")

# Initialize session state for form
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'form_success' not in st.session_state:
    st.session_state.form_success = False

# Contact Form
with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    with st.form("bundle_pay_contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name *", placeholder="Enter your first name")
            email = st.text_input("Email Address *", placeholder="your.email@example.com")
            country = st.selectbox("Country *", [
                "", "United States", "Canada", "United Kingdom", "Nigeria", "Kenya", 
                "Ghana", "South Africa", "Uganda", "Tanzania", "Rwanda", "India", 
                "Philippines", "Mexico", "Brazil", "Colombia", "Other"
            ])
        
        with col2:
            last_name = st.text_input("Last Name *", placeholder="Enter your last name")
            phone = st.text_input("Phone Number *", placeholder="+1234567890")
            transfer_purpose = st.selectbox("Primary Transfer Purpose *", [
                "", "Family Support", "Business Payments", "Education Fees", 
                "Medical Expenses", "Investment", "Other"
            ])
        
        monthly_volume = st.selectbox("Expected Monthly Transfer Volume", [
            "", "Under $500", "$500 - $2,000", "$2,000 - $10,000", 
            "$10,000 - $50,000", "Over $50,000"
        ])
        
        message = st.text_area("Additional Information", 
                              placeholder="Tell us about your specific needs or any questions you have...")
        
        # Marketing consent
        marketing_consent = st.checkbox("I would like to receive updates about Bundle Pay services and promotions")
        terms_consent = st.checkbox("I agree to Bundle Pay's Terms of Service and Privacy Policy *")
        
        submitted = st.form_submit_button("Send My Information", use_container_width=True)
        
        if submitted:
            # Validation
            errors = []
            
            if not first_name or not first_name.strip():
                errors.append("First name is required")
            
            if not last_name or not last_name.strip():
                errors.append("Last name is required")
            
            if not email or not validate_email(email):
                errors.append("Please enter a valid email address")
            
            if not phone or not validate_phone(phone):
                errors.append("Please enter a valid phone number")
            
            if not country:
                errors.append("Please select your country")
            
            if not transfer_purpose:
                errors.append("Please select your primary transfer purpose")
            
            if not terms_consent:
                errors.append("You must agree to the Terms of Service and Privacy Policy")
            
            if errors:
                for error in errors:
                    st.markdown(f'<div class="error-message">❌ {error}</div>', unsafe_allow_html=True)
            else:
                # Prepare data for n8n webhook
                form_data = {
                    "form_type": "contact_inquiry",
                    "timestamp": datetime.now().isoformat(),
                    "personal_info": {
                        "first_name": first_name.strip(),
                        "last_name": last_name.strip(),
                        "email": email.strip().lower(),
                        "phone": phone.strip(),
                        "country": country
                    },
                    "transfer_info": {
                        "primary_purpose": transfer_purpose,
                        "expected_monthly_volume": monthly_volume
                    },
                    "message": message.strip() if message else "",
                    "consent": {
                        "marketing": marketing_consent,
                        "terms": terms_consent
                    },
                    "source": "streamlit_landing_page",
                    "user_agent": "Streamlit App",
                    "lead_score": 75 if monthly_volume in ["$2,000 - $10,000", "$10,000 - $50,000", "Over $50,000"] else 50
                }
                
                # Show loading spinner
                with st.spinner("Sending your information..."):
                    success, response = send_to_n8n(form_data)
                
                if success:
                    st.markdown("""
                    <div class="success-message">
                        ✅ <strong>Thank you!</strong> Your information has been sent successfully. 
                        Our team will contact you within 24 hours to help you get started with Bundle Pay.
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.markdown(f"""
                    <div class="error-message">
                        ❌ <strong>Oops!</strong> There was an error sending your information. 
                        Please try again or contact us directly at support@bundlepay.com
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Show technical error in expander for debugging
                    with st.expander("Technical Details"):
                        st.error(f"Error: {response}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# How It Works Section
st.markdown("## How Bundle Pay Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    **1. Sign Up** 📝  
    Create your free account in minutes with just your email and phone number.
    """)

with col2:
    st.markdown("""
    **2. Verify Identity** 🆔  
    Upload your ID for security and compliance. Quick verification process.
    """)

with col3:
    st.markdown("""
    **3. Send Money** 💸  
    Enter recipient details, choose payment method, and send instantly.
    """)

with col4:
    st.markdown("""
    **4. Track Transfer** 📍  
    Monitor your transfer in real-time until it reaches the recipient.
    """)

# Testimonials Section
st.markdown("## What Our Customers Say")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    > *"Bundle Pay made sending money to my family in Nigeria so easy and affordable. 
    > The transfer was instant and the customer service is excellent!"*
    > 
    > **Sarah M.** - New York, USA
    """)

with col2:
    st.markdown("""
    > *"As a business owner, I needed reliable international payments. 
    > Bundle Pay's API integration was seamless and their rates are unbeatable."*
    > 
    > **David K.** - London, UK
    """)

# CTA Section
st.markdown("""
<div class="cta-section">
    <h2>Ready to Send Money Worldwide?</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem;">
        Join millions of satisfied customers who trust Bundle Pay for their international transfers.
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <h3>Bundle Pay</h3>
    <p>Send Money Safely Worldwide</p>
    <p>
        📧 support@bundlepay.com | 📞 +1-800-BUNDLE-0 | 🌐 bundlepay.com
    </p>
    <p style="margin-top: 1rem; opacity: 0.7;">
        © 2025 Bundle Pay. All rights reserved. | Licensed Money Transmitter | 
        <a href="#" style="color: white;">Privacy Policy</a> | 
        <a href="#" style="color: white;">Terms of Service</a>
    </p>
</div>
""", unsafe_allow_html=True)

# Floating Chat Widget (Optional)
if st.sidebar.button("💬 Chat with Support"):
    st.sidebar.info("""
    **Live Chat Available 24/7**
    
    • General Questions
    • Transfer Support  
    • Account Help
    • Technical Issues
    
    Chat with our AI assistant or connect with a human agent.
    """)

# Sidebar with quick stats and links
st.sidebar.markdown("### Quick Actions")
st.sidebar.markdown("🔗 [Download Mobile App](https://bundlepay.com/app)")
st.sidebar.markdown("📊 [Check Exchange Rates](https://bundlepay.com/rates)")
st.sidebar.markdown("🏢 [Business Solutions](https://bundlepay.com/business)")
st.sidebar.markdown("📚 [Help Center](https://bundlepay.com/help)")

st.sidebar.markdown("### Transfer Calculator")
with st.sidebar.form("quick_calc"):
    send_amount = st.number_input("Send Amount ($)", min_value=1.0, value=100.0)
    to_country = st.selectbox("To Country", ["Nigeria", "Kenya", "Ghana", "India", "Philippines"])
    
    if st.form_submit_button("Calculate"):
        # Mock calculation - replace with real API call
        fee = send_amount * 0.005  # 0.5% fee
        exchange_rate = 0.85  # Mock rate
        recipient_gets = (send_amount - fee) * exchange_rate
        
        st.sidebar.success(f"""
        **Transfer Summary:**
        - Send: ${send_amount:.2f}
        - Fee: ${fee:.2f}
        - Recipient gets: ${recipient_gets:.2f}
        """)
