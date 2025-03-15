import time

from vllm import LLM, SamplingParams
from typing import List


class GenerateTask(object):
    def __init__(self):
        start = time.time()
        self.llm = LLM(model="facebook/opt-125m")
        print("INIT, cost=%.2fs" % (time.time() - start))

    def execute(self, prompts: List[str]):
        start = time.time()
        sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
        print("Params, cost=%.2fs" % (time.time() - start))
        start = time.time()
        outputs = self.llm.generate(prompts=prompts, sampling_params=sampling_params)
        print("Gen, cost=%.2fs" % (time.time() - start))

        for output in outputs:
            print("PROMPT=", output.prompt)
            for item in output.outputs:
                print(item.text)
