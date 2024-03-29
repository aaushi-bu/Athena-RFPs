import os
import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Streamlit app title and description
st.title("Athena Proposal Generator")
st.write("Generate Proposal using AI")

# Input fields for user-provided information
client_name = st.text_input("Client Name", "")
purposes_defined = st.text_area("Project Purpose or Need", "")
duties_responsibilities = st.text_area("Scope and Deliverables Requested by Client", "")
deliverables = st.text_area("Required Qualifications", "")
athena_approach = st.text_area("Athena Approach", "")

# Generate RFP button
if st.button("Generate Proposal"):
    # Check if all required inputs are provided
    if client_name and purposes_defined and duties_responsibilities and deliverables and athena_approach:
        # Create the prompt using user-provided inputs
        prompt = f"Generate a Prposal for {client_name} to address the following purposes defined in the request:\n\n{purposes_defined}\n\nThe client has specified the following scope and deliverables:\n\n{duties_responsibilities}\n\nThe required qualifications expected include:\n\n{deliverables}\n\nThe proposal should also incorporate the Company's approach as follows:\n\n{athena_approach}"

        # Generate RFP using OpenAI's GPT-3.5 Turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant that generates Proposals from requirements shared by the client."}, {"role": "user", "content": prompt}],
        )

        # Extract and display the generated RFP
        proposal_message = response["choices"][0]["message"]["content"]
        st.subheader("Generated Proposal:")
        st.write(proposal_message)
    else:
        st.warning("Please fill in all required fields.")

# Footer
st.write("Powered by Athena AI Solutions")
