import streamlit as st
from datetime import datetime, timedelta
import json

# Page config
st.set_page_config(
    page_title="Bill-Pay Aggregator Startup Checklist",
    page_icon="💳",
    layout="wide"
)

# Initialize session state for checklist items
if 'checklist_state' not in st.session_state:
    st.session_state.checklist_state = {}

def create_checkbox(key, label, help_text=None):
    """Create a checkbox with persistent state"""
    if key not in st.session_state.checklist_state:
        st.session_state.checklist_state[key] = False
    
    checked = st.checkbox(label, value=st.session_state.checklist_state[key], key=f"cb_{key}", help=help_text)
    st.session_state.checklist_state[key] = checked
    return checked

def progress_bar(completed_items, total_items, phase_name):
    """Display progress bar for a phase"""
    progress = completed_items / total_items if total_items > 0 else 0
    st.progress(progress, text=f"{phase_name}: {completed_items}/{total_items} completed ({progress:.1%})")

# Title and intro
st.title("💳 Bill-Pay Aggregator Startup Checklist")
st.markdown("### One debit → All bills paid. Track your progress from idea to launch.")

# Sidebar for overall progress
st.sidebar.title("📊 Overall Progress")
total_completed = sum(1 for v in st.session_state.checklist_state.values() if v)
total_items = len(st.session_state.checklist_state) if st.session_state.checklist_state else 100  # Approximate

if st.session_state.checklist_state:
    st.sidebar.progress(total_completed / len(st.session_state.checklist_state))
    st.sidebar.write(f"**{total_completed}/{len(st.session_state.checklist_state)} tasks completed**")

# Export/Import functionality
if st.sidebar.button("📥 Export Progress"):
    st.sidebar.download_button(
        "Download Checklist State",
        data=json.dumps(st.session_state.checklist_state, indent=2),
        file_name=f"billpay_progress_{datetime.now().strftime('%Y%m%d')}.json",
        mime="application/json"
    )

uploaded_file = st.sidebar.file_uploader("📤 Import Progress", type="json")
if uploaded_file is not None:
    try:
        imported_state = json.loads(uploaded_file.read())
        st.session_state.checklist_state.update(imported_state)
        st.sidebar.success("Progress imported!")
        st.rerun()
    except:
        st.sidebar.error("Invalid file format")

# Main content in tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🔍 Phase A-F", "⚖️ Compliance", "🚀 MVP", "🏆 Competitors", "📈 Market", "👥 Team & Budget", "💰 Investor Pitch"
])

