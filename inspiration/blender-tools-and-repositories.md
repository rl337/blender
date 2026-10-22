# Blender and Agentic 3D: Reference Tool & Repository Catalog

Status: Living inspiration index (not an implementation commitment)  
Created: 2026-10-21  
Home: rl337/blender  
Purpose: A recurring reference of distinct tools, repositories and techniques discussed for agentic Blender production. Verify upstream APIs, licensing and maturity before implementation.

## Product and Blender-agent references

| Project | Source | Relevant ideas | Investigation |
| --- | --- | --- | --- |
| Loopcut | https://loopcut.org/ ; https://github.com/loopcut-ai/loopcut | Scene-aware assistant, bpy generation, visual feedback, scene checkpoints, motion generation/retargeting, rendering, ChatGPT account sign-in claims | Inspect actual Blender agent source and supported auth mechanism; do not assume third-party OAuth grants subscription inference. |
| Scenario Blender extension | https://blender.scenario.com/ ; https://github.com/scenario-labs/blender-plugin | Local MCP, scene_summary/object_detail, Python execution, multi-view contact sheets, blockouts, camera paths, film recipes, materials, cloud jobs, cost approval, recovery | Examine source for reusable interfaces; avoid dependence on Scenario cloud. |
| BlenderAI | https://github.com/kakajan/blenderAI | In-Blender agent chat, local/cloud inference, modelling/material/lighting skills, external agent control | Compare semantic operations and tool surface. |
| Blender MCP | https://github.com/ahujasid/blender-mcp | Agent-driven Blender scene tools, Python, renders, optional asset services | Compare protocol boundaries and safety. Earlier discussion also referred to a teamipc/blender-mcp variant; verify exact repository identity. |
| Blender MCP Server (Blender ecosystem) | Search upstream official Blender MCP Server project | Blender-facing MCP API, version compatibility, code-execution risks | Confirm upstream ownership, URL and Blender requirements before citing as official. |
| Scenario agent skills | Scenario companion skills repository (verify URL) | Domain-specific agent workflows and skill descriptions | Evaluate reuse of skill contracts, not code by default. |

## 3D asset generation, modelling and libraries

| Project | Source | Relevant ideas | Investigation |
| --- | --- | --- | --- |
| Microsoft TRELLIS / TRELLIS.2 | https://github.com/microsoft/TRELLIS | Image-to-3D generation, mesh/GLB asset candidates | Benchmark local memory and geometry quality; verify TRELLIS.2 repository and licence separately. |
| TripoSR | https://github.com/VAST-AI-Research/TripoSR | Single-image 3D reconstruction for props | Evaluate topology, scale, textures, clean-up. |
| Stable Fast 3D | https://github.com/Stability-AI/stable-fast-3d | Rapid image-to-3D | Check licence/commercial limits before adopting. |
| Hunyuan3D | https://github.com/Tencent-Hunyuan/Hunyuan3D-2 | Image/text-assisted 3D | Review model-specific licensing; not a default dependency. |
| Hyper3D Rodin | https://hyper3d.ai/ | Hosted text/image-to-3D | Optional inspiration, not local-first default. |
| MakeHuman | http://www.makehumancommunity.org/ | Reusable human bases and character creation | Review rig interoperability and licence. |
| Poly Haven | https://polyhaven.com/ | HDRIs, materials, 3D assets and asset discovery | Catalogue provenance/licence per asset. |
| Sketchfab | https://sketchfab.com/ | Searchable asset collections and metadata | Respect per-asset licensing and provenance. |
| Scenario plugin's modelling tools | https://github.com/scenario-labs/blender-plugin | Concept art, mesh generation, remesh/retexture, auto-rigging, PBR | Extract typed workflows, not vendor coupling. |

## Adjacent media, animation and scene pipelines

| Project | Source | Relevant ideas | Investigation |
| --- | --- | --- | --- |
| ComfyUI | https://github.com/comfyanonymous/ComfyUI | Graph-based image/video workflows, reference images, textures, background plates, render-to-video | Blender depth/normal/wireframe passes as conditioning inputs. |
| VoiceStudio | https://github.com/debpalash/VoiceStudio | Local voice and audio asset production | Integrate through media pipeline, not Blender core. |
| Wan2.x | https://github.com/Wan-Video | Local video generation | Assess video continuity with Blender spatial controls. |
| LTX-Video | https://github.com/Lightricks/LTX-Video | Video generation/editing | Test Blender-guided compositing and cost. |
| Whisper | https://github.com/openai/whisper | Transcription and caption timing | Scene timeline synchronization. |
| Kdenlive | https://kdenlive.org/ | Video editing and assembly | Export/round-trip contracts. |
| Remotion | https://www.remotion.dev/ | Deterministic timelines and programmatic rendering | Useful reference for shot specifications. |
| HyperFrames; claude-motion-design; claude-motion; motion-graphics-skills; animate; product-launch-motion; motion-graphics | Repositories previously discussed in NeoStudio motion-design work; exact upstream URLs to verify | Seekable timelines, animation grammar, frame inspection, iterative visual QA | Resolve exact repositories before implementing. |

