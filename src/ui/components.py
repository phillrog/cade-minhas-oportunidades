import streamlit as st
import pathlib
import os

class UIComponents:
    """Gerencia a parte visual e injeção de assets."""
    
    @staticmethod
    def inject_css(css_path: str):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))     
        caminho_ajustado = css_path.lstrip('/')
        caminho_final = os.path.join(diretorio_atual, '..', caminho_ajustado)
        
        try:
            with open(caminho_final, "r", encoding="utf-8") as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        except FileNotFoundError:
            st.error(f"Arquivo não encontrado em: {caminho_final}")

    @staticmethod
    def render_marquee_header():
        st.markdown(f"""
        <div class="marquees-container">
            <section class="marquee">
                <div class="marquee--inner">                
                    <p>FULLSTACK .NET SÊNIOR</p><p>VAGAS .NET C#</p><p>VAGA REMOTO</p>
                    <p>CADÊ MINHAS OPORTUNIDADES</p><p>PRESENCIAL, HÍBRIDO OU REMOTO</p><p>SALÁRIOS ACIMA DA MÉDIA</p>
                    <p>CONTRATAÇÃO IMEDIATA</p><p>VAGAS .NET ANGULAR</p><p>VAGA PRESENCIAL</p>
                </div>
            </section>
            <section class="marquee">
                <div class="marquee--inner">
                    <p>CADÊ MINHAS OPORTUNIDADES</p><p>PRESENCIAL, HÍBRIDO OU REMOTO</p><p>SALÁRIOS ACIMA DA MÉDIA</p>
                    <p>CONTRATAÇÃO IMEDIATA</p><p>VAGAS .NET ANGULAR</p><p>VAGA PRESENCIAL</p>
                    <p>CADÊ MINHAS OPORTUNIDADES</p><p>PRESENCIAL, HÍBRIDO OU REMOTO</p><p>SALÁRIOS ACIMA DA MÉDIA</p>
                </div>
            </section>
        </div>
        <p style="text-align: center; color: #888;">Encontre sua próxima oportunidade com filtros avançados</p>
        """, unsafe_allow_html=True)