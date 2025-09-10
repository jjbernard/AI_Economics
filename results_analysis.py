import polars as pl

if __name__ == "__main__":
    # Scan CSV file
    df = pl.scan_csv("test_results.csv", has_header=True, separator=";")

    # Build the result table in multiple steps
    result = df.group_by("model").agg(pl.col("tokens").mean()).rename({"tokens": "mean"})
    result = result.join(df.group_by("model").agg(pl.col("tokens").max()).rename({"tokens": "max"}), on="model")
    result = result.join(df.group_by("model").agg(pl.col("tokens").min()).rename({"tokens": "min"}), on="model")

    # output to a new CSV
    result.sink_csv("table.csv")
