import argparse
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=60)
    parser.add_argument("--delay", type=float, default=1.0)
    args = parser.parse_args()

    print("Training simulation started", flush=True)

    for step in range(1, args.steps + 1):
        loss = 1 / step
        print(
            f"epoch {step:03d} loss: {loss:.4f}",
            flush=True,
        )
        time.sleep(args.delay)

    print("Training simulation completed", flush=True)


if __name__ == "__main__":
    main()
