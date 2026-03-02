#!/usr/bin/env python3
"""Insert AgentClear entry into README.md"""

AGENTCLEAR_ENTRY = """## [AgentClear](https://agentclear.dev)
API marketplace and commerce infrastructure for AI agents

<details>

### Category
Infrastructure, Agent tooling

### Description

- AgentClear lets AI agents discover and call 60+ API services using semantic search
- Agents describe what they need in natural language; AgentClear finds matching services ranked by trust score
- Built-in micropayments \u2014 sub-cent per-call billing, no monthly subscriptions
- Works with any agent framework: LangChain, CrewAI, AutoGen, PydanticAI, and more
- Python SDK (`pip install agentclear`), Node SDK (`npm install @agentclear/sdk`), MCP Server
- Includes a trust & security engine with automated scanning and trust tiers

### Links
- [Website](https://agentclear.dev)
- [Documentation](https://agentclear.dev/docs)

</details>

"""

with open('README.md', 'r') as f:
    content = f.read()

# Find insertion point: after Agent4Rec's closing </details> tag, before AgentForge
marker = '</details>\n\n## [AgentForge]'
if marker in content:
    content = content.replace(marker, '</details>\n\n' + AGENTCLEAR_ENTRY + '## [AgentForge]')
    with open('README.md', 'w') as f:
        f.write(content)
    print("Successfully inserted AgentClear entry!")
else:
    print("ERROR: Could not find insertion marker!")
    exit(1)
