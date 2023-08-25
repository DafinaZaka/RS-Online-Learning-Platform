#!/bin/bash
streamlit run --server.port 8501 app.py &
streamlit run --server.port 8502 chatapi.py


# Keep the script running to allow the processes to continue running
tail -f /dev/null
