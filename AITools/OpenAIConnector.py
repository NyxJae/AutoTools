import requests
import time
from requests.adapters import HTTPAdapter, Retry

class OpenAIConnection:
    def __init__(self, apikey, base_url, model_name):
        """
        初始化 OpenAIConnection
        :param apikey: API 密钥
        :param base_url: API 基础 URL
        :param model_name: 模型名称
        """
        self.apikey = apikey
        self.base_url = base_url
        self.model_name = model_name
        
        # 配置重试策略
        self.session = requests.Session()
        retries = Retry(
            total=5,  # 最大重试次数
            backoff_factor=1,  # 重试间隔时间
            status_forcelist=[500, 502, 503, 504],  # 需要重试的HTTP状态码
        )
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def _send_request(self, messages):
        """
        发送请求到 OpenAI API
        :param messages: 聊天消息
        :return: 回复内容或错误信息
        """
        print(f"\n[正在调用API] 发送请求到OpenAI...")
        
        max_attempts = 3
        current_attempt = 1
        
        while current_attempt <= max_attempts:
            try:
                start_time = time.time()
                
                headers = {
                    "Authorization": f"Bearer {self.apikey}",
                    "Content-Type": "application/json"
                }
                data = {
                    "model": self.model_name,
                    "messages": messages
                }
                
                response = self.session.post(
                    f"{self.base_url}/chat/completions",
                    headers=headers,
                    json=data,
                    timeout=60  # 设置60秒超时
                )
                response.raise_for_status()
                result = response.json()['choices'][0]['message']['content']
                
                end_time = time.time()
                print(f"[API调用成功] 耗时: {end_time - start_time:.2f}秒")
                return result
                
            except requests.exceptions.RequestException as e:
                if current_attempt < max_attempts:
                    wait_time = current_attempt * 2  # 递增等待时间
                    print(f"[API调用失败] 第{current_attempt}次尝试失败: {str(e)}")
                    print(f"[重试] 等待{wait_time}秒后重试...")
                    time.sleep(wait_time)
                    current_attempt += 1
                else:
                    print(f"[API调用失败] 已达到最大重试次数({max_attempts}次)")
                    return f"Error: 接口调用失败，请检查网络连接或API配置。详细错误: {str(e)}"

    def test_function(self):
        """
        测试连接
        :return: 回复内容或错误信息
        """
        print("[测试连接] 正在测试与OpenAI的连接...")
        messages = [{"role": "user", "content": "hi"}]
        return self._send_request(messages)

    def generate_document(self, code, prompt):
        """
        生成文档
        :param code: 代码示例
        :param prompt: 提示信息
        :return: 文档内容或错误信息
        """
        print("[生成文档] 正在分析代码并生成文档...")
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": code}
        ]
        return self._send_request(messages)

if __name__ == "__main__":
    # 初始化并测试
    print("\n=== OpenAI API连接测试 ===")
    
    apikey = "sk-5WVwOmZqjuuhXiQZ5d4c8c1e1dB24fF4B59630C66fB91cFe"
    base_url = "https://35fast.aigcbest.top/v1"
    model_name = "gpt-4o-2024-08-06"
    
    print(f"API基础URL: {base_url}")
    print(f"模型名称: {model_name}")
    
    openai_connection = OpenAIConnection(apikey, base_url, model_name)
    reply = openai_connection.test_function()
    
    print("\n测试结果:", reply)
    print("\n=== 测试完成 ===")