with tab1:
    st.header("Development Phases (Weeks 1-24)")
    
    # Phase A - Prove real demand (Weeks 1-3)
    st.subheader("📋 Phase A: Prove Real Demand (Weeks 1-3)")
    phase_a_tasks = []
    
    phase_a_tasks.append(create_checkbox(
        "define_promise", 
        "Define shortest promise: 'We take one payment and pay all your bills—on time, every time'"
    ))
    
    phase_a_tasks.append(create_checkbox(
        "recruit_users", 
        "Recruit 15-25 target users (busy households, roommates, freelancers, caregivers)"
    ))
    
    phase_a_tasks.append(create_checkbox(
        "smoke_test", 
        "Create no-code smoke test: 2-page site with Typeform for bill collection data"
    ))
    
    phase_a_tasks.append(create_checkbox(
        "success_metrics", 
        "Achieve success metrics: ≥40% email signups, ≥60% willing to connect bank + pay 3+ bills"
    ))
    
    progress_bar(sum(phase_a_tasks), len(phase_a_tasks), "Phase A")
    
    # Phase B - Regulatory & Bank Path (Weeks 2-6)
    st.subheader("🏛️ Phase B: Choose Regulatory & Bank Path (Weeks 2-6)")
    phase_b_tasks = []
    
    phase_b_tasks.append(create_checkbox(
        "research_agent_payee", 
        "Research 'Agent of Payee' model and state exemptions (CA DFPI guidance)"
    ))
    
    phase_b_tasks.append(create_checkbox(
        "evaluate_partners", 
        "Evaluate BaaS partners: Dwolla, Modern Treasury, Moov"
    ))
    
    phase_b_tasks.append(create_checkbox(
        "choose_path", 
        "Choose initial path: Partner with licensed provider for quick pilot"
    ))
    
    phase_b_tasks.append(create_checkbox(
        "compliance_plan", 
        "Plan compliance guardrails: Nacha WEB debits, Regulation E, OFAC screening"
    ))
    
    progress_bar(sum(phase_b_tasks), len(phase_b_tasks), "Phase B")
    
    # Phase C - MVP Design (Weeks 4-8)
    st.subheader("🎨 Phase C: MVP Design & Prototype (Weeks 4-8)")
    phase_c_tasks = []
    
    phase_c_tasks.append(create_checkbox(
        "user_flows", 
        "Design user flows: Link bank → set debit date → add billers → autopay rules"
    ))
    
    phase_c_tasks.append(create_checkbox(
        "bill_intake", 
        "Design bill intake: login to biller, scan/upload PDF, email parsing"
    ))
    
    phase_c_tasks.append(create_checkbox(
        "feasibility_hack", 
        "Plan feasibility hack: Doxo/Papaya-style scan+pay for long-tail billers"
    ))
    
    phase_c_tasks.append(create_checkbox(
        "figma_prototype", 
        "Create clickable Figma prototype and test with 15-25 users"
    ))
    
    progress_bar(sum(phase_c_tasks), len(phase_c_tasks), "Phase C")
    
    # Phase D - Build MVP (Weeks 8-16)
    st.subheader("⚙️ Phase D: Build MVP (Weeks 8-16)")
    phase_d_tasks = []
    
    st.write("**Tech Stack:**")
    phase_d_tasks.append(create_checkbox("frontend_stack", "Frontend: Next.js, TypeScript, Tailwind"))
    phase_d_tasks.append(create_checkbox("backend_stack", "Backend: Node (NestJS) or Python (FastAPI)"))
    phase_d_tasks.append(create_checkbox("database_stack", "Database: Postgres + row-level encryption, Redis queues"))
    phase_d_tasks.append(create_checkbox("infra_stack", "Infrastructure: AWS/GCP + managed secrets, VPC, security groups"))
    
    st.write("**Vendor Integrations:**")
    phase_d_tasks.append(create_checkbox("bank_linking", "Bank linking: Plaid or Mastercard Finicity"))
    phase_d_tasks.append(create_checkbox("ach_origination", "ACH origination: Dwolla/Moov/Modern Treasury"))
    phase_d_tasks.append(create_checkbox("kyc_aml", "KYC/AML: Persona/Alloy + OFAC checks"))
    phase_d_tasks.append(create_checkbox("check_fallback", "Check fallback for non-electronic billers"))
    
    st.write("**Risk & Funds Flow:**")
    phase_d_tasks.append(create_checkbox("funds_flow", "Implement conservative funds flow: T-0 debit, T-2/3 payout"))
    phase_d_tasks.append(create_checkbox("risk_policy", "Risk policy: No payout until debit settles, per-biller caps"))
    
    progress_bar(sum(phase_d_tasks), len(phase_d_tasks), "Phase D")
    
    # Phase E - Pilot (Weeks 16-24)
    st.subheader("🧪 Phase E: Pilot (Weeks 16-24)")
    phase_e_tasks = []
    
    phase_e_tasks.append(create_checkbox("private_beta", "Launch private beta with 200-500 users"))
    phase_e_tasks.append(create_checkbox("measure_metrics", "Measure: on-time %, late-fee reductions, failed debit rate, bills/user"))
    phase_e_tasks.append(create_checkbox("rtp_fednow", "Add RTP/FedNow for last-minute payments where supported"))
    
    progress_bar(sum(phase_e_tasks), len(phase_e_tasks), "Phase E")
    
    # Phase F - Go-to-Market (Months 6-12)
    st.subheader("🚀 Phase F: Go-to-Market & Fundraising (Months 6-12)")
    phase_f_tasks = []
    
    st.write("**Target Segments:**")
    phase_f_tasks.append(create_checkbox("roommate_segment", "Roommate/household splits with single source debit"))
    phase_f_tasks.append(create_checkbox("caregiver_segment", "Caregivers managing parents' bills"))
    phase_f_tasks.append(create_checkbox("gig_worker_segment", "Gig workers needing weekly smoothing"))
    
    phase_f_tasks.append(create_checkbox("pricing_model", "Set pricing: Free bank payments, $5-8/mo premium features"))
    
    progress_bar(sum(phase_f_tasks), len(phase_f_tasks), "Phase F")

