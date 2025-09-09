# AI Economics
These simple pieces of code are here to illustrate the AI Economics article.

## How to use
You need [`uv`](https://docs.astral.sh/uv/) to run the code: `uv run python ./token_counts.py > results.txt`. This will create a CSV file that can be used for further analysis with the `results_analysis.py` Python file. 


## Results
Two files hold the results:
- `table.txt` provides the number of output for each model with their mean, max and min numbers. 
- `results.txt` provides the detailed output for each model and each run (there are 30 runs per model)
