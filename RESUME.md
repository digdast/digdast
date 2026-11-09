# EFRAIN RIVAS
**Senior Cloud Architect | DevOps & Infrastructure Systems Engineer**  
*Enterprise Cloud (Azure/Entra ID) | 10-Node HA Kubernetes | Active Directory (7 Data Centers) | Proxmox VE & Multi-Hypervisor SAN | Sovereign AI & DevOps Automation*  
Cary, NC • [resume.ertechlab.com](https://resume.ertechlab.com) • [linkedin.com/in/efrain-rivas-93455a10](https://www.linkedin.com/in/efrain-rivas-93455a10) • [github.com/digdast](https://github.com/digdast)

---

## Executive Summary
Results-driven **Senior Cloud Architect, DevOps Engineer, and Infrastructure Systems Administrator** with 20+ years of hands-on enterprise experience designing, modernizing, and automating mission-critical infrastructure across Microsoft Azure, High-Availability Kubernetes, Sovereign AI/LLM platforms, Active Directory Domain Services, Linux, and multi-hypervisor SAN clusters. Proven architectural track record deploying global multi-site Active Directory forests across 7 data centers, directing 5-stage financial CI/CD release pipelines with 99.999% SLA uptime, orchestrating a 10-node high-availability Kubernetes (K3s) cluster (5-node etcd quorum + 5 workers, 72 vCPUs / 84GB RAM, 70+ pods across 14 namespaces), engineering dual-GPU local AI & multi-agent inference platforms (90+ tok/sec Flash-Attention), and delivering zero-touch endpoint governance via Microsoft Intune and Windows Autopilot. Creator of open-source infrastructure & DevOps platforms (**NovaFlix, AegisDNS, SynapseFlow, Pulsearr, Renamarr, PrintForge, Proxmox Cluster Suite, 58+ Intune remediation modules**) with deep expertise in PowerShell 7, Python (Asyncio/FastAPI), Infrastructure-as-Code (Terraform/Ansible), and Zero Trust identity governance.

---

## Core Technical Competencies & Systems Matrix

* **Cloud Architecture & Identity Governance**: Microsoft Azure (VMs, VNets, NSGs, AKS, Azure Files, Automation Runbooks, AVD, FSLogix), Microsoft Entra ID (Azure AD), Active Directory Domain Services (Multi-Site Forests across 7 Data Centers, DCs, GPOs, Kerberos/LDAP, DFSR), Hybrid Identity (Entra Connect, PHS/PTA, Seamless SSO), Conditional Access, PIM, Microsoft 365 & Exchange Online Administration.
* **DevOps, GitOps & Infrastructure Automation**: CI/CD Release Pipelines (5-Stage DEV ➔ QA ➔ UAT ➔ Staging ➔ PROD), Infrastructure-as-Code (Terraform, Ansible), PowerShell 7+ (Enterprise Tooling, Microsoft Graph API, Active Directory & GPO Automation), Python (Asyncio, FastAPI, SQLite WAL, Paramiko), Bash, GitHub Actions, Automated Let's Encrypt DNS-01 SSL/TLS Lifecycles, Systemd Daemons.
* **Containers & High-Availability Kubernetes**: 10-Node HA K3s / K8s Cluster (5-node control-plane etcd quorum + 5 worker nodes, 72 vCPUs / 84GB RAM, 70+ pods across 14 production namespaces), Traefik & Nginx Proxy Manager Ingress, Cloudflare Zero Trust Tunnel DaemonSets (`cloudflared`), Klipper ServiceLB, NVMe HostPath & Shared NFS Persistent Storage, Kernel `sysctl` Optimization, Automated etcd Compaction.
* **Virtualization, Hypervisors & Enterprise SAN**: Proxmox VE (5-Node HA Cluster, 12-Core AVX2 Host Passthrough, Zero-Balloon Memory Tuning, LXC-to-K8s Live Migration), Storage Area Networks (SAN — iSCSI, Fibre Channel, MPIO), VMware vSphere / ESXi (vCenter, vMotion, DRS, HA), Linux KVM, Citrix XenServer / XCP-NG, Microsoft Hyper-V Failover Clustering, Ceph / ZFS / NFS Arrays.
* **Sovereign AI, LLM Infrastructure & Multi-Agent Swarms**: Dual-GPU AI Platform (NVIDIA GeForce RTX 5070 Blackwell + RTX 3060, Driver 595.112, CUDA 13.2 / 12.4), Ollama Flash-Attention Local LLM Inference (90+ tok/sec), Hermes Autonomous Multi-Agent Swarm & Paperclip AI Control Plane, SynapseFlow Visual DAG Workflow Engine, Open WebUI, ChromaDB Vector RAG Embeddings, Faster-Whisper STT.
* **Endpoint Engineering & Zero-Touch Governance**: Microsoft Intune (MDM/MAM), Windows Autopilot (Zero-Touch Provisioning), SCCM / MECM Modernization, Win32 Application Packaging (`.intunewin`), 58+ Proactive Remediation Modules, BitLocker Automated Key Escrow, Enterprise Patch Compliance, Windows Server (NT 4.0 through 2022), RHEL / Ubuntu / Debian Linux, macOS.
* **Zero Trust Security, DNSSEC & Observability**: Authentik Enterprise SSO/IdP (SAML 2.0, OIDC/OAuth2, PostgreSQL 17, Redis), Checkmk Enterprise Monitoring, Reconya Continuous Layer-2 ARP/ICMP Asset Discovery, 3-Node High-Availability Pi-hole v6 + Unbound Recursive DNSSEC + Cloudflare DoH Cluster (Nebula-Sync), AegisDNS (RFC 8484 DoH & 227k+ Threat Sinkhole Rules).

---

## Professional Experience

### **O.S. Consulting, Inc.** | Remote
**Senior Cloud, DevOps & Infrastructure Architect** | *2025 – Present*
* **10-Node High-Availability Kubernetes (K3s) Orchestration**: Architected and deployed a 10-node HA K3s cluster (5 etcd control-plane quorum nodes + 5 worker nodes, 72 vCPUs, 84GB RAM) orchestrating 70+ pods across 14 production namespaces (`ai`, `authentik`, `database`, `monitoring`, `npm`, `portainer`, `printforge`, `tomcat`, `tools`, `web`); engineered Cloudflare Zero Trust Tunnel DaemonSets, Traefik & NPM ingress, kernel `sysctl` tuning, and NVMe/NFS persistent storage.
* **Sovereign Dual-GPU AI, RAG & Autonomous Agent Infrastructure**: Engineered a dedicated dual-GPU AI platform (NVIDIA RTX 5070 Blackwell + RTX 3060) running Ollama (90+ tok/sec Flash-Attention), Open WebUI with CUDA-accelerated ChromaDB vector RAG embeddings and Faster-Whisper STT, Hermes 5-agent autonomous engineering swarm (bidirectional Telegram Bot streaming), and SynapseFlow visual DAG automation.
* **Proxmox VE Fleet & Workload Modernization**: Administer a 5-node Proxmox VE HA cluster, executing live LXC-to-Kubernetes workload migrations (Apache Tomcat 10.1, Reconya network discovery), configuring 12-core AVX2 host CPU passthrough and 4GB RAM `tmpfs` buffers, and eliminating hypervisor memory ballooning contention.
* **Tri-Node DNSSEC/DoH & Automated GitOps SSL Lifecycle**: Engineered a 3-node synchronized Pi-hole v6, Unbound recursive DNSSEC, and Cloudflare DoH sidecar cluster replicated via Nebula-Sync; built automated Let's Encrypt wildcard SSL renewal pipelines using Cloudflare DNS-01 APIs and Kubernetes CronJobs.
* **Hybrid Cloud Identity & Zero-Touch Endpoint Governance**: Architect hybrid Active Directory to Microsoft Entra ID synchronizations (PHS, Seamless SSO, Conditional Access, PIM) and modernize legacy SCCM/GPO estates into zero-touch Microsoft Intune and Windows Autopilot deployments backed by 58+ custom PowerShell proactive remediation scripts.
* **Enterprise SSO, Tier-3 Observability & Asset Discovery**: Deployed in-cluster Authentik SSO/IdP (PostgreSQL 17 + Redis), Checkmk Raw Edition telemetry, and Reconya continuous Layer-2 ARP/ICMP discovery; serve as principal Tier-3 escalation architect for complex cloud, hypervisor, directory, and network root cause analysis (RCA).

### **BlueMatrix** | Durham, NC
**Senior Systems Administrator & Cloud Infrastructure Architect** | *2018 – 2025*
* **Global Multi-Site Active Directory Forest (7 Data Centers)**: Architected, built, and maintained enterprise Active Directory forest and domain infrastructure across 7 global data centers and regional offices; engineered multi-site replication topology, site-link cost weighting, and distributed DNS to guarantee sub-second authentication worldwide.
* **Multi-Hypervisor Virtualization & Storage Area Networks (SAN)**: Administered and tuned high-density virtualization clusters across VMware vSphere/ESXi, Linux KVM, Citrix XenServer, and XCP-NG; architected enterprise Storage Area Networks (SAN), iSCSI/Fibre Channel LUNs, MPIO fabrics, shared NFS arrays, dynamic memory allocation, and disaster recovery snapshot replication.
* **Microsoft Azure Cloud Migration & IaaS/PaaS Automation**: Spearheaded phased cloud migrations transitioning mission-critical on-premises workloads to Microsoft Azure; architected VNets, Network Security Groups (NSGs), Azure Virtual Machines, Azure Files, and custom Azure Automation Runbooks for scheduled compute scaling and patch governance.
* **Automated Identity Lifecycle & Zero-Touch Provisioning**: Developed enterprise PowerShell and Microsoft Graph API automation workflows integrating HR systems with AD DS and Entra ID, automating account provisioning, RBAC security group delegation, M365 licensing, BitLocker key escrow, and zero-day offboarding revocation.

### **StreamingEdge (Tradition America Holdings)** | New York, NY (Hybrid)
**DevOps Engineer & Senior Systems Administrator** | *2013 – 2018*
* **Financial CI/CD Release Pipeline Engineering**: Directed release engineering across a structured 5-stage deployment pipeline (DEV ➔ QA ➔ UAT ➔ Staging ➔ Production) for institutional high-frequency financial trading systems, orchestrating zero-downtime application releases, automated rollback gates, and configuration verification.
* **Five-Nines (99.999% SLA) Hybrid Server Reliability**: Engineered and administered mission-critical Windows Server (2012–2016) and Linux (RHEL, CentOS, Ubuntu) server farms hosting low-latency financial transaction engines, consistently maintaining 99.999% production SLA uptime.
* **Clustered Virtualization & Enterprise SAN Fabrics**: Managed fault-tolerant virtualization clusters across Microsoft Hyper-V and VMware vSphere backed by enterprise Storage Area Networks (SAN), configuring Multi-Path I/O (MPIO), multi-NIC teaming, virtual switch isolation, host failover clustering, and DR replication.
* **Enterprise Networking & Perimeter Security**: Designed and maintained high-throughput LAN/WAN routing, core switching, hardware firewalls, site-to-site IPsec VPN tunnels, and enterprise VOIP telecommunications infrastructure.

### **Datapipe** | Jersey City, NJ
**NOC Infrastructure Engineer** | *2012 – 2013*
* **24x7 Managed Cloud, SAN & Hybrid Fleet Operations**: Monitored and maintained 24x7 high availability across hosted Windows Server and Unix/Linux web, application, and database server fleets backed by enterprise SAN storage within a mission-critical managed services NOC.
* **Multi-Tier Incident Triage & SLA Restoration**: Responded to real-time infrastructure, network, and SAN fabric alerts, triaged and resolved complex multi-tier outages, and executed standard operating procedures (SOPs) to guarantee strict client SLA restoration targets.
* **Database Administration & Runbook Engineering**: Supported production Microsoft SQL Server and MySQL environments (health checks, backup verification, performance telemetry) and authored detailed incident post-mortems (RCAs) and operational runbooks.

### **Digital Network Development** | Peoria, IL
**Senior Network & Systems Administrator** | *1999 – 2011*
* **Enterprise Windows Server & Active Directory Operations**: Commissioned, upgraded, and administered physical enterprise server farms spanning Windows NT 4.0, 2000, 2003, and 2008, governing Active Directory, Group Policy Objects (GPO), DNS, DHCP, WDS/MDT bare-metal OS imaging, and storage arrays.
* **Core Networking, Cisco Routing & Telecommunications**: Engineered, programmed, and maintained managed Cisco switches, routers, hardware firewalls, multi-building wireless links, T1/T3 telecommunications circuits, and enterprise VOIP telephony platforms.
* **Disaster Recovery & Tier-3 Escalation Leadership**: Served as primary technical escalation point for server crashes, routing bottlenecks, and tape/NAS disaster recovery routines across distributed enterprise environments.

---

## Flagship Engineering Projects & Open Source Tools

* **10-Node HA Kubernetes (K3s) Cluster & Zero Trust Ingress**: Production 10-node K3s cluster (5-node etcd quorum + 5 workers, 72 vCPUs / 84GB RAM, 70+ pods across 14 namespaces) with Authentik SSO, Checkmk, 3-Node Pi-hole DoH/DNSSEC, Cloudflared DaemonSet, and HA web hosting. ([resume.ertechlab.com](https://resume.ertechlab.com))
* **Sovereign Dual-GPU AI, Hermes Swarm & SynapseFlow**: Dual-GPU AI platform (RTX 5070 Blackwell + RTX 3060) running Ollama (90+ tok/sec), CUDA ChromaDB RAG, Hermes 5-agent autonomous engineering swarm with bidirectional Telegram control, and SynapseFlow visual DAG automation engine. ([github.com/digdast/synapseflow](https://github.com/digdast/synapseflow))
* **NovaFlix (Creator & Architect)**: Sovereign open-source media platform & home theater engine (Plex/Jellyfin alternative) featuring 4K HDR Direct Play, HTTP 206 Range streaming, built-in remote access, SyncPlay watch party, and cross-platform client portal. ([github.com/digdast/novaflix](https://github.com/digdast/novaflix))
* **AegisDNS (Creator & Architect)**: Next-generation recursive DNS resolver & RFC 8484 DNS-over-HTTPS (DoH) engine traversing ICANN root hints with zero telemetry, sub-0.5ms cache, 227k+ active threat sinkhole rules, and real-time cyber command center. ([github.com/digdast/aegisdns](https://github.com/digdast/aegisdns))
* **Pulsearr & Renamarr (Creator & Architect)**: Asynchronous Python media daemon unifying Sonarr, Radarr, and Prowlarr into an 85MB FastAPI/SQLite WAL engine (10x memory reduction) ([github.com/digdast/pulsearr](https://github.com/digdast/pulsearr)) + zero-config IMDb/TVMaze media organizer with 1-click undo ledger ([github.com/digdast/renamarr](https://github.com/digdast/renamarr)).
* **Proxmox Cluster Suite & PrintForge 3D + Intune Catalog**: Automated 5-node Proxmox VE HA optimization & telemetry suite ([github.com/digdast/proxmox-cluster-suite](https://github.com/digdast/proxmox-cluster-suite)), 2-replica K3s 3D printing portal ([3dprinting.ertechlab.com](https://3dprinting.ertechlab.com)), and 58 open-source PowerShell Intune/Autopilot remediation modules ([github.com/digdast/Intune-scripts](https://github.com/digdast/Intune-scripts)).

---

## Industry Certifications & Technical Credentials

* **Microsoft Certified**: Azure Administrator Associate (AZ-104)
* **Microsoft 365 Certified**: Administrator Expert (MS-102)
* **Microsoft Entra ID**: Administration & Identity Security
* **CompTIA Security+** Certified
* **CompTIA Network+** Certified
* **Inter-Tel University**: Telecommunications & VOIP Systems Engineering
