from google.colab import userdata
from IPython.core.magic import register_cell_magic
from IPython.display import display, Markdown
import openai

messages = []

# Markdown形式での出力を求めるプロンプト
SYSTEM_PROMPT = (
    "You are a technical writer. Return ONLY valid GitHub-flavored Markdown.\n"
    "Inline math should be in $ $ and block math should be in $$ $$."
)

def register_gpt_magic():
    @register_cell_magic
    def gpt(line, cell):
        global messages
        
        if not messages:
            messages.append({
                "role": "system", 
                "content": SYSTEM_PROMPT
            })
        
        messages.append({"role": "user", "content": cell.strip()})
        
        key = userdata.get('openaiApiKey')
        if not key:
            print(
                "[ERROR] APIキーが設定されていません。"
                "シークレットの openaiApiKey に設定してください。"
            )
            return

        openai.api_key = key
        try:
            response = openai.chat.completions.create(
                model="gpt-5-nano",
                messages=messages,
            )
            reply = response.choices[0].message.content
            messages.append({"role": "assistant", "content": reply})
            display(Markdown(reply))
        except Exception as e:
            messages.pop()
            print(f"[ERROR] {e}")
