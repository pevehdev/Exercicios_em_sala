{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNUU0PrT5WhA5LswyYw1JfH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/pevehdev/Exercicios_em_sala/blob/main/Exercicio_em_Sala_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:\n",
        "O modelo do carro mais econômico;\n",
        "Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa"
      ],
      "metadata": {
        "id": "5Ic43Ol9wVVq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Lista aninhada com cada modelo de carro com quilometros por litro, ou seja a cada 1KM o carro Buggati consome 49 Litros\n",
        "\n",
        "carros = [\n",
        "    ['Koenigsegg_Jesko_Absolut', 53],\n",
        "    ['Hennessey_Venom_F5', 50],\n",
        "    ['Bugatti', 49] ,\n",
        "    ['Koenigsegg', 48] ,\n",
        "    ['Tuatara', 46 ]\n",
        "    ]\n",
        "preco_combustivel = 2.25\n",
        "\n",
        "def calcular_custo(modelo, consumo):\n",
        "    litros_consumidos = 1000 / consumo\n",
        "    custo = litros_consumidos * preco_combustivel\n",
        "    return litros_consumidos, custo\n",
        "\n",
        "# A variável abaixo percorre toda a sublista de carros, como temos duas posições, passamos no parametro x a posição que será feito a verificação de menor, pois\n",
        "# posição [0] é o modelo, que não faria sentido em termos de comparação de menor valor pois é uma string. O [0] fora do parenteses da função min, é para exibir para o usuario\n",
        "# o modelo do carro.\n",
        "modelo_mais_economico = min(carros, key=lambda x: x[1])[0]\n",
        "print(\"Modelo mais econômico:\", modelo_mais_economico)\n",
        "\n",
        "for carro in carros:\n",
        "    modelo = carro[0]\n",
        "    consumo = carro[1]\n",
        "litros, custo = calcular_custo(modelo, consumo)\n",
        "print(f\"{modelo} consome: {litros:.2f} litros percorrendo 1000km, custando R$ {custo:.2f}\")\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KYqbCHKhwXWq",
        "outputId": "0059625b-1e94-4c15-b323-4bbfe1705463"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Modelo mais econômico: Tuatara\n",
            "Tuatara consome: 21.74 litros, custando R$ 48.91\n"
          ]
        }
      ]
    }
  ]
}