from typing import List

from app.chat_task import ChatTask
from app.generate_task import GenerateTask

if __name__ == '__main__':
    task: GenerateTask = GenerateTask()
    prompts: List[str] = ["Hello, my name is"]
    task.execute(prompts)

    task: ChatTask = ChatTask()
    messages: List = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
        {"role": "user", "content": "Write an essay about the importance of higher education."}
    ]
    task.execute(messages=messages)
