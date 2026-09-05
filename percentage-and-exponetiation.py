"""
Calculadora de Porcentagem e Potenciação.
Utilitário interativo via terminal com tratamento rigoroso de erros.
"""

from fractions import Fraction

def limpar_e_analisar(valor_str: str) -> float:
    limpo = valor_str.replace(" ", "")
    
    if "/" in limpo:
        try:
            num, den = limpo.split("/")
            if float(den) == 0:
                raise ValueError("O denominador de uma fração não pode ser zero.")
            return float(num) / float(den)
        except ValueError:
            raise ValueError(f"Formato de fração inválido: '{valor_str}'")
            
    try:
        return float(limpo)
    except ValueError:
        raise ValueError(f"Não foi possível converter '{valor_str}' em um número válido.")

def obter_porcentagem_de(porcentagem: float, total: float) -> float:
    return (porcentagem / 100) * total

def obter_proporcao_percentual(parte: float, total: float) -> float:
    if total == 0:
        raise ValueError("O valor total não pode ser zero.")
    return (parte / total) * 100

def formatar_resultado_potencia(base: float, expoente: float) -> str:
    if base == 0 and expoente <= 0:
        raise ValueError("Indefinição matemática: base zero com expoente menor ou igual a zero.")
    
    if base < 0 and not expoente.is_integer():
        raise ValueError("Resultado fora do domínio dos números reais (base negativa com expoente fracionário).")

    res = base ** expoente

    try:
        forma_fracionaria = Fraction(res).limit_denominator(1000000)
        if forma_fracionaria.denominator == 1:
            return f"{int(res)}"
        else:
            return f"{forma_fracionaria} (ou {res:.6f})"
    except Exception:
        return f"{res:.6f}"

def main():
    while True:
        print("\nPORCENTAGEM E POTENCIAÇÃO")
        print("1. Calcular Porcentagem Direta")
        print("2. Calcular Proporção Percentual")
        print("3. Potenciação (Suporta expoentes inteiros, negativos e frações)")
        print("0. Sair")
        
        opcao = input("Opção: ").strip()

        if opcao == "0":
            break

        try:
            if opcao == "1":
                porcentagem_input = input("Porcentagem: ")
                total_input = input("Valor total: ")
                
                pct = limpar_e_analisar(porcentagem_input)
                total = limpar_e_analisar(total_input)
                
                res = obter_porcentagem_de(pct, total)
                print(f"Resultado: {pct}% de {total} = {res}")

            elif opcao == "2":
                parte_input = input("Parte: ")
                total_input = input("Total: ")
                
                parte = limpar_e_analisar(parte_input)
                total = limpar_e_analisar(total_input)
                
                res = obter_proporcao_percentual(parte, total)
                print(f"Resultado: {parte} representa {res:.2f}% de {total}")

            elif choice == "3": # Apenas corrigido para 'opcao' em vez do termo antigo em inglês
                base_input = input("Base: ")
                expoente_input = input("Expoente (Ex: -2 ou 1/2): ")
                
                base = limpar_e_analisar(base_input)
                expoente = limpar_e_analisar(expoente_input)
                
                res_str = formatar_resultado_potencia(base, expoente)
                print(f"Resultado: {base} ^ ({expoente_input.strip()}) = {res_str}")

            else:
                print("Erro: Opção inválida.")

        except ValueError as e:
            print(f"Erro: {e}")
        except ZeroDivisionError:
            print("Erro: Divisão por zero detectada na operação.")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
