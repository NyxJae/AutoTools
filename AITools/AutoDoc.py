from .OpenAIConnector import OpenAIConnection

# 初始化并测试
apikey = "sk-5WVwOmZqjuuhXiQZ5d4c8c1e1dB24fF4B59630C66fB91cFe"
base_url = "https://35fast.aigcbest.top/v1"
model_name = "gpt-4o-2024-08-06"

openai_connection = OpenAIConnection(apikey, base_url, model_name)
reply = openai_connection.test_function()

print("回复内容:", reply)
