import random
import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Jokempô - Você vs Computador", page_icon="🤖", layout="centered"
)

# --- Cabeçalho ---
st.title("🎮 Jogo Pedra, Papel e Tesoura")
st.markdown(
    "### Desafie o Computador: faça sua escolha e veja quem leva a melhor!"
)
st.write("-" * 50)

# Opções válidas do jogo
opcoes_validas = ("pedra", "papel", "tesoura")

# --- Coleta da Jogada do Usuário ---
st.markdown("#### **Sua vez (Jogador 1):**")
jogador_escolha = st.selectbox(
    "Escolha sua opção:", ["Selecione..."] + list(opcoes_validas)
)

st.write("-" * 50)

# --- Botão para Executar a Lógica do Jogo ---
if st.button("🕹️ Realizar Disputa"):
  if jogador_escolha == "Selecione...":
    st.warning("⚠️ Por favor, selecione uma opção antes de jogar!")
  else:
    # Tratamento da escolha do jogador
    j1 = jogador_escolha.lower().strip()

    # O Computador escolhe de forma aleatória
    j2 = random.choice(opcoes_validas)

    # Mostrando as jogadas lado a lado
    col1, col2 = st.columns(2)
    with col1:
      st.info(f"**Você:** {j1.capitalize()}")
    with col2:
      st.info(f"**Computador:** {j2.capitalize()}")

    st.write("")

    # --- Lógica do Jogo e Resultado ---
    if j1 == j2:
      st.warning(f"🤝 **Resultado:** Empate! Ambos escolheram {j1}.")
    elif (
        (j1 == "pedra" and j2 == "tesoura")
        or (j1 == "tesoura" and j2 == "papel")
        or (j1 == "papel" and j2 == "pedra")
    ):
      st.success(f"🎉 **Resultado:** Você venceu! ({j1} ganha de {j2})")
      st.balloons()  # Chuva de balões para comemorar sua vitória!
    else:
      st.error(f"🤖 **Resultado:** O Computador venceu! ({j2} ganha de {j1})")

st.markdown("---")
st.caption(
    "Desenvolvido por Tonjr | Fundamentos de Linguagem Python para Ciência de"
    " Dados"
)