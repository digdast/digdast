# EFRAIN RIVAS
**Senior Cloud Architect & Infrastructure Systems Engineer**  
*Enterprise Cloud & HA Kubernetes | Sovereign AI & Multi-GPU Infrastructure | Active Directory & Entra ID | Proxmox VE & DevOps*  
Cary, NC • [resume.ertechlab.com](https://resume.ertechlab.com) • [linkedin.com/in/efrain-rivas-93455a10](https://www.linkedin.com/in/efrain-rivas-93455a10) • [github.com/digdast](https://github.com/digdast)

---

## Executive Summary
Results-driven Senior Cloud Architect and Systems Engineer with 20+ years of enterprise experience designing, modernizing, and automating mission-critical infrastructure across Microsoft Azure, Kubernetes, Sovereign AI/LLM platforms, Active Directory, Entra ID, Linux, and multi-hypervisor environments. Proven track record architecting global Active Directory forests across 7 data centers, managing financial CI/CD release pipelines with 99.999% SLA uptime, engineering 6-node high-availability Kubernetes (K3s) clusters (36 vCPUs / 56GB RAM, 50+ pods across 12 namespaces), deploying dual-GPU local AI & RAG inference platforms, and delivering zero-touch endpoint provisioning via Microsoft Intune and Windows Autopilot. Creator of open-source automation platforms (NovaFlix, AegisDNS, Pulsearr, Renamarr, PrintForge, Proxmox Cluster Suite, 58+ Intune modules) with deep expertise in PowerShell, Python, Proxmox VE clustering, and enterprise identity governance.

---

## Core Competencies & Technical Skills

* **Cloud & Directory Services**: Microsoft Azure (VMs, VNets, NSGs, AKS, Azure Files, Runbooks), Entra ID (Azure AD), Active Directory Domain Services (AD DS), Hybrid Identity (Entra Connect / PHS), Microsoft 365, Exchange Online, Group Policy (GPO).
* **Containers & High-Availability Kubernetes**: 6-Node HA K3s / K8s Clusters (dual control-plane etcd quorum + 4 worker nodes, 50+ pods across 12 namespaces), Traefik & Nginx Proxy Manager Ingress, Cloudflare Zero Trust Tunnel DaemonSets (`cloudflared`), Klipper ServiceLB, Shared NFS Persistent Storage, sysctl Kernel Tuning, etcd Compaction.
* **Sovereign AI & Multi-GPU Infrastructure**: Local LLM Inference & Multi-Agent Orchestration (Ollama, Open WebUI, Paperclip AI), Dual-GPU CUDA 12.4 Workload Isolation (NVIDIA RTX 5070 + RTX 3060), ChromaDB RAG Vector Search, Sentence-Transformers Embeddings, Faster-Whisper STT.
* **Virtualization & Hypervisors**: Proxmox VE (5-node HA clustering, AVX2 host CPU passthrough, zero-downtime memory tuning, Ceph / ZFS / NFS shared storage, LXC to K8s migrations, cloud-init), VMware vSphere / ESXi, Linux KVM, Citrix XenServer, XCP-NG, Microsoft Hyper-V, Azure Virtual Desktop (AVD), FSLogix.
* **DevOps & Automation**: PowerShell 7+ (Enterprise Scripting, Tooling, GPO Automation), Python (Asyncio, FastAPI, Paramiko), Bash, CI/CD Delivery Pipelines (DEV/QA/UAT/Staging/PROD), Ansible, Terraform, Azure Automation Runbooks, Systemd service/timer daemons, Git Version Control.
* **Endpoint & Device Management**: Microsoft Intune (MDM/MAM), Windows Autopilot (Zero-Touch), SCCM / MECM, Win32 App Packaging (.intunewin), Proactive Remediations, Windows 10/11, macOS, iOS, Android, Patch Governance.
* **Security, Identity & Observability**: Zero Trust Architecture, Authentik Enterprise SSO/IdP (PostgreSQL 17 & Redis), Checkmk Enterprise Monitoring, Reconya L2 ARP/ICMP Asset Discovery, Automated SSL/TLS Lifecycle (Let's Encrypt DNS-01 / Cloudflare API), Tri-Node Pi-hole v6 + Unbound DNSSEC + DoH Cluster with Nebula-Sync, Conditional Access, FIDO2 / MFA, BitLocker / TPM Encryption.

---

## Professional Experience

### **O.S. Consulting, Inc.** | Remote
**Senior IT Infrastructure Consultant** | *2025 – Present*
* **Enterprise Infrastructure & Cloud Advisory**: Provide senior-level infrastructure consulting across diverse client environments, translating business requirements into scalable cloud, Kubernetes, AI inference, network, endpoint, and server architectures.
* **6-Node High-Availability Kubernetes (K3s) Orchestration**: Architected and deployed a 6-node HA K3s cluster (2 etcd/control-plane nodes + 4 workers, 36 vCPUs, 56GB RAM) hosting 50+ pods across 12 production namespaces (`authentik`, `dns`, `media`, `monitoring`, `npm`, `portainer`, `printforge`, `reconya`, `tomcat`, `tools`, `web`); implemented 4-node Cloudflare Tunnel DaemonSets, Traefik & Nginx Proxy Manager ingress, kernel `sysctl` tuning, and shared NFS storage.
* **Sovereign AI & Dual-GPU RAG Infrastructure**: Engineered a dedicated dual-GPU AI workstation (NVIDIA RTX 5070 12GB + RTX 3060 12GB) running Ollama local LLMs, Open WebUI with isolated CUDA 12.4 PyTorch acceleration for ChromaDB vector RAG embeddings and Faster-Whisper speech transcription, and Paperclip AI multi-agent control plane orchestration.
* **Proxmox VE Fleet & Workload Modernization**: Administer a 5-node Proxmox VE HA cluster, executing live LXC-to-Kubernetes workload migrations (Apache Tomcat 10.1, Reconya network discovery), configuring 12-core AVX2 host passthrough and RAM `tmpfs` transcode buffers, and eliminating memory ballooning contention.
* **Resilient DNSSEC, DoH & Automated SSL/TLS Lifecycle**: Engineered a 3-node synchronized Pi-hole v6, Unbound recursive DNSSEC, and Cloudflare DoH sidecar cluster replicated via Nebula-Sync; built automated Let's Encrypt wildcard certificate renewal pipelines via Cloudflare DNS-01 APIs and Kubernetes CronJobs.
* **Enterprise SSO, Observability & Asset Discovery**: Deployed in-cluster Authentik SSO/IdP (PostgreSQL 17 + Redis), Checkmk Raw Edition monitoring, and Reconya continuous Layer-2 ARP/ICMP network reconnaissance across production subnets.
* **Hybrid Identity & Endpoint Modernization**: Architect hybrid Active Directory to Microsoft Entra ID synchronizations (PHS, Seamless SSO, Conditional Access) and modernize legacy SCCM/GPO estates into zero-touch Microsoft Intune and Windows Autopilot deployments.

### **BlueMatrix** | Durham, NC
**Senior Systems Administrator & Infrastructure Architect** | *2018 – 2025*
* **Global Active Directory Architecture**: Architected, built, and deployed enterprise Active Directory forest and domain infrastructure across 7 global data centers and regional offices; optimized multi-site replication topology, site-cost weighting, and DNS to ensure sub-second global authentication.
* **Enterprise Multi-Hypervisor Virtualization**: Administered, tuned, and maintained multi-node virtualization clusters across Linux KVM, Citrix XenServer, VMware vSphere, and XCP-NG; orchestrated shared SAN/NFS storage, vCPU allocation, and disaster recovery replication.
* **Azure Cloud Migration & Modernization**: Led phased cloud migration initiatives transitioning legacy on-premise workloads to Microsoft Azure; engineered VNets, Network Security Groups (NSGs), Azure Virtual Machines, and Azure Automation Runbooks to automate scheduled compute and patch cycles.
* **Fleet-Wide Intune & Endpoint Governance**: Governed endpoint management across Windows, macOS, and mobile devices using Microsoft Intune and SCCM; deployed proactive remediation scripts, automated BitLocker key escrow, and streamlined Win32 app packaging.
* **Identity Lifecycle & Onboarding Automation**: Built robust PowerShell automation for new employee onboarding and offboarding, automating AD/Entra ID account creation, license assignment, mailbox provisioning, and security group memberships.

### **StreamingEdge, a Tradition America Holdings Company** | New York, NY (Hybrid)
**DevOps Engineer & Systems Administrator** | *2013 – 2018*
* **Multi-Stage CI/CD Release Engineering**: Directed release engineering across a structured 5-stage deployment pipeline (DEV ➡️ QA ➡️ UAT ➡️ Staging ➡️ Production) for high-frequency financial trading systems, coordinating zero-downtime application deployments and release windows.
* **High-Availability Windows & Linux Platforms**: Engineered and administered mission-critical Windows Server (2012–2022) and Linux (RHEL, Ubuntu, CentOS) infrastructure hosting financial transaction engines, achieving 99.999% production SLA uptime.
* **Virtualization Infrastructure**: Managed clustered enterprise virtualization across Microsoft Hyper-V and VMware vSphere, optimizing host resource allocation, failover clustering, and virtual network switching.
* **LAN/WAN Network Architecture**: Designed, deployed, and maintained enterprise connectivity infrastructure spanning high-throughput routers, switches, firewalls, site-to-site IPsec VPNs, wireless networks, and enterprise VOIP systems.
* **Observability & Incident Management**: Implemented proactive infrastructure monitoring and alerting; led Tier 3 incident troubleshooting during production anomalies, authoring post-incident RCAs and automated recovery procedures to eliminate recurring failures.

### **Digital Network Development** | Peoria, IL
**Senior Network Administrator** | *1999 – 2011*
* **Enterprise Windows Server Administration**: Built, upgraded, and administered physical server infrastructure across Windows NT 4.0, Windows 2000, Windows Server 2003, and 2008, managing Active Directory, Group Policy, DNS, DHCP, and enterprise file/print services.
* **Telecommunications & Enterprise Networking**: Designed, installed, programmed, and maintained hardware switches, routers, multi-building wireless links, T1/T3 telecommunications circuits, and enterprise VOIP phone systems.
* **Tier 3 Escalation Leadership**: Acted as the primary technical escalation authority for desktop support and engineering teams, resolving mission-critical server crashes, network routing bottlenecks, and system integration failures.
* **Data Protection & Disaster Recovery**: Managed enterprise backup routines, storage arrays, antivirus deployments, OS imaging (WDS/MDT), and routine patch compliance across distributed server farms.

---

## Key Technical Projects & Open Source

* **6-Node HA Kubernetes (K3s) Cluster & Cloudflared Mesh**: Production 6-node K3s cluster (`v1.36.5+k3s1`, 36 vCPUs / 56GB RAM) running 50+ pods across 12 namespaces with Authentik SSO, Checkmk, Tri-Node Pi-hole DoH/DNSSEC, 4-node Cloudflared Tunnel DaemonSet, Traefik & NPM ingress, and 4-replica HA web services. ([resume.ertechlab.com](https://resume.ertechlab.com))
* **Sovereign Dual-GPU AI & RAG Platform**: Self-hosted LLM inference and multi-agent control plane combining Ollama (RTX 5070 12GB), Open WebUI with dedicated CUDA 12.4 RAG vector embedding & Faster-Whisper acceleration (RTX 3060 12GB), and Paperclip AI orchestration.
* **NovaFlix (Creator & Architect)**: Sovereign next-generation open media platform & home theater engine (Plex / Jellyfin alternative) featuring 4K HDR Direct Play, HTTP 206 Range streaming, built-in remote access, SyncPlay, and cross-platform download portal. ([github.com/digdast/novaflix](https://github.com/digdast/novaflix))
* **AegisDNS (Creator & Architect)**: Next-generation recursive DNS resolver & RFC 8484 DNS-over-HTTPS (DoH) engine traversing ICANN root hints with zero telemetry, in-memory threat defense (227k+ active threat/ad rules), and real-time cyber command center. ([github.com/digdast/aegisdns](https://github.com/digdast/aegisdns))
* **PrintForge 3D Portal (Creator & Architect)**: High-performance dark-mode 3D printing portal, calibration masterclass suite, 2026 printer benchmarks, and curated 3D model vault hosted on a 2-replica K3s deployment. ([3dprinting.ertechlab.com](https://3dprinting.ertechlab.com))
* **Proxmox Cluster Suite**: Automated enterprise optimization, no-sub repo activation, nag removal, CPU governor, memory ballooning elimination, and real-time monitoring for multi-node Proxmox VE HA clusters. ([github.com/digdast/proxmox-cluster-suite](https://github.com/digdast/proxmox-cluster-suite))
* **Pulsearr & Renamarr (Creator & Architect)**: Asynchronous Python media suite unifying Sonarr, Radarr, and Prowlarr into an 85MB FastAPI/SQLite WAL daemon ([github.com/digdast/pulsearr](https://github.com/digdast/pulsearr)), paired with a zero-config IMDb/TVMaze asset organizer and 1-click undo ledger ([github.com/digdast/renamarr](https://github.com/digdast/renamarr)).
* **Enterprise Intune Automation Catalog**: Authored and open-sourced 58 production PowerShell automation modules covering Autopilot pre-provisioning, BitLocker cipher detection, driver crash telemetry, and proactive endpoint remediations. ([github.com/digdast/Intune-scripts](https://github.com/digdast/Intune-scripts))

---

## Education & Certifications

* **Microsoft Certified**: Azure Administrator Associate (AZ-104)
* **Microsoft 365 Certified**: Administrator Expert (MS-102)
* **Microsoft Entra ID**: Administration & Identity Security
* **CompTIA Network+** Certified
* **CompTIA Security+** Certified
* **Inter-Tel University**: Telecommunications & VOIP Systems Engineering
