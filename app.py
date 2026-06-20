import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Interview Application Tracker")

st.title("💻 Interview Application Tracker")
st.write("Track your job applications and interview progress.")

application_id = st.number_input(
    "Application ID",
    min_value=1,
    step=1
)

company = st.text_input("Company Name")

role = st.text_input("Role")

location = st.text_input("Location")

status = st.selectbox(
    "Application Status",
    [
        "Applied",
        "Shortlisted",
        "Assessment",
        "Interview Round 1",
        "Interview Round 2",
        "HR Round",
        "Selected",
        "Rejected"
    ]
)

salary = st.text_input("Expected Salary")

application_date = st.date_input("Application Date")

job_link = st.text_input("Job Link")

notes = st.text_area("Notes")

# Submit Application
if st.button("Submit Application", key="submit_btn"):

    data = {
        "id": application_id,
        "company": company,
        "role": role,
        "location": location,
        "status": status,
        "salary": salary,
        "application_date": str(application_date),
        "job_link": job_link,
        "notes": notes
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/applications",
            json=data
        )

        if response.status_code == 200:
            st.success("✅ Application Added Successfully")
        else:
            st.error(response.json()["detail"])

    except Exception as e:
        st.error(f"Backend Connection Error: {e}")

st.divider()

# Show Applications
if st.button("Show Applications", key="show_btn"):

    try:
        response = requests.get(
            "http://127.0.0.1:8000/applications"
        )

        if response.status_code == 200:

            applications = response.json()

            if applications:
                df = pd.DataFrame(applications)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No applications found.")

        else:
            st.error("Failed to fetch applications.")

    except Exception as e:
        st.error(f"Backend Connection Error: {e}")
st.header("📊 Dashboard")

try:
    response = requests.get("http://127.0.0.1:8000/applications")

    if response.status_code == 200:
        applications = response.json()

        total = len(applications)

        selected = len([
            app for app in applications
            if app["status"] == "Selected"
        ])

        rejected = len([
            app for app in applications
            if app["status"] == "Rejected"
        ])

        pending = total - selected - rejected

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total", total)
        col2.metric("Selected", selected)
        col3.metric("Rejected", rejected)
        col4.metric("Pending", pending)

except Exception as e:
    st.error(e)
st.divider()
st.header("✏️ Update Application")

update_id = st.number_input(
    "Application ID to Update",
    min_value=1,
    key="update_id"
)

if st.button("Update Application", key="update_btn"):

    updated_data = {
        "id": update_id,
        "company": company,
        "role": role,
        "location": location,
        "status": status,
        "salary": salary,
        "application_date": str(application_date),
        "job_link": job_link,
        "notes": notes
    }

    response = requests.put(
        f"http://127.0.0.1:8000/applications/{update_id}",
        json=updated_data
    )

    if response.status_code == 200:
        st.success("Application Updated Successfully")
    else:
        st.error(response.json()["detail"])
st.divider()
st.header("🗑️ Delete Application")

delete_id = st.number_input(
    "Application ID to Delete",
    min_value=1,
    key="delete_id"
)

if st.button("Delete Application", key="delete_btn"):

    response = requests.delete(
        f"http://127.0.0.1:8000/applications/{delete_id}"
    )

    if response.status_code == 200:
        st.success("Application Deleted Successfully")
    else:
        st.error(response.json()["detail"])
st.divider()

if st.button("Refresh Applications", key="refresh_btn"):

    response = requests.get(
        "http://127.0.0.1:8000/applications"
    )

    if response.status_code == 200:

        data = response.json()

        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No Applications Found")