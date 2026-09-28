#!/usr/bin/env bash
source .venv/bin/activate
uvicorn app.main:app --reload
