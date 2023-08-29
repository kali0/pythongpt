import os
import openai
import streamlit as st

# Configurações
openai.api_key = "process.env.OPENAI_API_KEY"

def coleta_input():
  input_text = st.text_input("Faça uma pergunta:", "")
  return input_text

def obtém_resposta(prompt):
  response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
  )

  return response.choices[0].text

def exibe_resposta(resposta):
  st.markdown(resposta)

def main():
  
  st.title("Meu App com OpenAI")

  prompt = coleta_input()

  if st.button("Obter Resposta"):
    try:
      resposta = obtém_resposta(prompt)
      exibe_resposta(resposta)
  
    except Exception as e:
      st.error("Erro ao consultar OpenAI:")
      st.error(e)

if __name__ == "__main__":
  main()