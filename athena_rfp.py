import streamlit as st
import os
from openai import OpenAI



client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

# Streamlit app title and description
st.title("Athena RFP Generator")
st.write("Generate Request for Proposal (RFP) using AI")

# Input fields for user-provided information
client_name = st.text_input("Client Name", "")
purposes_defined = st.text_area("Purposes Defined in the RFP", "")
duties_responsibilities = st.text_area("Duties or Responsibilities mentioned by the Client", "")
deliverables = st.text_area("Deliverables", "")
athena_approach = st.text_area("Athena Approach to be Included", "")

# Generate RFP button
if st.button("Generate RFP"):
    # Check if all required inputs are provided
    if client_name and purposes_defined and duties_responsibilities and deliverables and athena_approach:
        # Create the prompt using user-provided inputs
        prompt = f"Generate a Request for Proposal (RFP) for {client_name} to address the following purposes defined in the RFP:\n\n{purposes_defined}\n\nThe client has specified the following duties or responsibilities:\n\n{duties_responsibilities}\n\nThe deliverables expected include:\n\n{deliverables}\n\nThe proposal should also incorporate the Athena approach as follows:\n\n{athena_approach}"

        # Generate RFP using OpenAI's GPT-3
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=2000,
        )

        # Display the generated RFP
        st.subheader("Generated RFP:")
        st.write(response.choices[0].text)
    else:
        st.warning("Please fill in all required fields.")

# Footer
st.write("Powered by OpenAI's GPT-3")