with tab2:
    st.header("⚖️ Compliance Requirements")
    
    compliance_tasks = []
    
    st.subheader("📋 Legal Structure")
    compliance_tasks.append(create_checkbox(
        "mtl_research", 
        "Research Money Transmitter License requirements by state",
        "Most states require MTL unless using agent-of-payee exemption"
    ))
    
    compliance_tasks.append(create_checkbox(
        "agent_payee_contracts", 
        "Negotiate agent-of-payee contracts with major billers",
        "Written agreements needed for exemption in most states"
    ))
    
    st.subheader("🏦 Banking Compliance")
    compliance_tasks.append(create_checkbox(
        "nacha_web_debits", 
        "Implement Nacha WEB debit authentication and validation",
        "Must authenticate user and validate bank account for first-time WEB debits"
    ))
    
    compliance_tasks.append(create_checkbox(
        "regulation_e", 
        "Build Regulation E error resolution process",
        "10 business day investigation timeline, 60-day notice window"
    ))
    
    compliance_tasks.append(create_checkbox(
        "ofac_screening", 
        "Implement OFAC sanctions screening program",
        "Screen all counterparties and maintain documented controls"
    ))
    
    st.subheader("📄 Documentation")
    compliance_tasks.append(create_checkbox("compliance_docs", "Create compliance documentation and procedures"))
    compliance_tasks.append(create_checkbox("fintech_counsel", "Engage fintech counsel for regulatory guidance"))
    
    progress_bar(sum(compliance_tasks), len(compliance_tasks), "Compliance")

with tab3:
    st.header("🚀 MVP Features")
    
    mvp_tasks = []
    
    st.subheader("✅ Must-Have Features")
    mvp_tasks.append(create_checkbox("one_debit_many_bills", "One debit → many bills (monthly date + 'pay now')"))
    mvp_tasks.append(create_checkbox("bill_capture", "Bill capture: link accounts, scan bills, forward emails"))
    mvp_tasks.append(create_checkbox("payment_calendar", "Payment calendar with due-date guardrails and autopay rules"))
    mvp_tasks.append(create_checkbox("reconciliation", "Reconciliation center: status, payout rail, proof/confirmation"))
    
    st.subheader("🌟 V1 Differentiators")
    mvp_tasks.append(create_checkbox("weekly_smoothing", "Weekly smoothing: split monthly debit into four"))
    mvp_tasks.append(create_checkbox("last_minute_save", "Last-minute save: instant payout (RTP/FedNow) with service fee"))
    mvp_tasks.append(create_checkbox("household_mode", "Household mode: split bills among roommates"))
    mvp_tasks.append(create_checkbox("caregiver_mode", "Caregiver mode: manage multiple profiles with permissions"))
    
    progress_bar(sum(mvp_tasks), len(mvp_tasks), "MVP Features")

with tab4:
    st.header("🏆 Competitive Analysis")
    
    competitor_tasks = []
    
    st.subheader("🔍 Research Completed")
    competitors = [
        ("doxo", "Large pay-any-bill network, doxoBILLS experience"),
        ("Papaya", "Snap photo, pay any U.S. bill service"),
        ("PayPal Bill Pay", "Manage billers inside PayPal wallet"),
        ("Quicken Bill Manager", "Quick Pay and Check Pay in Quicken"),
        ("Chase Online Bill Pay", "Bank bill pay with eBills"),
        ("SoFi Bill Pay", "Schedule payments from SoFi checking"),
        ("Wells Fargo Bill Pay", "Mainstream bank bill pay"),
        ("Western Union Bill Pay", "Online/in-person biller payments"),
        ("MoneyGram Bill Pay", "Cash/in-person coverage"),
        ("SilverBills/Paytrust", "Concierge bill management for seniors")
    ]
    
    for comp_id, comp_desc in competitors:
        competitor_tasks.append(create_checkbox(f"research_{comp_id}", f"Research {comp_desc}"))
    
    st.subheader("📊 Differentiation Strategy")
    competitor_tasks.append(create_checkbox("diff_one_debit", "Define one-debit promise differentiation"))
    competitor_tasks.append(create_checkbox("diff_instant_payments", "Plan instant 'save me' payouts"))
    competitor_tasks.append(create_checkbox("diff_caregiver", "Design caregiver & household modes"))
    competitor_tasks.append(create_checkbox("diff_transparency", "Plan transparent fees and late-fee guarantee"))
    
    progress_bar(sum(competitor_tasks), len(competitor_tasks), "Competitive Analysis")

