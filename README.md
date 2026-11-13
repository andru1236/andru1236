# Andres Gutierrez Panoso

**Principal Software Engineer at [SINCPRO](https://sincpro.dev)** · Cochabamba, Bolivia ·
remote with US and Canadian teams since 2019

I came into software as the industry moved from server-rendered monoliths to the cloud. Until
2025 my main work was technical, inside US and Canadian product teams; alongside it, I led client
implementations at SINCPRO part-time and grew into product and process work. Each step added a
layer instead of replacing the last, so today I see the whole system: the business process, the
code, the infrastructure and how it runs in production.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/layers-dark.svg">
  <img alt="Six layers, thick while each was my main work and thin while it ran alongside it: full-stack web on Linux (2017–2018), services, frontend and DDD (2018–2025), product and business process (part-time from 2021, main since 2025), Kubernetes and observability (part-time from 2021, main since 2025), data processing and integrations (2023–2025), direction and AI-driven delivery (since 2025)." src="assets/layers-light.svg" width="100%">
</picture>

Since 2025 I work at SINCPRO full time, and my focus is direction: I lead 6 engineers and 5
functional consultants, and my job is deciding what to build, how it fits
together, and keeping it secure and running for 86+ clients in production.

## How a change ships today

The agent writes the code. People decide what to build, review how it fits and test it against
the real process.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/loop-dark.svg">
  <img alt="Spec, written by the functional team; build, by an AI agent in a sandbox inside our framework; review, by engineers; preview, a per-pull-request environment tested by the functional team; production on Kubernetes, whose errors and traces go back into the next spec." src="assets/loop-light.svg" width="100%">
</picture>

## How I got here

**Full-stack web on Linux · 2017.** Django apps for a retailer, and a desktop ERP moved to the
web for a Peruvian vendor, with e-invoicing for SUNAT, Peru's tax authority, signed and sent
over SOAP. My first ERP.

**Services, frontend and DDD · 2018.** I joined US product teams through Jalasoft. On a survey
platform we used DDD and CQRS over RabbitMQ to absorb traffic peaks. At ScienceLogic, which
monitors networks and data centers for large enterprises, the client named me technical lead
of the core platform while it moved from batch monoliths to microservices.

**Data, integrations, and product on the side · 2021.** My main work stayed technical, inside
US and Canadian product teams through Encora: synthetic health data on Ray and Spark at Aetion,
a React trading client at PCI Energy Solutions, an event-driven JumpCloud integration on AWS at
Electric. Part-time at SINCPRO, I led client implementations: defining the product and the
process with each client and coordinating the team that built it. That is where product became
a skill of mine, as a certified Odoo functional implementer who sits with finance, imports and
HR teams.

**Direction and AI-driven delivery · 2025.** I moved to SINCPRO full time, and my focus moved
from building to directing: the platform, the frameworks and the client systems we had built,
and how we build from here. It started with simple tools. Writing code got cheap, so the
hard part moved to the spec, the architecture, the review and running it all in production. We
first gave coding agents our rules and domain knowledge through MCP servers, then turned that
into Forge. Today agents write most of our code from written specs, inside our own frameworks
and review gates, and my work is the platform around them.

## What I work on now

- **Frameworks.** One architecture (DDD, hexagonal, CQRS) for every Python service, web app and
  offline-first mobile app, with logs, metrics and traces wired in from the first commit.
- **Platform.** Kubernetes (RKE2) for 86+ clients in production: Kong gateway, staging, UAT and
  production deploys, and on-premise nodes for clients who keep their data on their own
  servers. Prometheus, Loki, Tempo, Grafana and GlitchTip watch all of it.
- **Forge** (internal, alpha). Implementers, functional consultants and client teams ask for a
  change from the AI assistant they already use, a web UI or an API. Agents build it in
  isolated sandboxes, and what comes back is a verified pull request with its own preview
  environment.

## The platform, in the open

| Repository | What it is | Package |
|---|---|---|
| [sincpro_framework](https://github.com/Sincpro-SRL/sincpro_framework) | Application layer for Python services: commands, features, bounded contexts | [PyPI](https://pypi.org/project/sincpro-framework/) |
| [sincpro_client_framework](https://github.com/Sincpro-SRL/sincpro_client_framework) | The same application layer in TypeScript, for web, React Native and scripts | [npm](https://www.npmjs.com/package/@sincpro/client-framework) |
| [sincpro_criteria](https://github.com/Sincpro-SRL/sincpro_criteria) | One query object (filter, order, page) shared by the TypeScript clients and the Python services | [npm](https://www.npmjs.com/package/@sincpro/criteria) |
| [sincpro_mobile](https://github.com/Sincpro-SRL/sincpro_mobile) | Offline-first framework for enterprise React Native / Expo apps | [npm](https://www.npmjs.com/package/@sincpro/mobile) |
| [sincpro_web_framework](https://github.com/Sincpro-SRL/sincpro_web_framework) | Enterprise web apps, with [web-ui](https://github.com/Sincpro-SRL/sincpro_web_ui) and [web-composer](https://github.com/Sincpro-SRL/sincpro_web_composer) | [npm](https://www.npmjs.com/package/@sincpro/web-framework) |
| [cups_http_gateway](https://github.com/Sincpro-SRL/cups_http_gateway) | A JSON/HTTP gateway to CUPS print servers, in Rust | |

## What I hold to

- **Architecture is what keeps AI-written code maintainable.** The agent writes the code; the
  framework decides where it goes.
- **If it runs in production, it reports.** Logs, metrics and traces come with the template,
  not after the first incident.
- **The person who knows the process tests the change.** Every pull request gets its own
  environment where the functional team tries it before release.

[LinkedIn](https://www.linkedin.com/in/andres-gutierrez-97129a136) ·
andres.gutierrez@sincpro.com.bo
