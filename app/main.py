import streamlit as st
from budget_tracker import BudgetTracker

def main():
    st.title("Personal Budget Tracker")

    # Initialize BudgetTracker instance
    budget_tracker = BudgetTracker()

     # Add tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Upload CSV", "Add Expense", "Visualize Data"])

    with tab1:
        st.header("Upload CSV File")
        data = budget_tracker.upload_file()
    
    if budget_tracker.data is not None:
        with tab2:
            st.header("Add New Expense")
            budget_tracker.display_data()

        with tab3:
            st.header("Visualize Data")
            budget_tracker.visualize_data()

if __name__ == "__main__":
    main()