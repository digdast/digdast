# EFRAIN RIVAS
**Senior Cloud Architect & Infrastructure Systems Engineer**  
*Enterprise Cloud & Kubernetes | Active Directory & Entra ID | Proxmox VE & Virtualization | DevOps / CI/CD*  
Cary, NC • [resume.ertechlab.com](https://resume.ertechlab.com) • [linkedin.com/in/efrain-rivas-93455a10](https://www.linkedin.com/in/efrain-rivas-93455a10) • [github.com/digdast](https://github.com/digdast)

---

## Executive Summary
Results-driven Senior Cloud Architect and Systems Engineer with 20+ years of enterprise experience designing, modernizing, and automating mission-critical infrastructure across Microsoft Azure, Kubernetes, Active Directory, Entra ID, Linux, and multi-hypervisor environments. Proven track record architecting global Active Directory forests across 7 data centers, managing financial CI/CD release pipelines with 99.999% SLA uptime, engineering high-availability containerized microservices clusters, and delivering zero-touch endpoint provisioning via Microsoft Intune and Windows Autopilot. Skilled at translating complex business needs into resilient, automated architectures spanning physical bare-metal servers to cloud-native platforms. Creator of open-source automation platforms (NovaFlix, AegisDNS, Pulsearr, 58+ Intune modules) with deep expertise in PowerShell, Python, Proxmox VE clustering, and enterprise identity governance.

---

## Core Competencies & Technical Skills

* **Cloud & Directory Services**: Microsoft Azure (VMs, VNets, NSGs, AKS, Azure Files, Runbooks), Entra ID (Azure AD), Active Directory Domain Services (AD DS), Hybrid Identity (Entra Connect / PHS), Microsoft 365, Exchange Online, Group Policy (GPO).
* **Containers & Kubernetes**: Kubernetes (k3s / k8s HA multi-node clusters, control-plane failover, worker pools, Traefik ingress, NodePort / LoadBalancer services, NFS persistent storage, rolling deployments, pod self-healing).
* **Virtualization & Hypervisors**: Proxmox VE (HA multi-node clustering, zero-downtime memory tuning, Ceph / ZFS / NFS shared storage, LXC containerization, cloud-init), VMware vSphere / ESXi, Linux KVM, Citrix XenServer, XCP-NG, Microsoft Hyper-V, Azure Virtual Desktop (AVD), FSLogix.
* **DevOps & Automation**: PowerShell 7+ (Enterprise Scripting, Tooling, GPO Automation), Python (Asyncio, FastAPI, PyParamiko), Bash, CI/CD Delivery Pipelines (DEV/QA/UAT/Staging/PROD), Azure Automation Runbooks, Systemd service/timer daemons, Git Version Control.
* **Endpoint & Device Management**: Microsoft Intune (MDM/MAM), Windows Autopilot (Zero-Touch), SCCM / MECM, Win32 App Packaging (.intunewin), Proactive Remediations, Windows 10/11, macOS, iOS, Android, Patch Governance.
* **Security & Identity Governance**: Zero Trust Architecture, Automated SSL/TLS Lifecycle (Let's Encrypt DNS-01 / Cloudflare API, systemd timers), Privileged Identity Management (PIM), Conditional Access, FIDO2 / MFA, SAML 2.0 & OAuth 2.0 SSO, BitLocker / TPM Encryption, SecOps Hardening, Defender for Cloud.
* **Networking, DNS & Storage**: Recursive DNSSEC Resolvers (Pi-hole v6, Unbound root hint recursion, DoH/DoT, multi-node sync), LAN/WAN Architecture, Routing & Switching, TCP/IP, Firewalls, Site-to-Site WireGuard / IPsec VPNs, Cloudflare Zero Trust, SAN/NAS, unRAID NFS, VOIP Telephony, T1/T3 Circuits.

---

## Professional Experience

### **O.S. Consulting, Inc.** | Remote
**Senior IT Infrastructure Consultant** | *2025 – Present*
* **Enterprise Infrastructure & Cloud Advisory**: Provide senior-level infrastructure consulting across diverse client environments, translating business requirements into scalable cloud, Kubernetes, network, endpoint, and server architectures.
* **High-Availability Kubernetes & Cluster Orchestration**: Architect and deploy resilient multi-node Kubernetes clusters with control-plane replication, worker pools, Traefik ingress routing, and persistent shared NFS storage; engineered 4-replica zero-downtime deployments with health checks and automated failover.
* **Proxmox VE & Hypervisor Fleet Optimization**: Administer multi-node Proxmox VE virtualization clusters, tuning hardware resource allocation, eliminating memory ballooning contention for guaranteed performance, and orchestrating live-migration and automated backup routines.
* **DNSSEC & Automated SSL/TLS Lifecycle**: Engineered tri-node synchronized Pi-hole v6 and Unbound recursive DNS clusters with root-hint recursion and DNSSEC validation; built automated Let's Encrypt wildcard certificate renewal pipelines via Cloudflare DNS-01 APIs and systemd timers.
* **Hybrid Identity Modernization**: Architect and execute hybrid Active Directory to Microsoft Entra ID (Azure AD) synchronizations, implementing Password Hash Sync (PHS), Seamless SSO, and risk-based Conditional Access policies.
* **Endpoint & Intune Migration**: Modernize legacy on-premise SCCM and GPO environments into cloud-native Microsoft Intune configurations; design automated Windows Autopilot deployment profiles reducing device onboarding time by over 80%.
* **Level 3 Escalation & Root Cause Analysis**: Serve as the primary Tier 3 escalation architect for complex server, network connectivity, and authentication outages, systematically conducting root cause analysis (RCA) and eliminating systemic failure points.

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

* **NovaFlix (Creator & Architect)**: Sovereign next-generation open media platform & home theater engine (Plex / Jellyfin alternative) featuring 4K HDR Direct Play, HTTP 206 Range streaming, built-in remote access, SyncPlay, and cross-platform download portal. ([github.com/digdast/novaflix](https://github.com/digdast/novaflix))
* **AegisDNS (Creator & Architect)**: Next-generation recursive DNS resolver & RFC 8484 DNS-over-HTTPS (DoH) engine traversing ICANN root hints with zero telemetry, in-memory threat defense (227k+ active threat/ad rules), and real-time cyber command center. ([github.com/digdast/aegisdns](https://github.com/digdast/aegisdns))
* **High-Availability Kubernetes Cluster & Ingress**: Orchestrated multi-node k8s cluster with Traefik ingress, shared NFS storage, and automated 4-replica zero-downtime web application hosting. ([resume.ertechlab.com](https://resume.ertechlab.com))
* **Proxmox Cluster Suite**: Automated enterprise optimization, no-sub repo activation, nag removal, CPU governor, memory ballooning elimination, and real-time monitoring for multi-node Proxmox VE HA clusters. ([github.com/digdast/proxmox-cluster-suite](https://github.com/digdast/proxmox-cluster-suite))
* **Pulsearr (Creator & Architect)**: Architected and built an ultra-fast, asynchronous Python media suite unifying Sonarr, Radarr, and Prowlarr into a single lightweight daemon; engineered with FastAPI, asyncio, SQLite WAL mode, and Gluetun WireGuard integration (85MB idle RAM vs 1.2GB .NET stack). ([github.com/digdast/pulsearr](https://github.com/digdast/pulsearr))
* **Renamarr (Creator & Architect)**: High-performance media asset organizer with zero-config IMDb/TVMaze metadata suggestions, remote CLI agent, recursive UNC network share scanning, and an atomic 1-click batch undo ledger. ([github.com/digdast/renamarr](https://github.com/digdast/renamarr))
* **Enterprise Intune Automation Catalog**: Authored and open-sourced 58 production PowerShell automation modules covering Autopilot pre-provisioning, BitLocker cipher detection, driver crash telemetry, and proactive endpoint remediations. ([github.com/digdast/Intune-scripts](https://github.com/digdast/Intune-scripts))

---

## Education & Certifications

* **Microsoft Certified**: Azure Administrator Associate (AZ-104)
* **Microsoft 365 Certified**: Administrator Expert (MS-102)
* **Microsoft Entra ID**: Administration & Identity Security
* **CompTIA Network+** Certified
* **CompTIA Security+** Certified
* **Inter-Tel University**: Telecommunications & VOIP Systems Engineering

