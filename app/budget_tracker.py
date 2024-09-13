import streamlit as st 
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go
from dataclasses import dataclass
from loggers import setup_logger
from exceptions import NoDataError

logger = setup_logger()

@dataclass
class BudgetTracker:
    data: pd.DataFrame = None 

    def upload_file(self):
        """
        Upload CSV file function.
        Returns:
            pd.DataFrame: Uploaded data
        """
        try:
            uploaded_file = st.file_uploader("Upload your csv file", type=["csv"])
            if uploaded_file is not None:
                self.data = pd.read_csv(uploaded_file)
                st.success("File uploaded successfully")
                logger.info("File uploaded successfully")
            else:
                raise NoDataError
        except NoDataError as e:
            st.warning(str(e))
            logger.error(f"File upload failed: {e}")
        return self.data 

    def display_data(self):
        """
        Displays data in DataFrame format.
        """
        try:
            if self.data is not None:
                st.dataframe(self.data)
                logger.info("Data is displayed successfully")
            else:
                raise NoDataError("No data to display")
        except NoDataError as e:
            st.warning(str(e))
            logger.error(f"Display data failed: {e}")

    def visualize_data(self):
        """
        Visualizes the data using bar and pie charts
        """
        try:
            if self.data is not None:
                st.subheader("Expense Breakdown by category")
                selected_categories = st.multiselect(
                     "Filter by Category (Optional)", options=self.data["Category"].unique(), default=self.data["Category"].unique()
                )
                filtered_data = self.data[self.data["Category"].isin(selected_categories)]
                
                # Bar chart
                category_expense = filtered_data.groupby("Category").sum()["Amount"].reset_index()

                # Using Plotly for more customization
                fig_bar = px.bar(
                    category_expense,
                    x="Category",
                    y="Amount",
                    title="Expense Breakdown by Category",
                    color="Category",
                    text="Amount",  # Display the amount on the bars
                    labels={"Amount": "Total Amount ($)", "Category": "Expense Category"},
                    template="plotly_dark",  # Optional: dark theme
                )

                fig_bar.update_traces(texttemplate='$%{text:.2s}', textposition='outside')
                fig_bar.update_layout(showlegend=False, height=500)
                
                # Display the bar chart
                st.plotly_chart(fig_bar)

                # --- Pie Chart: Payment Method Breakdown ---
                st.subheader("Payment Methods Breakdown")

                payment_method_expense = filtered_data.groupby("Payment Method").sum()["Amount"].reset_index()

                fig_pie = px.pie(
                    payment_method_expense,
                    values="Amount",
                    names="Payment Method",
                    title="Expenses by Payment Method",
                    hover_data=['Amount'],
                    labels={"Amount": "Total Amount ($)"},
                    color_discrete_sequence=px.colors.qualitative.Pastel,  # Use pastel colors for the pie chart
                    hole=0.3,  # Create a donut chart
                )
                fig_pie.update_traces(textposition='inside', textinfo='percent+label')

                # Display the pie chart
                st.plotly_chart(fig_pie)

                # Log success
                logger.info("Data visualized successfully")
            
            else:
                raise NoDataError("No data to visualize")
        except NoDataError as e:
            st.warning(str(e))
            logger.error(f"Data visualization failed: {e}")