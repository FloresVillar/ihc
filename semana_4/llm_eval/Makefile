.PHONY: install run run-deepseek run-gemini charts clean

install:
	pip install -r requirements.txt

# Run as a module from the parent dir so `from llm_eval import ...` resolves.
run:
	cd .. && python3 -m llm_eval.run_eval --providers deepseek gemini --clear

run-deepseek:
	cd .. && python3 -m llm_eval.run_eval --providers deepseek --clear

run-gemini:
	cd .. && python3 -m llm_eval.run_eval --providers gemini

charts:
	cd .. && python3 -c "from llm_eval import charts, metrics, storage; \
	providers = sorted(set(r['provider'] for r in storage.read_runs())); \
	charts.generate(metrics.compute_all(providers))"

clean:
	rm -rf data/runs.csv charts/*.png __pycache__
