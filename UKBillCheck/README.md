# UKBillCheck

UKBillCheck helps UK households independently recalculate a domestic electricity or gas bill from the readings and tariff printed on it.

It checks:

- electricity usage directly from meter readings;
- metric or imperial gas volume converted to kWh;
- usage charges and daily standing charges;
- VAT-inclusive totals;
- reported subtotal and total mismatches;
- bills based on estimated or mixed readings.

No current price cap is hardcoded because tariffs and regional rates change. Enter the rates printed on the bill you are checking.

The deterministic calculation works without credentials. With OPENAI_API_KEY, the agent can explain sanitized calculations and next steps. Names, addresses, account numbers, and full bill documents are not required or sent.

## Setup

~~~bash
cd UKBillCheck
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only for optional AI explanations. Never commit .env.

## Input

Use JSON containing the billing period, opening and closing readings, reading type, unit rate, standing charge, and VAT rate. Gas bills may also provide volume_unit, correction_factor, and calorific_value. The end date is treated as exclusive when counting standing-charge days.

See example_bill.json for a reconciled electricity bill.

## Usage

~~~bash
python cli.py example_bill.json --no-model
python cli.py my_bill.json --tolerance 0.10
~~~

The CLI prints JSON and exits with 0 when the supplied figures reconcile, 2 for findings, or an argparse error for invalid input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Important limits

UKBillCheck is an independent arithmetic aid, not legal, financial, or energy advice. Supplier bills may contain discounts, debt recovery, multiple tariff periods, or other line items not represented by the simple input. Confirm disputes with the supplier and use official consumer-support channels where appropriate.
