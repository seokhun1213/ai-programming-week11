from pathlib import Path

import pandas as pd


def 정제(df):
    result = df.copy()

    result = result.dropna(subset=["점수"])
    print(f"점수 결측 제거 후: {len(result)}행")

    result = result.drop_duplicates()
    print(f"중복 제거 후: {len(result)}행")

    result["반"] = result["반"].str.strip()
    result["과목"] = result["과목"].str.strip()
    print(f"공백 제거 후: {len(result)}행")

    valid_score = result["점수"].between(0, 100) & (result["점수"] % 1 == 0)
    result = result[valid_score]
    result["점수"] = result["점수"].astype(int)
    print(f"점수 범위 확인 후: {len(result)}행")

    return result

def 반별평균(df):
    통계표 = df.groupby("반")["점수"].agg(
        개수="count",
        평균="mean",
        중앙값="median",
        최댓값="max"
    ).round(2)

    print(통계표)
    return 통계표["평균"]


if __name__ == "__main__":
    HERE = Path(__file__).parent
    정제된_df = 정제(pd.read_csv(HERE / "scores_2026.csv"))

    # ① 필터링
    수학_df = 정제된_df[정제된_df["과목"] == "수학"]
    print(len(수학_df))

    # ② 그룹화
    반별평균_결과 = 정제된_df.groupby("반")["점수"].mean()
    과목반별평균 = 정제된_df.groupby(["과목", "반"])["점수"].mean()
    print(반별평균_결과)
    print(과목반별평균)

    # ③ 통계
    반별평균(정제된_df)
