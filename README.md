# 🏥 BRADESCO SAÚDE em Dia

Assistente Preventivo com Inteligência Artificial voltado à redução de sinistralidade em planos de saúde corporativos.

Projeto desenvolvido no contexto do Bootcamp GenAI e Dados (DIO + Bradesco), com aplicação prática em Saúde Corporativa.

---

## 🎯 Propósito Estratégico

A sinistralidade é um dos principais indicadores de sustentabilidade em planos de saúde empresariais.

O **BRADESCO SAÚDE em Dia** propõe um modelo simples de monitoramento preventivo baseado em IA, capaz de identificar sinais iniciais de risco comportamental antes da ocorrência de eventos assistenciais de maior custo.

A lógica é preventiva:
monitorar → identificar padrão → classificar risco → orientar → reduzir impacto futuro.

---

## 💡 Conceito da Solução

O sistema coleta indicadores básicos de saúde física e emocional:

- Humor (escala 1–5)
- Horas de sono
- Nível de estresse
- Prática de atividade física
- Peso

Esses dados são processados automaticamente para gerar um **Score de Saúde**, que classifica o usuário em:

- 🟢 Baixo risco
- 🟡 Risco moderado
- 🔴 Alto risco

A partir da classificação, o sistema gera orientação automática em texto e áudio.

---

## 🧠 Tecnologias Utilizadas

- Python
- openai-whisper (Speech-to-Text)
- transformers (google/flan-t5-base)
- gTTS (Text-to-Speech)
- Google Colab

---

## ⚙️ Funcionamento Técnico

1. O usuário responde via texto ou voz.
2. O áudio é transcrito com Whisper.
3. Um modelo NLP interpreta e estrutura os dados.
4. Um algoritmo calcula o Score Preventivo.
5. O sistema classifica o nível de risco.
6. Uma mensagem orientativa é gerada automaticamente em áudio.

---

## 📊 Aplicação em Saúde Corporativa

Este protótipo demonstra como a IA pode apoiar:

- Programas de prevenção empresarial
- Monitoramento leve e contínuo de bem-estar
- Identificação precoce de padrões de risco
- Estratégias de redução de sinistralidade
- Cultura de cuidado preventivo

O modelo pode evoluir para integração com dashboards populacionais e análises preditivas.

---

## 📌 Exemplo de Resultado

Score: 8  
Classificação: Baixo risco  
Mensagem: Parabéns! Continue mantendo sua rotina saudável.

---

## 👩‍💻 Desenvolvido por

Juliane Nascimento  
Estagiária – Bradesco Saúde  
Bootcamp GenAI e Dados – DIO

---

⚠️ Projeto acadêmico e demonstrativo.

