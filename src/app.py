import streamlit as st
from streamlit_tags import st_tags
from datetime import date, timedelta

from core.dork import Dork
from ui.components import UIComponents
from utils.system import SystemTools

st.set_page_config(page_title="Cadê minhas oportunidades ?", layout="wide")
UIComponents.inject_css("assets/styles.css") 
UIComponents.render_marquee_header()

# Layout de Colunas
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("**Título (intitle):**", help="Palavras que DEVEM aparecer no título da vaga ou post. Ex: 'Sênior', 'Angular', 'C#'.")
    t_titulo = st_tags(
        label='',
        text='Digite e aperte ENTER',
        value=['ANGULAR', 'C#'],
        key='techs'
    )

    st.markdown("**Termos Obrigatórios (Corpo):**", help="Palavras que devem existir em qualquer lugar da descrição da vaga (CLT, PJ, Azure, etc).")
    t_obrigatorios = st_tags(
        label='',
        text='Digite e aperte ENTER',
        value=['.NET', 'BRASIL'],
        key='must'
    )

with col_b:
    st.markdown("**Regime de Trabalho:**", help="Filtra postagens que mencionam estas modalidades de trabalho.")
    t_regime = st_tags(
        label='',
        text='Digite e aperte ENTER',
        value=['REMOTO', 'HOME OFFICE'],
        key='regime'
    )
    st.markdown("**Excluir Termos (-):**", help="Remove resultados que contenham estas palavras.")
    t_exclusoes = st_tags(
        label='',
        text='Digite e aperte ENTER',
        value=[],
        key='excl'
    )

# Período
st.markdown("---")
st.write("**Período de Postagem (DD/MM/YYYY):**")
c1, c2 = st.columns(2)
d_ini = c1.date_input("De:", value=date.today() - timedelta(days=3), format="DD/MM/YYYY")
d_fim = c2.date_input("Até:", value=date.today(), format="DD/MM/YYYY")

dork = Dork.construir(t_titulo, t_obrigatorios, t_regime, t_exclusoes)
url = Dork.google_url(dork, d_ini, d_fim)

# Dork gerado
st.markdown("---")
container_topo = st.container()
container_topo.subheader("📋 Preview")

container_topo.markdown("**Comando Dork (Legível):**")
container_topo.code(dork, language="text")

container_topo.markdown("**URL Final (Link Técnico):**")
container_topo.code(url, language="text")

st.markdown("---")
b1, b2 = st.columns([2, 2])
b1.link_button("PESQUISAR NO GOOGLE 🚀", url, use_container_width=True)
if b2.button("LIMPAR 🗑️", use_container_width=True):
    SystemTools.reset_app()