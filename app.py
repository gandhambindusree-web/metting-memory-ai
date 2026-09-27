import streamlit as st
from hindsight_client import Hindsight

# Connect to local Hindsight
client = Hindsight(base_url="http://localhost:8888")

BANK_ID = "meeting-memory-app"

st.set_page_config(
    page_title="Meeting Memory AI",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Meeting Memory AI")
st.caption("Your meetings remember what you forget.")

st.divider()

# Save meeting
st.header("📝 Add Meeting Notes")

meeting_notes = st.text_area(
    "Enter your meeting notes",
    placeholder=(
        "Example:\n"
        "Client wants a dark-themed dashboard.\n"
        "Client prefers email updates.\n"
        "Project deadline is Friday."
    ),
    height=180
)

if st.button("💾 Remember Meeting", type="primary"):
    if not meeting_notes.strip():
        st.warning("Please enter meeting notes first.")
    else:
        with st.spinner("Saving meeting memory..."):
            result = client.retain(
                bank_id=BANK_ID,
                content=meeting_notes,
                retain_async=False
            )

        if result.success:
            st.success("✅ Meeting remembered by Hindsight!")
        else:
            st.error("Could not save the meeting.")

st.divider()

# Ask about meetings
st.header("💬 Ask About Previous Meetings")

question = st.text_input(
    "Ask a question",
    placeholder="What did the client want for the dashboard?"
)

if st.button("🔍 Recall Memory"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching Hindsight memory..."):
            result = client.recall(
                bank_id=BANK_ID,
                query=question
            )

        if result.results:
            st.success("🧠 Hindsight remembered:")
            
            for memory in result.results:
                st.write("•", memory.text)
        else:
            st.info("I couldn't find that information in the meeting memory.")