## Alternative scene engines and simulation references

| Project | Source | Relevant ideas |
| --- | --- | --- |
| Godot and Godot MCP | https://godotengine.org/ | Alternative headless scene compilation and animation backend |
| Unity and Unity MCP | https://unity.com/ | Alternative runtime and editor automation |
| Three.js / Drei | https://threejs.org/ ; https://github.com/pmndrs/drei | Camera/lighting/GLTF inspection and web previews |
| React Three Rapier | https://github.com/pmndrs/react-three-rapier | Deterministic prop physics |
| Yuka | https://github.com/Mugen87/yuka | Character and actor behavior |
| Three.quarks | https://github.com/Alchemist0823/three.quarks | Particle effects |
| React Postprocessing | https://github.com/pmndrs/react-postprocessing | Visual effects |
| Colyseus | https://github.com/colyseus/colyseus | Coordinated interactive scene state |

## Ownership and architectural interpretation

- **rl337/blender**: temporary integration foundry, existing handmade assets, curated 3D object/scene library, Blender-specific typed operations, recipes, previews, geometry validation and manifests. Preserve existing assets and paths until inventoried.
- **MechaHarness**: generic typed execution, dependency injection, checkpointing, bounded repair, visual judges, tool permissions, host-parameterized credentials, optional Codex escalation, human/test/agent drivers.
- **June**: optional central orchestrator, scheduling, remote supervision, resource-aware routing, persistence, approvals, artifact lifecycle and local inference scheduling.
- **Folk CMS library**: reusable asset registry and metadata API, taxonomy, search, provenance, versions and cross-project references; optional MCP exposure.
- **NeoStudio / Folk**: domain-specific characters, shots, scenes, animation, production and content needs.
- **home_network**: deploy reproducible headless Blender workers on 8 GB Raspberry Pi nodes; JuneSpark runs local inference; heavier rendering may route to a Mac.

## Principles to revisit

1. Local-first inference, with Codex escalation only for hard failures; subscription authentication must use a supported integration.
2. Prefer typed, deterministic bpy operations over unconstrained generated Python; gate arbitrary code.
3. Each asset has stable ID, primary type, orthogonal taxonomy facets, licence, provenance, dependencies, version, source recipe, validation evidence and previews.
4. Distinguish generated candidates from curated approved artifacts; never auto-publish solely on model confidence.
5. Treat assets as reproducible builds; support regeneration and versioned scene references.
6. Make Blender workers headless, short-lived, isolated, resource-limited and testable without June.
7. Validate geometry deterministically and appearance using multi-view visual judges; same acceptance criteria after escalation.
8. Use checkpoints, durable external-job IDs, explicit cost approval and safe reconciliation before retrying paid operations.
9. Keep Git for source/recipes/manifests and manageable assets; use LFS/object storage as size warrants.
10. Expose underlying Python capabilities first; MCP/CLI/HTTP are optional adapters, not required execution semantics.
11. Keep Blender spatial geometry authoritative; use generated video selectively for styling/compositing.
12. Test representative Pi workloads before treating all rendering or simulations as Pi-suitable.

## Initial experiments

- Inventory existing handmade assets without relocating them.
- Run a Blender ARM64 background-mode smoke test on one 8 GB Pi: primitive generation, GLB export, low-res preview, peak memory/time.
- Define versioned asset and scene manifest schemas plus controlled vocabulary and multi-facet taxonomy.
- Build a deterministic headless asset recipe with validation and contact-sheet preview.
- Run a local vision evaluator on JuneSpark, then a bounded repair cycle.
- Publish one approved asset with source, manifest, thumbnail and provenance; retrieve it through the CMS API.
- Test June-delegated execution and resume, with optional Codex escalation.

## Open questions

- Exact status/source of Loopcut's in-Blender agent and subscription authentication.
- Exact upstream URLs/licences for several previously discussed animation and MCP projects.
- Whether Folk CMS already has suitable asset/version APIs.
- Which Blender version/package works reliably on Debian Bookworm ARM64.
- Whether large binaries live in Git LFS, MinIO, or both.
- When to extract stable Blender operations into a dedicated shared package.

This catalog records inspiration and investigation leads, not verified feature parity or a decision to adopt upstream dependencies.
