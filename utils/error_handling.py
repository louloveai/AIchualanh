import logging
import streamlit as st

logger = logging.getLogger(__name__)

def handle_error(message: str, error: Exception):
    """Centralized error handling"""
    logger.error(f"{message}: {str(error)}")
    st.error(f"⚠️ {message}. Please try again later or contact support.")
