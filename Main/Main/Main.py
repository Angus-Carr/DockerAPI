
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Data model for a journal entry
class JournalEntry(BaseModel):
    id: int
    title: str
    content: str

# In-memory "database"
entries = []

# GET /Entries - Return all journal entries
@app.get("/Entries", response_model=List[JournalEntry])
def get_entries():
    return entries

# GET /Entries/{id} - Return a journal entry by id
@app.get("/Entries/{id}", response_model=JournalEntry)
def get_entry(id: int):
    for entry in entries:
        if entry.id == id:
            return entry
    raise HTTPException(status_code=404, detail="Entry not found")

# POST /Entries - Create a new entry
@app.post("/Entries", response_model=JournalEntry, status_code=201)
def create_entry(entry: JournalEntry):
    # Check if entry with same id exists
    for e in entries:
        if e.id == entry.id:
            raise HTTPException(status_code=400, detail="Entry with this ID already exists")
    entries.append(entry)
    return entry

# PUT /Entries/{id} - Update an existing entry
@app.put("/Entries/{id}", response_model=JournalEntry)
def update_entry(id: int, updated_entry: JournalEntry):
    for i, entry in enumerate(entries):
        if entry.id == id:
            entries[i] = updated_entry
            return updated_entry
    raise HTTPException(status_code=404, detail="Entry not found")

# DELETE /Entries/{id} - Delete an entry
@app.delete("/Entries/{id}", status_code=204)
def delete_entry(id: int):
    for i, entry in enumerate(entries):
        if entry.id == id:
            entries.pop(i)
            return
    raise HTTPException(status_code=404, detail="Entry not found")