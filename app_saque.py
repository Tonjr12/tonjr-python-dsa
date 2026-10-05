import streamlit as st

st.title("🧮 Simulador de Caixa Eletrônico")
st.write(
    "Digite o valor que deseja sacar e o sistema calculará as cédulas"
    " automaticamente."
)

# Caixinha de número na tela (substitui o input)
saque = st.number_input("Digite o valor do saque (R$):", min_value=1, step=1)

# Botão para o usuário clicar
if st.button("Realizar Saque"):
    total = saque
    ced = 50
    tot_ced = 0

    st.write("---")
    st.subheader("Cédulas entregues:")

    # Lógica do cálculo das notas
    while total > 0:
        if total >= ced:
            tot_ced = total // ced
            total %= ced
            st.success(f"{tot_ced} cédula(s) de R$ {ced}")

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
