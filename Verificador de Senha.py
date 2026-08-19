"""
Verificador de Força de Senha

Este script analisa uma senha digitada pelo usuário e avalia
o quão forte ela é, com base em critérios comuns de segurança.
"""

import re


def verificar_forca_senha(senha):
    pontos = 0
    feedback = []

    # Critério 1: comprimento mínimo
    if len(senha) >= 8:
        pontos += 1
    else:
        feedback.append("❌ A senha deveria ter pelo menos 8 caracteres.")

    # Critério 2: letra maiúscula
    if re.search(r'[A-Z]', senha):
        pontos += 1
    else:
        feedback.append("❌ Adicione pelo menos uma letra maiúscula.")

    # Critério 3: letra minúscula
    if re.search(r'[a-z]', senha):
        pontos += 1
    else:
        feedback.append("❌ Adicione pelo menos uma letra minúscula.")

    # Critério 4: número
    if re.search(r'[0-9]', senha):
        pontos += 1
    else:
        feedback.append("❌ Adicione pelo menos um número.")

    # Critério 5: caractere especial
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        pontos += 1
    else:
        feedback.append("❌ Adicione pelo menos um caractere especial (ex: !@#$%).")

    # Classificação final
    if pontos <= 2:
        classificacao = "FRACA 🔴"
    elif pontos <= 4:
        classificacao = "MÉDIA 🟡"
    else:
        classificacao = "FORTE 🟢"

    return classificacao, pontos, feedback


def main():
    print("=== Verificador de Força de Senha ===\n")
    senha = input("Digite uma senha para analisar: ")

    classificacao, pontos, feedback = verificar_forca_senha(senha)

    print(f"\nClassificação: {classificacao} ({pontos}/5 critérios atendidos)")

    if feedback:
        print("\nSugestões de melhoria:")
        for dica in feedback:
            print(f"  {dica}")
    else:
        print("\n✅ Excelente! Sua senha atende a todos os critérios de segurança.")


if __name__ == "__main__":
    main()