with tab5:
    st.header("📈 Market Analysis")
    
    market_tasks = []
    
    st.subheader("📊 Market Research")
    market_tasks.append(create_checkbox("tam_research", "Research total U.S. household bill spend (multi-trillion market)"))
    market_tasks.append(create_checkbox("payment_habits", "Analyze current payment habits (~22% via bank bill-pay)"))
    market_tasks.append(create_checkbox("household_count", "Validate U.S. household count (~132-134M in 2025)"))
    
    st.subheader("💰 Revenue Modeling")
    market_tasks.append(create_checkbox("freemium_model", "Model freemium pricing (free bank, $6/mo premium)"))
    market_tasks.append(create_checkbox("penetration_scenarios", "Calculate revenue scenarios (2% households = $187M ARR)"))
    market_tasks.append(create_checkbox("additional_revenue", "Plan card fees and B2B biller revenue-share"))
    
    progress_bar(sum(market_tasks), len(market_tasks), "Market Analysis")

with tab6:
    st.header("👥 Team & Budget")
    
    team_tasks = []
    
    st.subheader("👥 Team Assembly")
    roles = [
        ("Product Lead", "Lead product development and strategy"),
        ("Compliance Lead", "Fractional fintech counsel"),
        ("Senior Full-stack Engineer", "Lead technical development"),
        ("Backend/Payments Engineer", "Payments infrastructure"),
        ("Designer", "UI/UX design and user experience"),
        ("Ops/Support", "Operations and customer support")
    ]
    
    for role_id, role_desc in roles:
        team_tasks.append(create_checkbox(f"hire_{role_id.lower().replace(' ', '_')}", f"Hire {role_desc}"))
    
    st.subheader("💰 Budget Planning")
    team_tasks.append(create_checkbox("budget_plan", "Plan $300k-$700k build budget for first 6-9 months"))
    team_tasks.append(create_checkbox("vendor_costs", "Estimate vendor costs (Plaid, payments platform, legal)"))
    
    st.subheader("🎯 Milestones")
    milestones = [
        ("Month 2", "Clickable prototype + bank/payments partner selected"),
        ("Month 4", "MVP live with internal users; start private beta"),
        ("Month 6", "500+ beta users; KPIs on performance metrics"),
        ("Month 9", "Public launch + seed raise with real metrics")
    ]
    
    for milestone_id, milestone_desc in milestones:
        team_tasks.append(create_checkbox(f"milestone_{milestone_id.lower().replace(' ', '_')}", f"{milestone_id}: {milestone_desc}"))
    
    progress_bar(sum(team_tasks), len(team_tasks), "Team & Budget")

with tab7:
    st.header("💰 Investor Pitch Preparation")
    
    pitch_tasks = []
    
    st.subheader("📖 Narrative Elements")
    pitch_tasks.append(create_checkbox("problem_statement", "Craft problem: Americans juggle 10-15 bills, fragmented UX, late fees"))
    pitch_tasks.append(create_checkbox("solution_statement", "Define solution: One debit. All bills. Cash-flow smoothing + instant rescue"))
    pitch_tasks.append(create_checkbox("why_now", "Explain why now: Open banking + modern ACH/RTP rails + sponsor banks"))
    pitch_tasks.append(create_checkbox("market_size", "Present market: Multi-trillion annual volume, single-digit % served"))
    pitch_tasks.append(create_checkbox("moat_strategy", "Define moat: Biller network + agent contracts + guarantee data"))
    
    st.subheader("📊 Materials")
    pitch_tasks.append(create_checkbox("pitch_deck", "Create investor pitch deck"))
    pitch_tasks.append(create_checkbox("financial_model", "Build financial model with unit economics"))
    pitch_tasks.append(create_checkbox("demo_ready", "Prepare product demo"))
    pitch_tasks.append(create_checkbox("metrics_dashboard", "Create metrics dashboard for traction"))
    
    progress_bar(sum(pitch_tasks), len(pitch_tasks), "Investor Pitch")

# Footer with summary
st.divider()
st.subheader("📋 Quick Summary")
if st.session_state.checklist_state:
    total_tasks = len(st.session_state.checklist_state)
    completed_tasks = sum(1 for v in st.session_state.checklist_state.values() if v)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Tasks", total_tasks)
    with col2:
        st.metric("Completed", completed_tasks)
    with col3:
        st.metric("Completion Rate", f"{completed_tasks/total_tasks:.1%}" if total_tasks > 0 else "0%")
    
    if completed_tasks == total_tasks:
        st.balloons()
        st.success("🎉 Congratulations! You've completed all tasks. Ready to launch your bill-pay aggregator!")

# Reset button
if st.button("🔄 Reset All Progress", type="secondary"):
    st.session_state.checklist_state = {}
    st.rerun()
