"""Interactive DriftWatch demo for Hugging Face Spaces."""

from demo import report_csv


def evaluate(reference: str, current: str) -> dict:
    try:
        return report_csv(reference, current)
    except ValueError as error:
        return {"error": str(error)}


if __name__ == "__main__":
    import gradio as gr

    app = gr.Interface(
        fn=evaluate,
        inputs=[
            gr.Textbox(label="Reference window", value="0,1,2,3,4"),
            gr.Textbox(label="Current window", value="0,1,2,3,4"),
        ],
        outputs=gr.JSON(label="Drift report"),
        examples=[
            ["0,1,2,3,4", "0,1,2,3,4"],
            ["0,1,2,3,4", "10,11,12,13,14"],
            ["0,0,0,0,2", "0,0,0,0,2"],
        ],
        title="DriftWatch",
        description="Compare two comma-separated feature windows with the population stability index.",
    )
    app.launch()
