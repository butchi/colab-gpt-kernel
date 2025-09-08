from gpt_magic import register_gpt_magic
register_gpt_magic()
print(
    "✅ GPTマジック（%%gpt）を登録しました。"
    "セルの1行目に %%gpt 、2行目以降にメッセージを入れてShift + Enterを押してください。"
    "また、最初にAPIキーをシークレットの openaiApiKey にセットしてください。"
)
