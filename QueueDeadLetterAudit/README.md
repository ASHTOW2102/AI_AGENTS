# QueueDeadLetterAudit

Reviews dead-letter queue controls: delivery-attempt limits, retention against replay needs, backlog age, and reviewed redrive. Supply queue-policy and aggregate metric fields as a dictionary to `audit()`; it returns severity/issue findings and runs offline.
