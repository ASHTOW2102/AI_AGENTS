# EmailDeliverabilityAudit

Checks supplied SPF, DKIM, and DMARC validation results, enforcement policy, and bounce-rate metrics. It does not query DNS or send email; pass a domain status record to `audit()`.
