import time

from vllm import LLM, SamplingParams
from typing import List


class ChatTask(object):
    def __init__(self):
        start = time.time()
        self.llm = LLM(model="facebook/opt-125m")
        print("INIT, cost=%.2fs" % (time.time() - start))

    def execute(self, messages: List, tqdm: bool = False):
        start = time.time()
        sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
        print("Params, cost=%.2fs" % (time.time() - start))
        start = time.time()
        outputs = self.llm.chat(messages=messages, sampling_params=sampling_params, use_tqdm=tqdm,
                                chat_template="string")
        print("Gen, cost=%.2fs" % (time.time() - start))

        for output in outputs:
            print("PROMPT=", output.prompt)
            for item in output.outputs:
                print(item.text)
