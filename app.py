import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Check Balance",
        "Send Money",
        "Update Details",
        "Delete Account"
    ]
)

# =========================
# CREATE ACCOUNT
# =========================

if menu == "Create Account":

    st.header("Create Account")

    with st.form("create_account_form"):

        name = st.text_input("Name", key="create_name")
        email = st.text_input("Email", key="create_email")
        age = st.number_input(
            "Age",
            min_value=1,
            step=1,
            key="create_age"
        )
        pin = st.text_input(
            "PIN",
            type="password",
            key="create_pin"
        )

        submitted = st.form_submit_button(
            "Create Account"
        )

        if submitted:

            accNo = bank.create_account(
                name,
                email,
                age,
                pin
            )

            st.success("Account Created Successfully")
            st.info(f"Your Account Number: {accNo}")

# =========================
# DEPOSIT
# =========================

elif menu == "Deposit Money":

    st.header("Deposit Money")

    with st.form("deposit_form"):

        accNo = st.text_input(
            "Account Number",
            key="deposit_acc"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            key="deposit_pin"
        )

        amount = st.number_input(
            "Amount",
            min_value=1,
            step=1,
            key="deposit_amount"
        )

        submitted = st.form_submit_button(
            "Deposit"
        )

    if submitted:

        status, msg = bank.deposit(
            accNo,
            pin,
            amount
        )

        if status:
            st.success(
                f"Current Balance: ₹{msg}"
            )
        else:
            st.error(msg)

# =========================
# WITHDRAW
# =========================

elif menu == "Withdraw Money":

    st.header("Withdraw Money")

    with st.form("withdraw_form"):

        accNo = st.text_input(
            "Account Number",
            key="withdraw_acc"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            key="withdraw_pin"
        )

        amount = st.number_input(
            "Amount",
            min_value=1,
            step=1,
            key="withdraw_amount"
        )

        submitted = st.form_submit_button(
            "Withdraw"
        )

    if submitted:

        status, msg = bank.withdraw(
            accNo,
            pin,
            amount
        )

        if status:
            st.success(
                f"Remaining Balance: ₹{msg}"
            )
        else:
            st.error(msg)

# =========================
# CHECK BALANCE
# =========================

elif menu == "Check Balance":

    st.header("Check Balance")

    with st.form("balance_form"):

        accNo = st.text_input(
            "Account Number",
            key="balance_acc"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            key="balance_pin"
        )

        submitted = st.form_submit_button(
            "Check Balance"
        )

    if submitted:

        status, msg = bank.check_balance(
            accNo,
            pin
        )

        if status:
            st.success(
                f"Current Balance: ₹{msg}"
            )
        else:
            st.error(msg)

# =========================
# SEND MONEY
# =========================

elif menu == "Send Money":

    st.header("Send Money")

    with st.form("send_money_form"):

        sender = st.text_input(
            "Sender Account Number",
            key="sender_acc"
        )

        pin = st.text_input(
            "Sender PIN",
            type="password",
            key="sender_pin"
        )

        receiver = st.text_input(
            "Receiver Account Number",
            key="receiver_acc"
        )

        amount = st.number_input(
            "Amount",
            min_value=1,
            step=1,
            key="send_amount"
        )

        submitted = st.form_submit_button(
            "Transfer"
        )

    if submitted:

        status, msg = bank.send_money(
            sender,
            pin,
            receiver,
            amount
        )

        if status:
            st.success(msg)
        else:
            st.error(msg)

# =========================
# UPDATE DETAILS
# =========================

elif menu == "Update Details":

    st.header("Update Details")

    with st.form("update_form"):

        accNo = st.text_input(
            "Account Number",
            key="update_acc"
        )

        pin = st.text_input(
            "Current PIN",
            type="password",
            key="update_pin"
        )

        update_option = st.selectbox(
            "What do you want to update?",
            [
                "Name",
                "PIN",
                "Email"
            ],
            key="update_option"
        )

        new_value = st.text_input(
            "New Value",
            key="update_value"
        )

        submitted = st.form_submit_button(
            "Update"
        )

    if submitted:

        success = False

        if update_option == "Name":
            success = bank.update_name(
                accNo,
                pin,
                new_value
            )

        elif update_option == "PIN":
            success = bank.update_pin(
                accNo,
                pin,
                new_value
            )

        elif update_option == "Email":
            success = bank.update_email(
                accNo,
                pin,
                new_value
            )

        if success:
            st.success(
                "Updated Successfully"
            )
        else:
            st.error(
                "Account Not Found"
            )

# =========================
# DELETE ACCOUNT
# =========================

elif menu == "Delete Account":

    st.header("Delete Account")

    with st.form("delete_form"):

        accNo = st.text_input(
            "Account Number",
            key="delete_acc"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            key="delete_pin"
        )

        submitted = st.form_submit_button(
            "Delete Account"
        )

    if submitted:

        success = bank.delete_account(
            accNo,
            pin
        )

        if success:
            st.success(
                "Account Deleted Successfully"
            )
        else:
            st.error(
                "Account Not Found"
            )