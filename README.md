# 🤖 AI_AGENTS

A growing collection of practical, self-contained AI agents built with Python.

## Agent catalog

| Agent | Purpose | Runs without an API key |
|---|---|---:|
| [DocBrief](DocBrief/) | Summarizes uploaded documents | No |
| [HealthPlanner](HealthPlanner/) | Creates personalized health plans | No |
| [SpeakScore](SpeakScore/) | Transcribes and scores speaking practice | No |
| [UK Housing Agent](uk-housing-agent/) | Explains UK housing costs and guidance | Partly |
| [IncidentTriage](IncidentTriage/) | Converts incident reports into secret-safe action plans | Yes |
| [PromptShield](PromptShield/) | Detects prompt injection and unsafe tool-use requests | Yes |
| [SchemaScout](SchemaScout/) | Profiles CSV data and detects schema drift | Yes |
| [MailSift](MailSift/) | Privately triages email urgency and phishing signals | Yes |
| [PlanGraph](PlanGraph/) | Finds critical paths and dependency risks in project plans | Yes |
| [EnvDoctor](EnvDoctor/) | Audits environment configuration without exposing values | Yes |
| [OpenAPISentry](OpenAPISentry/) | Audits OpenAPI quality and authentication coverage | Yes |
| [A11yScout](A11yScout/) | Audits static HTML accessibility basics | Yes |
| [ChangeScribe](ChangeScribe/) | Generates release notes from Conventional Commits | Yes |
| [LocaleLens](LocaleLens/) | Checks translation catalogs for structural drift | Yes |
| [RetryRight](RetryRight/) | Audits HTTP retry traces for resilience and idempotency risks | Yes |
| [HookSentry](HookSentry/) | Audits webhook delivery security, replay, and ordering risks | Yes |
| [ADRGuard](ADRGuard/) | Audits architecture decision records for completeness and lifecycle hygiene | Yes |
| [CoverageCompass](CoverageCompass/) | Prioritizes risky test gaps from coverage.py JSON | Yes |
| [UKBillCheck](UKBillCheck/) | Recalculates UK household energy bills and flags mismatches | Yes |
| [MeetingPulse](MeetingPulse/) | Audits meeting participation, decisions, and action ownership | Yes |
| [BackupBeacon](BackupBeacon/) | Audits backup freshness, protection, and restore-test evidence | Yes |
| [CacheGuard](CacheGuard/) | Audits HTTP response caching for privacy and correctness risks | Yes |
| [FlagDoctor](FlagDoctor/) | Audits feature-flag ownership, expiry, rollout, and cleanup hygiene | Yes |
| [CronGuard](CronGuard/) | Audits scheduled jobs for overlap, retry, and collision risks | Yes |
| [PIIGuard](PIIGuard/) | Detects and masks likely personal data before files are shared | Yes |
| [LogSentry](LogSentry/) | Audits structured application logs for operational warning signals | Yes |
| [CookieCheck](CookieCheck/) | Audits web cookie settings for common security weaknesses | Yes |
| [QueueWatch](QueueWatch/) | Audits message queues for backlog and consumer risks | Yes |
| [SLAWatch](SLAWatch/) | Audits support tickets for SLA and ownership risks | Yes |
| [ConfigDiff](ConfigDiff/) | Finds risky drift between baseline and current configuration | Yes |
| [CertWatch](CertWatch/) | Audits TLS certificate inventory before outages occur | Yes |
| [CostPulse](CostPulse/) | Audits cloud cost snapshots for budget and tagging risks | Yes |
| [HeaderHawk](HeaderHawk/) | Audits HTTP security headers and browser protections | Yes |
| [RedirectRadar](RedirectRadar/) | Finds unsafe or inefficient HTTP redirect chains | Yes |
| [FormGuard](FormGuard/) | Audits web form definitions for privacy and security risks | Yes |
| [SecretLease](SecretLease/) | Audits secret inventories for rotation and ownership risks | Yes |
| [RetentionCheck](RetentionCheck/) | Audits data-retention rules for privacy and deletion gaps | Yes |
| [QuotaSentry](QuotaSentry/) | Audits API quotas and rate-limit configurations | Yes |
| [AccessReview](AccessReview/) | Audits user access exports for stale and excessive privileges | Yes |
| [ReleaseReady](ReleaseReady/) | Audits software releases for rollout and rollback readiness | Yes |
| [DNSGuard](DNSGuard/) | Audits DNS records for mail and domain-security gaps | Yes |
| [InvoiceAudit](InvoiceAudit/) | Recalculates invoices and flags payment-data inconsistencies | Yes |
| [ConsentLedger](ConsentLedger/) | Audits consent records for evidence and expiry gaps | Yes |
| [SessionSentry](SessionSentry/) | Audits application session policies for account risks | Yes |
| [RobotsGuard](RobotsGuard/) | Audits robots.txt rules for accidental exposure and blocking | Yes |
| [VendorWatch](VendorWatch/) | Audits third-party vendors for assurance and ownership gaps | Yes |
| [ChangeWindow](ChangeWindow/) | Audits production changes for timing and coordination risks | Yes |
| [TokenScope](TokenScope/) | Audits API token metadata for excessive permissions | Yes |
| [LicenseLens](LicenseLens/) | Audits dependency licenses for policy and attribution risks | Yes |
| [DomainExpiry](DomainExpiry/) | Audits domain portfolios for renewal and ownership risks | Yes |
| [StorageGuard](StorageGuard/) | Audits object-storage buckets for exposure and protection gaps | Yes |
| [BranchShield](BranchShield/) | Audits repository branch-protection configurations | Yes |
| [MFAWatch](MFAWatch/) | Audits account inventories for multi-factor authentication gaps | Yes |
| [RunbookReady](RunbookReady/) | Audits operational runbooks for incident readiness | Yes |
| [ImageBudget](ImageBudget/) | Audits web images for performance and accessibility budgets | Yes |
| [AlertNoise](AlertNoise/) | Audits monitoring alerts for noise and ownership risks | Yes |
| [PasswordGuard](PasswordGuard/) | Audits password policies for weak authentication controls | Yes |
| [ContainerCheck](ContainerCheck/) | Audits container settings for runtime hardening gaps | Yes |
| [FirewallLens](FirewallLens/) | Audits firewall rules for exposure and governance risks | Yes |
| [SitemapScout](SitemapScout/) | Audits sitemap entries for indexing and freshness problems | Yes |
| [MaskingAudit](MaskingAudit/) | Audits sensitive-data fields for masking coverage | Yes |
| [ServiceCatalog](ServiceCatalog/) | Audits service catalogs for ownership and lifecycle gaps | Yes |
| [HealthProbe](HealthProbe/) | Audits service health-check definitions for reliability gaps | Yes |
| [ScriptSentry](ScriptSentry/) | Audits third-party web scripts for supply-chain risks | Yes |
| [PortGuard](PortGuard/) | Audits network service inventories for exposed risky ports | Yes |
| [EncryptionAudit](EncryptionAudit/) | Audits dataset encryption policies and key governance | Yes |
| [PaginationGuard](PaginationGuard/) | Audits API pagination settings for reliability risks | Yes |
| [EnvParity](EnvParity/) | Audits deployment environments for configuration parity | Yes |
| [LinkSentinel](LinkSentinel/) | Audits website links for availability and redirect problems | Yes |
| [PinDoctor](PinDoctor/) | Audits dependency pinning and package-source hygiene | Yes |
| [OwnershipMap](OwnershipMap/) | Audits operational assets for ownership coverage | Yes |
| [StatusPageAudit](StatusPageAudit/) | Audits public status-page readiness and maintenance | Yes |
| [EmailTemplateAudit](EmailTemplateAudit/) | Audits transactional email templates for compliance gaps | Yes |
| [MobilePermission](MobilePermission/) | Audits mobile-app permission requests for privacy risks | Yes |
| [DataFreshness](DataFreshness/) | Audits datasets for freshness and pipeline ownership gaps | Yes |
| [SchemaContract](SchemaContract/) | Audits data contracts for compatibility and governance gaps | Yes |
| [MigrationGuard](MigrationGuard/) | Audits database migrations for destructive changes and rollout risks | Yes |
| [IndexAdvisor](IndexAdvisor/) | Audits database index inventories for performance risks | Yes |
| [PatchWindow](PatchWindow/) | Audits vulnerability patch plans for overdue remediation | Yes |
| [ArtifactIntegrity](ArtifactIntegrity/) | Audits build artifacts for integrity and provenance gaps | Yes |
| [ReplicationWatch](ReplicationWatch/) | Audits database replicas for lag and resilience gaps | Yes |
| [OnCallCoverage](OnCallCoverage/) | Audits on-call schedules for coverage and escalation gaps | Yes |
| [ResourceTagger](ResourceTagger/) | Audits cloud resources for cost-allocation tag gaps | Yes |
| [ModelCardAudit](ModelCardAudit/) | Audits AI model cards for transparency and risk gaps | Yes |
| [PromptVersion](PromptVersion/) | Audits production prompts for versioning and evaluation gaps | Yes |
| [CORSCompass](CORSCompass/) | Audits CORS policies for unsafe cross-origin access | Yes |
| [SBOMScout](SBOMScout/) | Audits software bills of materials for supply-chain evidence gaps | Yes |
| [TerraformPlanGuard](TerraformPlanGuard/) | Reviews Terraform plans for destructive infrastructure changes | Yes |
| [DataLineageAudit](DataLineageAudit/) | Audits dataset lineage and retention metadata | Yes |
| [IncidentTimeline](IncidentTimeline/) | Validates incident chronology, actors, and evidence | Yes |
| [DependencyFreshness](DependencyFreshness/) | Prioritises stale and lagging dependencies | Yes |
| [LLMEvidenceAudit](LLMEvidenceAudit/) | Audits generated answers for evidence and uncertainty signals | Yes |
| [CIWorkflowAudit](CIWorkflowAudit/) | Audits CI jobs for privilege and reproducibility risks | Yes |
| [DatasetFairness](DatasetFairness/) | Screens group outcome rates for material disparities | Yes |
| [APIErrorCatalog](APIErrorCatalog/) | Audits API error contracts for safety and consistency | Yes |
| [DRObjectiveAudit](DRObjectiveAudit/) | Audits recovery objectives and exercise evidence | Yes |
| [DataQualityGate](DataQualityGate/) | Enforces null, duplicate, and volume quality gates | Yes |
| [PromptCostGuard](PromptCostGuard/) | Estimates LLM workflow costs and checks budgets | Yes |
| [MLDriftWatch](MLDriftWatch/) | Screens numerical feature summaries for drift | Yes |
| [RegexRiskAudit](RegexRiskAudit/) | Flags risky regular-expression structures | Yes |
| [DependencyCycleAudit](DependencyCycleAudit/) | Detects service dependency cycles and missing references | Yes |
| [SyntheticMonitorAudit](SyntheticMonitorAudit/) | Audits synthetic-monitor coverage and alerting | Yes |
| [APIDeprecationAudit](APIDeprecationAudit/) | Audits endpoint sunset and migration readiness | Yes |
| [AuditTrailAudit](AuditTrailAudit/) | Audits security-event accountability and integrity | Yes |
| [CircuitBreakerAudit](CircuitBreakerAudit/) | Audits dependency circuit-breaker readiness | Yes |
| [FileUploadPolicy](FileUploadPolicy/) | Audits file-upload security controls | Yes |
| [GraphQLQueryBudget](GraphQLQueryBudget/) | Enforces GraphQL depth and complexity budgets | Yes |
| [IdempotencyKeyAudit](IdempotencyKeyAudit/) | Audits mutation idempotency safeguards | Yes |
| [LogSamplingAudit](LogSamplingAudit/) | Audits unsafe log-sampling policies | Yes |
| [MaintenanceScheduleAudit](MaintenanceScheduleAudit/) | Audits maintenance windows and rollback readiness | Yes |
| [MessageContractAudit](MessageContractAudit/) | Audits event-message contract governance | Yes |
| [ObservabilityCoverage](ObservabilityCoverage/) | Audits service telemetry coverage | Yes |
| [RequestTimeoutAudit](RequestTimeoutAudit/) | Audits outbound request timeout policies | Yes |
| [DataResidencyAudit](DataResidencyAudit/) | Audits declared dataset hosting regions | Yes |
| [ExternalEndpointAudit](ExternalEndpointAudit/) | Audits external endpoint safeguards | Yes |
| [CacheKeyAudit](CacheKeyAudit/) | Audits cache-key isolation and variation | Yes |
| [APIResponseBudget](APIResponseBudget/) | Audits API response size and pagination budgets | Yes |
| [ClockSkewAudit](ClockSkewAudit/) | Audits distributed-system clock synchronisation | Yes |
| [CompressionPolicyAudit](CompressionPolicyAudit/) | Audits response compression safety and efficiency | Yes |
| [ConnectionPoolAudit](ConnectionPoolAudit/) | Audits database connection-pool safeguards | Yes |
| [DeploymentHealthGate](DeploymentHealthGate/) | Enforces deployment health and rollback gates | Yes |
| [ErrorBudgetAudit](ErrorBudgetAudit/) | Audits reliability error-budget consumption | Yes |
| [MemoryLimitAudit](MemoryLimitAudit/) | Audits workload memory capacity and headroom | Yes |
| [OAuthRedirectAudit](OAuthRedirectAudit/) | Audits OAuth redirects and PKCE enforcement | Yes |
| [SearchIndexAudit](SearchIndexAudit/) | Audits search-index completeness and freshness | Yes |
| [WebSocketPolicyAudit](WebSocketPolicyAudit/) | Audits WebSocket security controls | Yes |
| [DataExportAudit](DataExportAudit/) | Audits sensitive-data export safeguards | Yes |
| [CanaryAnalysis](CanaryAnalysis/) | Compares canary and baseline rollout health | Yes |
| [DatabaseLockAudit](DatabaseLockAudit/) | Audits database lock contention | Yes |
| [DependencySLAAudit](DependencySLAAudit/) | Audits dependency service-level performance | Yes |
| [EgressPolicyAudit](EgressPolicyAudit/) | Audits workload outbound network rules | Yes |
| [GarbageCollectionAudit](GarbageCollectionAudit/) | Audits runtime GC pressure and pauses | Yes |
| [HTTPMethodAudit](HTTPMethodAudit/) | Audits unsafe HTTP method exposure | Yes |
| [JWTClaimAudit](JWTClaimAudit/) | Audits JWT claim requirements | Yes |
| [KubernetesPDBAudit](KubernetesPDBAudit/) | Audits disruption budgets and replicas | Yes |
| [LoadBalancerAudit](LoadBalancerAudit/) | Audits load-balancer resilience settings | Yes |
| [MetricCardinalityAudit](MetricCardinalityAudit/) | Audits metric cardinality risks | Yes |
| [NetworkLatencyAudit](NetworkLatencyAudit/) | Audits network latency and packet loss | Yes |
| [ObjectLifecycleAudit](ObjectLifecycleAudit/) | Audits object-storage lifecycle rules | Yes |
| [QueryTimeoutAudit](QueryTimeoutAudit/) | Audits database query timeouts | Yes |
| [ReplicaCapacityAudit](ReplicaCapacityAudit/) | Audits workload replica capacity | Yes |
| [SecretsMountAudit](SecretsMountAudit/) | Audits workload secret mounts | Yes |
| [TenantIsolationAudit](TenantIsolationAudit/) | Audits multi-tenant data isolation | Yes |
| [TracePropagationAudit](TracePropagationAudit/) | Audits distributed trace propagation | Yes |
| [BatchJobAudit](BatchJobAudit/) | Audits batch-job safety and duration | Yes |
| [EndpointOwnershipAudit](EndpointOwnershipAudit/) | Audits API endpoint ownership | Yes |
| [RollbackEvidenceAudit](RollbackEvidenceAudit/) | Audits rollback test evidence | Yes |
| [SQLParameterizationAudit](SQLParameterizationAudit/) | Screens SQL templates for unsafe interpolation | Yes |
| [BrowserStorageAudit](BrowserStorageAudit/) | Audits sensitive browser-side storage | Yes |
| [TLSCipherAudit](TLSCipherAudit/) | Audits TLS protocol and cipher inventories | Yes |
| [LocaleFallbackAudit](LocaleFallbackAudit/) | Audits translation fallback coverage | Yes |
| [CSVInjectionAudit](CSVInjectionAudit/) | Detects spreadsheet formula injection in CSV data | Yes |
| [FeatureStoreParity](FeatureStoreParity/) | Compares offline and online feature definitions | Yes |
| [TrafficShiftAudit](TrafficShiftAudit/) | Audits staged traffic rollout plans | Yes |
| [KubernetesHPAAudit](KubernetesHPAAudit/) | Audits Kubernetes autoscaler configuration | Yes |
| [ClientRetryBudget](ClientRetryBudget/) | Audits bounded client retry policies | Yes |
| [ContainerImageLifecycle](ContainerImageLifecycle/) | Audits container image pinning and maintenance metadata | Yes |
| [ModelServingSLOAudit](ModelServingSLOAudit/) | Audits model-serving SLO and saturation signals | Yes |
| [LoginAbuseAudit](LoginAbuseAudit/) | Audits login abuse and recovery protections | Yes |
| [CertificateChainAudit](CertificateChainAudit/) | Audits certificate-chain trust and hostname validation | Yes |
| [DatabaseTransportAudit](DatabaseTransportAudit/) | Audits database encryption and connection restrictions | Yes |
| [ExperimentGuardrailAudit](ExperimentGuardrailAudit/) | Audits product experiment guardrails and assignment controls | Yes |
| [MobileDeepLinkAudit](MobileDeepLinkAudit/) | Audits mobile deep-link authorization and validation | Yes |
| [APIKeyRotationAudit](APIKeyRotationAudit/) | Audits API-key rotation and ownership | Yes |
| [DataDeletionEvidenceAudit](DataDeletionEvidenceAudit/) | Tracks data-deletion requests and completion evidence | Yes |
| [BuildArtifactRetentionAudit](BuildArtifactRetentionAudit/) | Audits build-artifact retention and access | Yes |
| [IncidentCommunicationAudit](IncidentCommunicationAudit/) | Audits incident stakeholder update records | Yes |

## Getting started

Clone the repository, choose an agent directory, and follow that agent's README.

```bash
git clone https://github.com/ASHTOW2102/AI_AGENTS.git
cd AI_AGENTS
```

Each agent keeps its own dependencies and environment example. Never commit a populated .env file.
