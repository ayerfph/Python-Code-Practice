
from airflow.sdk import dag, task

@dag
def explore_pipeline():

    @task
    def extract():
        return [{"id": 1, "name": "alice"}, {"id": 2, "name": "bob"}]

    @task
    def transform(raw_data):
        return [{"id": r["id"], "name": r["name"].upper()} for r in raw_data]

    @task
    def load(records):
        print(f"Loaded {len(records)} records")

    raw = extract()
    cleaned = transform(raw)
    load(cleaned)

explore_pipeline()
