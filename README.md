# Meeting Memory AI

Your meetings remember what you forget.

Meeting Memory AI is a simple AI application that uses Hindsight agent memory to remember important information from meetings and recall it later.

## Problem

Important decisions from meetings are easy to forget. Users often have to search old notes or ask the same questions again.

## Solution

Meeting Memory AI stores important meeting information using Hindsight memory.

A user can:
- Add meeting notes
- Store important client requirements
- Start a fresh conversation
- Ask questions about previous meetings
- Recall information using Hindsight

## Example

Meeting notes:

- Client wants a dark-themed dashboard.
- Client prefers email updates.
- Project deadline is Friday.

Later, the user can ask:

"What did the client want for the dashboard?"

Hindsight recalls:

"Client wants a dark-themed dashboard."

## Technology

- Python
- Streamlit
- Hindsight Agent Memory
- Hindsight Python Client
- Groq

## How Hindsight is Used

Meeting information is stored using Hindsight retain and retrieved using Hindsight recall.

```python
client.retain(
    bank_id=BANK_ID,
    content=meeting_notes,
    retain_async=True
)

result = client.recall(
    bank_id=BANK_ID,
    query=question
)
