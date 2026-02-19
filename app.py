# ==============================
# BRADESCO SAÚDE em Dia
# ==============================

# --------- Dependências ----------
# pip install openai-whisper
# pip install gTTS
# pip install transformers
# ----------------------------------

import whisper
from gtts import gTTS
from IPython.display import Audio, display, Javascript
from google.colab import output
import base64
import re

from transformers import pipeline


# ==============================
# Configuração
# ==============================

language = "pt"
modelo_whisper = whisper.load_model("small")
interpretador = pipeline("text-generation", model="google/flan-t5-base")


# ==============================
# 1. Gravação de Áudio (Colab)
# ==============================

def gravar_audio(nome_base="entrada", duracao=15):

    display(Javascript(f"""
    async function gravarAudio() {{
      const stream = await navigator.mediaDevices.getUserMedia({{ audio: true }});
      const mediaRecorder = new MediaRecorder(stream);
      const chunks = [];
      mediaRecorder.ondataavailable = e => chunks.push(e.data);
      mediaRecorder.start();
      await new Promise(resolve => setTimeout(resolve, {duracao * 1000}));
      mediaRecorder.stop();
      await new Promise(resolve => mediaRecorder.onstop = resolve);
      const blob = new Blob(chunks, {{ type: 'audio/webm' }});
      const arrayBuffer = await blob.arrayBuffer();
      const base64Audio = btoa(
        new Uint8Array(arrayBuffer)
          .reduce((data, byte) => data + String.fromCharCode(byte), '')
      );
      google.colab.kernel.invokeFunction('notebook.salvar_audio', [base64Audio], {{}});
    }}
    gravarAudio();
    """))

    def salvar_audio(base64_audio):
        audio_bytes = base64.b64decode(base64_audio)
        with open(nome_base + ".webm", "wb") as f:
            f.write(audio_bytes)

    output.register_callback('notebook.salvar_audio', salvar_audio)


# ==============================
# 2. Transcrição
# ==============================

def transcrever_audio(arquivo="entrada.webm"):
    resultado = modelo_whisper.transcribe(arquivo)
    print("📝 Transcrição:", resultado["text"])
    return resultado["text"]


# ==============================
# 3. Falar Resposta
# ==============================

def falar(texto, nome_arquivo="resposta.mp3"):
    tts = gTTS(text=texto, lang='pt')
    tts.save(nome_arquivo)
    display(Audio(nome_arquivo, autoplay=True))


# ==============================
# 4. Extração com NLP
# ==============================

def extrair_dados(texto):

    prompt = f"""
    Extraia as informações abaixo do texto e responda no formato:
    humor=?
    sono=?
    estresse=?
    atividade=?
    peso=?

    Texto: {texto}
    """

    resposta = interpretador(prompt, max_new_tokens=100)[0]["generated_text"]

    print("🔎 Interpretação IA:", resposta)

    numeros = re.findall(r'\d+', resposta)

    dados = {
        "humor": int(numeros[0]) if len(numeros) > 0 else 3,
        "sono": float(numeros[1]) if len(numeros) > 1 else 7,
        "estresse": int(numeros[2]) if len(numeros) > 2 else 3,
        "peso": float(numeros[3]) if len(numeros) > 3 else 70,
        "atividade": "sim" if "sim" in resposta.lower() else "nao"
    }

    return dados


# ==============================
# 5. Score
# ==============================

def calcular_score(dados):
    score = 0

    if dados["humor"] >= 4:
        score += 2
    if dados["sono"] >= 7:
        score += 2
    if dados["estresse"] <= 2:
        score += 2
    if dados["atividade"] == "sim":
        score += 2

    return score


# ==============================
# 6. Classificação
# ==============================

def classificar(score):
    if score >= 7:
        return "Baixo risco", "Parabéns! Continue mantendo sua rotina saudável."
    elif score >= 4:
        return "Risco moderado", "Atenção à sua rotina. Pequenos ajustes podem melhorar sua saúde."
    else:
        return "Alto risco", "Recomendamos acompanhamento médico e maior atenção à sua saúde."


# ==============================
# 7. Fluxo Principal
# ==============================

def main():

    print("🏥 BRADESCO SAÚDE em Dia")
    print("Escolha como deseja responder:")
    print("1 - Digitando")
    print("2 - Por voz")

    modo = input("Digite 1 ou 2: ")

    if modo == "1":

        dados = {
            "humor": int(input("De 1 a 5, como está seu humor? ")),
            "sono": float(input("Quantas horas dormiu? ")),
            "estresse": int(input("De 1 a 5, qual seu estresse? ")),
            "atividade": input("Fez atividade física? (sim/nao) ").lower(),
            "peso": float(input("Qual seu peso? "))
        }

    elif modo == "2":

        print("🎙 Fale: humor, horas de sono, estresse, atividade física e peso.")
        gravar_audio()

        print("🎧 Áudio gravado:")
        display(Audio("entrada.webm"))

        texto = transcrever_audio()
        dados = extrair_dados(texto)

    else:
        print("Opção inválida.")
        return

    score = calcular_score(dados)
    risco, mensagem = classificar(score)

    print("\n📊 Score:", score)
    print("Classificação:", risco)
    print("Mensagem:", mensagem)

    falar(mensagem)


if __name__ == "__main__":
    main()
