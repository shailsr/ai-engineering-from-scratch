import argparse
import tempfile
import time
from pathlib import Path

from datasets import Dataset, load_dataset


def load_mrpc():
    return load_dataset(
        "nyu-mll/glue",
        "mrpc",
        split="train",
    )


def inspect_examples(dataset):
    print("\n=== Exercise 1: Inspect MRPC ===")
    print("Rows:", len(dataset))
    print("Columns:", dataset.column_names)

    for number, example in enumerate(dataset.select(range(5)), start=1):
        label = dataset.features["label"].int2str(example["label"])
        print(f"\nExample {number}")
        print("Sentence 1:", example["sentence1"])
        print("Sentence 2:", example["sentence2"])
        print("Label:", label)


def stream_c4(seconds):
    print(f"\n=== Exercise 2: Stream C4 for {seconds} seconds ===")

    stream = load_dataset(
        "allenai/c4",
        "en",
        split="train",
        streaming=True,
    )
    iterator = iter(stream)

    first = next(iterator)
    print("First example:", first["text"][:100].replace("\n", " "))

    start = time.monotonic()
    count = 0
    characters = 0

    for example in iterator:
        count += 1
        characters += len(example["text"])

        if time.monotonic() - start >= seconds:
            break

    elapsed = time.monotonic() - start

    print(f"Elapsed: {elapsed:.2f} seconds")
    print(f"Examples: {count:,}")
    print(f"Characters: {characters:,}")
    print(f"Rate: {count / elapsed:.1f} examples/second")


def compare_formats(dataset):
    print("\n=== Exercise 3: Compare CSV and Parquet ===")

    with tempfile.TemporaryDirectory(prefix="aiefs-data-formats-") as directory:
        output_dir = Path(directory)
        csv_path = output_dir / "mrpc.csv"
        parquet_path = output_dir / "mrpc.parquet"

        dataset.to_csv(str(csv_path))
        dataset.to_parquet(str(parquet_path))

        csv_size = csv_path.stat().st_size
        parquet_size = parquet_path.stat().st_size
        reloaded = Dataset.from_parquet(str(parquet_path))

        print(f"CSV: {csv_size:,} bytes")
        print(f"Parquet: {parquet_size:,} bytes")
        print(f"Space saved: {(1 - parquet_size / csv_size):.1%}")
        print("Reloaded rows:", len(reloaded))


def create_splits(dataset):
    print("\n=== Exercise 4: Create reproducible splits ===")

    def split_once(seed):
        first = dataset.train_test_split(test_size=0.30, seed=seed)
        second = first["test"].train_test_split(test_size=0.50, seed=seed)

        return {
            "train": first["train"],
            "validation": second["train"],
            "test": second["test"],
        }

    first_run = split_once(seed=42)
    second_run = split_once(seed=42)
    total = len(dataset)

    for name, split in first_run.items():
        print(f"{name.capitalize():10}: {len(split):4} ({len(split) / total:.1%})")

    ids = {
        name: set(split["idx"])
        for name, split in first_run.items()
    }

    all_rows_preserved = sum(map(len, first_run.values())) == total
    no_overlap = (
        ids["train"].isdisjoint(ids["validation"])
        and ids["train"].isdisjoint(ids["test"])
        and ids["validation"].isdisjoint(ids["test"])
    )
    reproducible = all(
        list(first_run[name]["idx"]) == list(second_run[name]["idx"])
        for name in first_run
    )

    print("All rows preserved:", all_rows_preserved)
    print("No overlap:", no_overlap)
    print("Reproducible:", reproducible)

    if not all((all_rows_preserved, no_overlap, reproducible)):
        raise RuntimeError("Split verification failed")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stream-seconds", type=float, default=10)
    args = parser.parse_args()

    dataset = load_mrpc()
    inspect_examples(dataset)
    stream_c4(args.stream_seconds)
    compare_formats(dataset)
    create_splits(dataset)

    print("\n[PASS] All data-management exercises completed")


if __name__ == "__main__":
    main()
