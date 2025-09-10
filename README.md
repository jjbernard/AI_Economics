# AI Economics
These simple pieces of code are here to illustrate the AI Economics article.

## How to use
You need [`uv`](https://docs.astral.sh/uv/) for this to work:
- `uv install`
- and to run the code: `uv run python ./token_counts.py > results.txt`.
This will create a CSV file that can be used for further analysis with the `results_analysis.py` Python file (you can run it with `uv` again).

Obviously you need API keys for OpenAI, Anthropic and MistralAI for the code to work. See the names of the environment variables in the code. 

## Results
Two files hold the results:
- `table.txt` provides the number of output for each model with their mean, max and min numbers.
- `results.txt` provides the detailed output for each model and each run (there are 30 runs per model)
