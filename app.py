def calculate_advanced_metrics(...):
    risk = round(...)  # rounding whole numbers
    remaining_pct = round(remaining_pct)
    blocker_pct = round(blocker_pct)
    not_started_pct = round(not_started_pct)
    velocity_gap_pct = round(velocity_gap_pct)

# ... other function modifications


def get_risk_status(...):
    risk_percentage = round(risk_percentage)  # round without decimals
    # other logic


# In Current Sprint summary metrics
committed_sp = round(committed_sp)
ideal_burn_rate = round(ideal_burn_rate)
completed_sp_summary = round(completed_sp_summary)
required_burn_rate = round(required_burn_rate)
spillover_risk_pct = round(spillover_risk_pct)
remaining_sp_summary = round(remaining_sp_summary)


# In Predictive KPI cards and indicator
success_probability = round(success_probability)  # no decimals
spillover_sp = round(spillover_sp)
risk_index = round(risk_index)
confidence_score = round(confidence_score)

# Modifying displayed confidence text


# In What-If Analysis
simulated_risk = round(simulated_risk)  # no decimals


# In both prepare_llm_summary and generate_ai_insights
prompt_formatting = '{:.0f}'  # changed to no decimals