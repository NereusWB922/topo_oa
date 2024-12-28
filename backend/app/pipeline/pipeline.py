from .step import Step


class Pipeline:
    def __init__(self, steps: list[Step] = []):
        self._steps = steps

    def add_step(self, step: Step) -> "Pipeline":
        new_steps = self._steps + [step]
        return Pipeline(new_steps)

    def execute(self):
        data = {}
        for step in self._steps:
            data = step.execute(data)
        return data
