#!/usr/bin/env python
"""
Run the FastAPI server.
Database initialization is handled automatically by the app lifespan
(Base.metadata.create_all + schema migrations).
"""
import os
import sys

print("=" * 60)
print("Starting ZeroTrace server...")
print("Database initialization will be handled by the app lifespan.")
print("=" * 60)

# Run the server
os.execvp(sys.executable, [sys.executable, "run.py"])

