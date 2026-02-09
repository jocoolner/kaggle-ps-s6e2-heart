from __future__ import annotations

from pathlib import Path
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "raw"
REPORTS_DIR = ROOT / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

TRAIN_PATH = DATA_DIR / "train.csv"
TEST_PATH = DATA_DIR / "test.csv"
SUB_PATH = DATA_DIR / "sample_submission.csv"


def missing_report(df: pd.DataFrame) -> pd.DataFrame:
    miss = df.isna().mean().sort_values(ascending=False)
    out = pd.DataFrame({"missing_pct": (miss * 100).round(3)})
    return out


def main() -> None:
    train = pd.read_csv(TRAIN_PATH)
    test = pd.read_csv(TEST_PATH)
    sub = pd.read_csv(SUB_PATH)

    # Detect id/target from sample submission
    id_col = sub.columns[0]
    target_col = sub.columns[1]

    lines: list[str] = []
    lines.append("=== Kaggle PS S6E2 — Sanity Check Report ===")
    lines.append(f"Train shape: {train.shape}")
    lines.append(f"Test  shape: {test.shape}")
    lines.append(f"Sample submission shape: {sub.shape}")
    lines.append("")
    lines.append(f"Detected id_col: {id_col}")
    lines.append(f"Detected target_col: {target_col}")
    lines.append("")

    # Basic checks
    lines.append("Train columns:")
    lines.append(", ".join(train.columns.tolist()))
    lines.append("")
    lines.append("Dtypes (train):")
    lines.append(train.dtypes.astype(str).to_string())
    lines.append("")

    if target_col in train.columns:
        vc = train[target_col].value_counts(dropna=False)
        lines.append("Target distribution (counts):")
        lines.append(vc.to_string())
        lines.append("")
        lines.append("Target distribution (percent):")
        lines.append((vc / len(train) * 100).round(3).to_string())
        lines.append("")
    else:
        lines.append(f"WARNING: target_col '{target_col}' not found in train!")
        lines.append("")

    if id_col in train.columns:
        dup_ids = train[id_col].duplicated().sum()
        lines.append(f"Duplicated IDs in train: {dup_ids}")
        lines.append("")
    else:
        lines.append(f"WARNING: id_col '{id_col}' not found in train!")
        lines.append("")

    # Missingness reports
    miss_train = missing_report(train)
    miss_test = missing_report(test)

    miss_train.to_csv(REPORTS_DIR / "missing_train.csv", index=True)
    miss_test.to_csv(REPORTS_DIR / "missing_test.csv", index=True)

    report_path = REPORTS_DIR / "data_profile.txt"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    print("\n".join(lines))
    print("")
    print(f"Saved: {report_path}")
    print(f"Saved: {REPORTS_DIR / 'missing_train.csv'}")
    print(f"Saved: {REPORTS_DIR / 'missing_test.csv'}")


if __name__ == "__main__":
    main()
