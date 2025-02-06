
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def calculate_irr(cashflows, iterations=5000):
    rate = 0.1
    for _ in range(iterations):
        npv = sum(cf / (1 + rate)**t for t, cf in enumerate(cashflows))
        derivative = sum(-cf * t / (1 + rate)**(t+1) for t, cf in enumerate(cashflows))
        try:
            rate -= npv / derivative
        except ZeroDivisionError:
            break
        if abs(npv) < 1e-6:
            break
    return rate * 100

def create_cashflow_visualizations(cashflows):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Cash flow timeline
    periods = range(len(cashflows))
    ax1.bar(periods, cashflows, color=['red' if cf < 0 else 'green' for cf in cashflows])
    ax1.set_title('Cash Flow Timeline')
    ax1.set_xlabel('Period')
    ax1.set_ylabel('Amount')
    ax1.grid(True, alpha=0.3)
    
    # NPV sensitivity analysis
    rates = np.linspace(0, 0.5, 100)
    npvs = [sum(cf / (1 + r)**t for t, cf in enumerate(cashflows)) for r in rates]
    ax2.plot(rates, npvs, label='NPV Curve', color='purple')
    ax2.axhline(0, color='grey', linestyle='--')
    ax2.set_title('NPV vs Discount Rate')
    ax2.set_xlabel('Discount Rate')
    ax2.set_ylabel('NPV')
    ax2.grid(True, alpha=0.3)
    
    return fig

# Page configuration
st.set_page_config(page_title="IRR Calculator", layout="wide")
st.title('💵 Interactive IRR Calculator')
st.markdown("""
**A professional-grade Internal Rate of Return calculator with advanced visualization features**
""")

# Initialize default cash flows
default_data = {
    'Period': [0, 1, 2, 3],
    'Cash Flow': [-10000, 3000, 4200, 6800]
}

# Create editable DataFrame
with st.expander("📥 Edit Cash Flows", expanded=True):
    df = st.data_editor(
        pd.DataFrame(default_data),
        num_rows="dynamic",
        use_container_width=True,
        column_config={
            "Period": st.column_config.NumberColumn(
                format="%d",
                disabled=True
            ),
            "Cash Flow": st.column_config.NumberColumn(
                format="%d ¥",
                default=0
            )
        }
    )

# Process input data
cashflows = df['Cash Flow'].tolist()

# Input validation
if len(cashflows) < 2:
    st.error("❌ At least two periods required")
elif all(cf >= 0 for cf in cashflows):
    st.error("❌ Must include at least one negative cash flow (initial investment)")
else:
    try:
        with st.spinner('Calculating IRR...'):
            irr_result = calculate_irr(cashflows)
            
            # Main results columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Internal Rate of Return", 
                         f"{irr_result:.6f}%",
                         help="Discount rate that makes NPV zero")
            
            with col2:
                total_investment = -sum(cf for cf in cashflows if cf < 0)
                st.metric("Total Investment", 
                         f"¥{total_investment:,.0f}",
                         help="Sum of all negative cash flows")
            
            with col3:
                total_return = sum(cf for cf in cashflows if cf > 0)
                st.metric("Total Return", 
                         f"¥{total_return:,.0f}", 
                         delta=f"¥{total_return + cashflows[0]:,.0f} Net Profit")
            
            # Visualization section
            st.divider()
            st.subheader("📊 Financial Visualization")
            fig = create_cashflow_visualizations(cashflows)
            st.pyplot(fig)
            
            # Detailed data table
            with st.expander("🔍 View Detailed Calculations"):
                st.write("Cash Flow Details:")
                st.dataframe(df.style.format({
                    'Cash Flow': '${:,}'
                }), use_container_width=True)

    except Exception as e:
        st.error(f"Calculation error: {str(e)}")

# Help section
with st.expander("ℹ️ How to Use"):
    st.markdown("""
    1. **Edit Cash Flows** directly in the table:
       - Add/remove rows using + and - buttons
       - First period (0) should be negative (initial investment)
       - Subsequent periods should show returns
    2. **Visualizations** automatically update to show:
       - Cash flow distribution over time
       - NPV sensitivity to discount rates
    3. **Key Metrics** show:
       - IRR calculation result
       - Investment vs return analysis
    """)

st.caption("Note: Calculations use numerical approximation methods. Results may vary from financial software.")

import plotly.graph_objects as go

def calculate_future_value(capital_input, r, n, frequency=1):
    """
    Calculate the future value of a series of investments.
    
    :param capital_input: Amount invested each period
    :param r: Annual interest rate (decimal)
    :param n: Number of years
    :param frequency: Number of investments per year (1 for annual, 2 for semi-annual)
    :return: Future value of the investment
    """
    r_period = r / frequency
    total_periods = n * frequency
    future_value = capital_input * ((1 + r_period) ** total_periods - 1) / r_period
    return future_value

import streamlit as st
import plotly.graph_objects as go

# Function to calculate future value
def calculate_future_value(capital_input, r, n, frequency=1):
    """
    Calculate the future value of a series of investments.
    
    :param capital_input: Amount invested each period
    :param r: Annual interest rate (decimal)
    :param n: Number of years
    :param frequency: Number of investments per year (1 for annual, 2 for semi-annual)
    :return: Future value of the investment
    """
    r_period = r / frequency
    total_periods = n * frequency
    future_value = capital_input * ((1 + r_period) ** total_periods - 1) / r_period
    return future_value

# Function to plot investment growth
def plot_investment_growth(capital_input, r, n, frequency=1):
    """
    Plot the growth of an investment over time using Plotly.
    
    :param capital_input: Amount invested each period
    :param r: Annual interest rate (decimal)
    :param n: Number of years
    :param frequency: Number of investments per year (1 for annual, 2 for semi-annual)
    """
    years = list(range(n + 1))
    future_values = []

    for year in years:
        periods = year * frequency
        if periods == 0:
            future_values.append(0)
        else:
            future_value = capital_input * ((1 + r / frequency) ** periods - 1) / (r / frequency)
            future_values.append(future_value)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=future_values, mode='lines+markers', name='Investment Growth'))
    fig.update_layout(
        title=f"Investment Growth Over {n} Years (Rate: {r * 100}%)",
        xaxis_title="Years",
        yaxis_title="Future Value ($)",
        template="plotly_white"
    )
    return fig

# Streamlit app
def main():
    st.title("Investment Growth Calculator")
    st.write("This app calculates and visualizes the future value of periodic investments over time.")

    # Input fields
    capital_input = st.number_input("Capital Input per Period ($)", min_value=0.0, value=1000.0, step=100.0)
    r = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=5.0, step=0.1) / 100
    n = st.number_input("Number of Years", min_value=1, value=10, step=1)
    frequency = st.radio("Investment Frequency", ["Annual", "Semi-Annual"])

    # Convert frequency to numeric value
    frequency = 1 if frequency == "Annual" else 2

    # Calculate future value
    future_value = calculate_future_value(capital_input, r, n, frequency)

    # Display future value
    st.subheader(f"Future Value after {n} years: ${future_value:,.2f}")

    # Plot investment growth
    st.subheader("Investment Growth Over Time")
    fig = plot_investment_growth(capital_input, r, n, frequency)
    st.plotly_chart(fig)

# Run the app
if __name__ == "__main__":
    main()