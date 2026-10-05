import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Jokempô - 2 Jogadores", page_icon="🎮", layout="centered"
)

# --- Cabeçalho ---
st.title("🎮 Jogo Pedra, Papel e Tesoura")
st.markdown(
    "### Desafie um amigo: cada jogador escolhe uma opção e o sistema decide"
    " quem vence!"
)
st.write("-" * 50)

# Opções válidas do jogo
opcoes_validas = ("pedra", "papel", "tesoura")

# --- Coleta dos Dados de Entrada (Direto na Tela Principal) ---
# Dividimos a tela em duas colunas para o Jogador 1 e Jogador 2 ficarem lado a lado
col1, col2 = st.columns(2)

with col1:
  st.markdown("#### **Jogador 1**")
  jogador1_escolha = st.selectbox(
      "Escolha a jogada do Jogador 1",
      ["Selecione..."] + list(opcoes_validas),
      key="j1",
  )

with col2:
  st.markdown("#### **Jogador 2**")
  jogador2_escolha = st.selectbox(
      "Escolha a jogada do Jogador 2",
      ["Selecione..."] + list(opcoes_validas),
      key="j2",
  )

st.write("-" * 50)

# --- Botão para Executar a Lógica do Jogo ---
if st.button("🕹️ Realizar Disputa"):
  # Validação se as opções foram escolhidas
  if jogador1_escolha == "Selecione..." or jogador2_escolha == "Selecione...":
    st.warning("⚠️ Por favor, ambos os jogadores devem escolher uma opção!")
  else:
    # Tratamento de dados (garantindo minúsculas)
    j1 = jogador1_escolha.lower().strip()
    j2 = jogador2_escolha.lower().strip()

    # --- Lógica do Jogo e Resultado ---
    if j1 == j2:
      st.warning(f"🤝 **Resultado:** Empate! Ambos escolheram {j1}.")
    elif (
        (j1 == "pedra" and j2 == "tesoura")
        or (j1 == "tesoura" and j2 == "papel")
        or (j1 == "papel" and j2 == "pedra")
    ):
      st.success(
          f"🎉 **Resultado:** Jogador 1 venceu ({j1} vence {j2})! Parabéns!"
      )
      st.balloons()  # Efeito especial de comemoração!
    else:
      st.success(
          f"🏆 **Resultado:** Jogador 2 venceu ({j2} vence {j1})! Parabéns!"
      )
      st.balloons()

st.markdown("---")
st.caption(
    "Desenvolvido por Tonjr | Fundamentos de Linguagem Python para Ciência de"
    " Dados"
)