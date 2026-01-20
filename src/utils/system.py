import streamlit as st

class SystemTools:
    """Encapsula operações de estado e sistema do Streamlit."""
    
    @staticmethod
    def reset_app():
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()