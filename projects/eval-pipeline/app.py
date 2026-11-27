"""EvalGate interactive demo for Hugging Face Spaces."""

from demo import run_pipeline


def evaluate(scores: str) -> dict:
    try:
        values = [float(value) for value in scores.split(",")] if scores.strip() else []
    except ValueError:
        return {"error": "Enter comma-separated numbers."}
    try:
        return run_pipeline(values)
    except ValueError as error:
        return {"error": str(error)}


if __name__ == "__main__":
    import gradio as gr

    gr.Interface(
        fn=evaluate,
        inputs=gr.Textbox(label="Candidate scores"),
        outputs=gr.JSON(label="Gate result"),
        examples=[["0.90, 0.91, 0.89"], ["0.70, 0.72"], ["0.9, 1.2"]],
        title="EvalGate",
        description="Compare candidate scores from 0 to 1 with a fixed baseline.",
    ).launch()
