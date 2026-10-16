"""Reusable KPI functions for the Love's customer segmentation portfolio project."""

from pathlib import Path
import pandas as pd


EXPECTED_FILES = {
    "driver_lookup": ["DRIVER_LOOKUP.csv", "DRIVER_LOOKUP-Afnan_Rafid.csv"],
    "driver_aggs": ["DRIVER_3_YEAR_AGGS.csv", "DRIVER_3_YEAR_AGGS-Afnan_Rafid.csv"],
    "campaigns": ["DRIVER_MONTHLY_CAMPAIGNS.csv", "DRIVER_MONTHLY_CAMPAIGNS (1).csv"],
    "product_sales": ["DRIVER_MONTHLY_PRODUCT_SALES.csv"],
    "store_lookup": ["STORE_LOOKUP.csv"],
}


def find_file(data_dir: Path, names):
    for name in names:
        path = data_dir / name
        if path.exists():
            return path
    raise FileNotFoundError(f"Missing expected data file. Tried: {names}")


def load_data(data_dir="data"):
    data_dir = Path(data_dir)
    return {
        key: pd.read_csv(find_file(data_dir, names))
        for key, names in EXPECTED_FILES.items()
    }


def validate_data(data):
    lookup = data["driver_lookup"]
    aggs = data["driver_aggs"]
    campaigns = data["campaigns"]
    product_sales = data["product_sales"]
    stores = data["store_lookup"]

    return {
        "unique_drivers_lookup": lookup["DRIVER_ID"].nunique(),
        "unique_drivers_aggs": aggs["DRIVER_ID"].nunique(),
        "unique_drivers_campaigns": campaigns["DRIVER_ID"].nunique(),
        "unique_drivers_product_sales": product_sales["DRIVER_ID"].nunique(),
        "driver_id_sets_match": set(lookup["DRIVER_ID"]) == set(aggs["DRIVER_ID"]),
        "campaign_ids_missing_from_lookup": len(
            set(campaigns["DRIVER_ID"]) - set(lookup["DRIVER_ID"])
        ),
        "product_ids_missing_from_lookup": len(
            set(product_sales["DRIVER_ID"]) - set(lookup["DRIVER_ID"])
        ),
        "most_visited_store_matches": int(
            lookup["MOSTVISITEDSTORE"].isin(stores["STORE_CODE"]).sum()
        ),
    }


def segment_kpis(campaigns, driver_lookup):
    df = campaigns.merge(
        driver_lookup[["DRIVER_ID", "SEGMENTGROUP"]],
        on="DRIVER_ID",
        how="left",
    )

    out = df.groupby("SEGMENTGROUP").agg(
        valid_campaigns=("JOINED", "count"),
        joined=("JOINED", "sum"),
        achieved=("ACHIEVE", "sum"),
        avg_campaign_cost=("CAMPAIGN_COST", "mean"),
        avg_fuel_gallons=("CAMPAIGNMONTHFUELGALLONS", "mean"),
        avg_merch_sales=("CAMPAIGNMONTHMERCHSALES", "mean"),
        avg_visits=("CAMPAIGNMONTHVISITS", "mean"),
    )

    out["join_rate"] = out["joined"] / out["valid_campaigns"]
    out["achieve_rate"] = out["achieved"] / out["joined"]
    return out


def historical_campaign_summary(campaigns):
    return campaigns.groupby("AGGNAME").agg(
        total_rewards=("REWARD", "sum"),
        goals_achieved=("ACHIEVE", "sum"),
        total_cost=("CAMPAIGN_COST", "sum"),
        participant_records=("DRIVER_ID", "size"),
    )


def channel_success(campaigns, driver_lookup):
    df = campaigns.merge(
        driver_lookup[["DRIVER_ID", "SEGMENTGROUP"]],
        on="DRIVER_ID",
        how="left",
    )
    df = df[df["JOINED"].notna()].copy()

    out = df.groupby("SEND_CHANNEL").agg(
        joined=("JOINED", "sum"),
        achieved=("ACHIEVE", "sum"),
    )
    out["success_rate"] = out["achieved"] / out["joined"]
    return out


if __name__ == "__main__":
    data = load_data()
    print("Validation")
    print(pd.Series(validate_data(data)))
    print("\nSegment KPIs")
    print(segment_kpis(data["campaigns"], data["driver_lookup"]).round(4))
