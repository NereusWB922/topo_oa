from app.pipeline import Pipeline
from app.pipeline import Step


def test_add_step(mocker):
    step = mocker.Mock(spec=Step)

    pipeline = Pipeline().add_step(step)

    assert len(pipeline._steps) == 1
    assert pipeline._steps[0] == step


def test_execute(mocker):
    step1 = mocker.Mock(spec=Step)
    step2 = mocker.Mock(spec=Step)
    step1.execute.return_value = {"data": "step1"}
    step2.execute.return_value = {"data": "step2"}

    pipeline = Pipeline().add_step(step1).add_step(step2)
    result = pipeline.execute()

    step1.execute.assert_called_once_with({})
    step2.execute.assert_called_once_with({"data": "step1"})
    assert result == {"data": "step2"}
