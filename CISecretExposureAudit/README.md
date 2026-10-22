# CISecretExposureAudit

Flags risky CI workflow conditions such as secrets on untrusted forks, privileged PR jobs running checkout code, secret logging, and static credentials. Supply workflow metadata to `audit()`; it does not inspect or expose secret values.
