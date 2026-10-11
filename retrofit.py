#!/usr/bin/env python3
"""
Retrofit script for RPM Apps Lab Guide
- Adds 3 new Reference nav items to all existing HTML pages
- Wires CoModeler screenshot placeholders into 6 pages
- Applies Priority 3 sales language fixes
"""

import os
import re

DOCS_DIR = "/home/gstoa/.openclaw/workspace/projects/work/workshops/lab-guide/docs"

# Nav addition: 3 new pages to add after 18-facilitator.html in every page
NAV_OLD = '      <li><a class="nav-link" href="./18-facilitator.html">Facilitator Guide</a></li>\n    </ul>'
NAV_NEW_TEMPLATE = '      <li><a class="nav-link" href="./18-facilitator.html">Facilitator Guide</a></li>\n      <li><a class="nav-link{active_lim}" href="./limitations.html">Limitations Reference</a></li>\n      <li><a class="nav-link{active_pre}" href="./presales-demo.html">Pre-Sales Demo Playbook</a></li>\n      <li><a class="nav-link{active_road}" href="./roadmap.html">Roadmap Snapshot</a></li>\n    </ul>'

# Files already built with nav (skip)
SKIP_FILES = {"limitations.html", "presales-demo.html", "roadmap.html"}

# Screenshot placeholder HTML snippet
def ss_placeholder(label, description):
    return f'''      <div class="screenshot-placeholder">
        <div class="ss-icon">📸</div>
        <div class="ss-label">[SCREENSHOT NEEDED: {label}]</div>
        <div class="ss-desc">{description}</div>
      </div>'''

def update_nav(content, filename):
    """Add 3 new nav entries to a page."""
    active_lim = " active" if filename == "limitations.html" else ""
    active_pre = " active" if filename == "presales-demo.html" else ""
    active_road = " active" if filename == "roadmap.html" else ""
    nav_new = NAV_NEW_TEMPLATE.format(
        active_lim=active_lim,
        active_pre=active_pre,
        active_road=active_road,
    )
    if NAV_OLD in content:
        return content.replace(NAV_OLD, nav_new, 1)
    return content  # already updated or different structure

# ================================================================
# PRIORITY 3 — Sales Language Fixes
# ================================================================

def fix_01_spm_overview(content):
    """
    1. "Most mature, most robust app" → "Most-implemented app in the RPM suite"
    2. "T&Q is the best landing app" TSD banner tell step → rewrite as factual
    """
    # Fix 1: pillar card description
    content = content.replace(
        "The cornerstone of the RPM Apps suite. Covers territory design, hierarchy management, target allocation, quota setting, account assignment, and the rule engine. The most mature, most robust app in the portfolio — and the best landing use case for new SPM customers.",
        "The cornerstone of the RPM Apps suite. Covers territory design, hierarchy management, target allocation, quota setting, account assignment, and the rule engine. The most-implemented app in the RPM suite — and the most common starting point for new SPM engagements."
    )

    # Fix 2: TSD banner "why T&Q is the best landing app" → factual
    content = content.replace(
        "You'll learn the five SPM pillars, why T&amp;Q is the best landing app, and how to position the suite in a customer conversation.",
        "You'll learn the five SPM pillars, why T&amp;Q is the most common landing app, and what context helps position the suite in a customer conversation."
    )

    # Fix 3: callout-tip "T&Q is the best landing app in the RPM suite"
    content = content.replace(
        "<strong>T&amp;Q is the best landing app in the RPM suite</strong> — even for customers who think they don't have territory complexity. Almost every sales organization sets quotas, and almost every organization that sets quotas in Excel has significant pain. Start there. The other pillars become natural follow-ons once T&amp;Q is live and trusted.",
        "T&amp;Q is the most-implemented app in the RPM suite and the most common starting point for new SPM engagements. Almost every sales organization sets quotas, and organizations that manage quotas in Excel have consistent, well-documented pain. The other pillars become natural follow-ons once T&amp;Q is live and the customer trusts the data."
    )

    # Fix the pillar tag from "⭐ Best Landing App" to factual context
    content = content.replace(
        '<span class="pillar-tag">⭐ Best Landing App</span>',
        '<span class="pillar-tag">Most-Implemented App</span>'
    )

    return content


def fix_sf_01_overview(content):
    """Badge: 'Now GA 🎉' → 'GA — March 2026'"""
    content = content.replace(
        '<span class="content-badge">Now GA 🎉</span>',
        '<span class="content-badge">GA — March 2026</span>'
    )
    return content


def fix_cap_08_extensions(content):
    """
    Move 'holy grail / most powerful demo moment' framing to facilitator note;
    replace with factual description in the participant page.
    """
    old_tip = '''      <div class="callout-tip">
        <span class="callout-label">💡 Positioning Tip</span>
        <p>The most powerful Capacity demo moment is showing a VP of Sales Finance the "holy grail" page: "Hire 2 AEs in January, 3 in April — here's exactly when you close the revenue gap." Lead with that. Everything else is detail.</p>
      </div>'''
    new_tip = '''      <div class="callout-note">
        <span class="callout-label">📝 Revenue Projection Output</span>
        <p>The revenue projection page shows the month-by-month revenue contribution of a hiring plan, based on ramp profiles and hire dates. It answers: "If we hire these roles in these months, when does the revenue contribution kick in and does it close the gap to target?" This is the page most Sales Finance stakeholders focus on during a review.</p>
      </div>
      <div class="callout-tip" style="display:none"><!-- FACILITATOR NOTE: Lead the demo with the revenue projection page. Show a VP of Sales Finance two hiring scenarios — aggressive Q1 vs. conservative Q1 — and the difference in when they close their revenue gap. This is the moment that typically resonates most strongly with financial stakeholders. Keep this framing in facilitation; it's too prescriptive for the participant guide. --></div>'''
    content = content.replace(old_tip, new_tip)
    return content


# ================================================================
# PRIORITY 1 — CoModeler Screenshot Placeholders
# ================================================================

# For model review pages: add Show step content with placeholders
TQ_06_COMODELER_SECTION = '''
      <h2>CoModeler — What to Expect</h2>
      <p>Before running the CoModeler labs, familiarize yourself with the interface. CoModeler opens as a side panel within any Anaplan module. You type a natural language prompt, and CoModeler reads the model structure to generate a response.</p>

      <div class="callout-note">
        <span class="callout-label">📝 Access Note</span>
        <p>CoModeler access must be enabled by the Apps team for your workspace. Confirm access before the lab session. If you see the toolbar but CoModeler is greyed out, contact Chan or Jon to enable it.</p>
      </div>

      <h3>CoModeler Interface</h3>
''' + ss_placeholder(
    "CoModeler panel open in a T&Q module",
    "Show CoModeler side panel open alongside a T&Q module (e.g., SYS Territory Quota). The panel should show the prompt input field and the CoModeler icon highlighted in the toolbar. No suitable frame found in Day 2B recording — record from a live T&Q template app with CoModeler enabled."
) + '''

      <h3>Entering a Prompt</h3>
''' + ss_placeholder(
    "CoModeler prompt entry — typing a line item dictionary request",
    'Show the CoModeler panel with a prompt typed in: "Generate a line item dictionary for this module." Cursor should be in the input field. Record from the T&Q template app.'
) + '''

      <h3>Viewing CoModeler Output</h3>
''' + ss_placeholder(
    "CoModeler output — line item dictionary response for SYS Territory Quota",
    "Show CoModeler response listing line items with name, formula summary, data type, and purpose. Should show at least 5-6 line items from SYS Territory Quota."
) + '''

'''

SEG_06_COMODELER_SECTION = '''
      <h2>CoModeler — What to Expect</h2>
      <p>CoModeler opens as a side panel within any module. For the Segmentation model, it is especially useful for understanding the scoring formula logic — the relationships between scoring metrics and the final segment assignment are non-obvious from reading the module structure alone.</p>

      <div class="callout-note">
        <span class="callout-label">📝 Access Note</span>
        <p>CoModeler access must be enabled by the Apps team for your workspace. Confirm before the lab session.</p>
      </div>

      <h3>CoModeler Interface in Segmentation</h3>
''' + ss_placeholder(
    "CoModeler panel open in a Segmentation module (SG Account Scoring)",
    "Show CoModeler side panel open alongside the SG Account Scoring module. Panel shows prompt input field ready for input. No suitable frame in Day 2B recording — capture from live Segmentation demo app."
) + '''

      <h3>Entering a Prompt</h3>
''' + ss_placeholder(
    "CoModeler prompt entry — Segmentation scoring documentation request",
    'Show the prompt: "Generate a line item dictionary for this module. Include name, formula summary, and how each line item contributes to the final score."'
) + '''

      <h3>Viewing Output</h3>
''' + ss_placeholder(
    "CoModeler output — SG Account Scoring line item dictionary",
    "CoModeler response showing scoring metric line items with formula summaries. Should show how each metric weight contributes to the final score."
) + '''

'''

CAP_06_COMODELER_SECTION = '''
      <h2>CoModeler — What to Expect</h2>
      <p>CoModeler is particularly useful in the Capacity model because the ramp-to-revenue formula chains are longer and less obvious than in T&amp;Q or Segmentation. Use it to trace how a hire date in HC Hiring Plan propagates through ramp profiles to a revenue projection in HC Revenue Projection.</p>

      <div class="callout-note">
        <span class="callout-label">📝 Access Note</span>
        <p>CoModeler access must be enabled by the Apps team for your workspace. Confirm before the lab session.</p>
      </div>

      <h3>CoModeler Interface in Capacity</h3>
''' + ss_placeholder(
    "CoModeler panel open in a Capacity module (HC Hiring Plan)",
    "Show CoModeler side panel open alongside the HC Hiring Plan module. Panel shows the prompt input field ready. No suitable frame in Day 2B recording — capture from live Capacity demo app."
) + '''

      <h3>Entering a Prompt</h3>
''' + ss_placeholder(
    "CoModeler prompt entry — Capacity hiring plan documentation request",
    'Show the prompt: "Generate a line item dictionary for this module. Include name, formula summary, data type, and what downstream modules depend on each line item."'
) + '''

      <h3>Viewing Ramp-to-Revenue Output</h3>
''' + ss_placeholder(
    "CoModeler output — HC Hiring Plan line item dictionary showing ramp formula chain",
    "Response listing HC Hiring Plan line items, with special attention to how monthly new hire counts feed into ramp profile lookups and downstream revenue projection."
) + '''

'''

# For CoModeler lab pages: add Show step screenshots before the labs
def add_comodeler_show_tq07(content):
    """Add Show step screenshots before the labs in tq-07-comodeler-lab.html"""
    insert_after = '''      <div class="callout-note">
        <span class="callout-label">📝 Access</span>
        <p>CoModeler is available within Anaplan. Open any module in the app → look for the CoModeler icon in the toolbar. Complete Lab A before Lab B — Lab B builds on what you find in Lab A.</p>
      </div>'''
    show_block = '''

      <h2>What You'll See — CoModeler in T&amp;Q</h2>
      <p>The screenshots below show what CoModeler looks like when open in the T&amp;Q app. Familiarize yourself with the interface before starting Lab A.</p>

''' + ss_placeholder(
    "CoModeler panel open in T&Q SYS Territory Quota module",
    "Show CoModeler side panel alongside SYS Territory Quota. Prompt input field visible. Toolbar CoModeler icon highlighted. No live demo recorded — capture from T&Q template app with CoModeler enabled."
) + '''

''' + ss_placeholder(
    "CoModeler response — line item dictionary for SYS Territory Quota",
    "Show a CoModeler output listing quota calculation line items. Should show Base Target, Assignment %, Ramp Factor, and the output quota line item."
) + '''

''' + ss_placeholder(
    "CoModeler documentation output — formula explanation",
    "Show CoModeler explaining a formula in plain language — e.g., how Rep Quota = Base Target × Assignment % × Ramp Factor is calculated."
) + '''

'''
    return content.replace(insert_after, insert_after + show_block)


def add_comodeler_show_seg07(content):
    """Add Show step screenshots before the labs in seg-07-comodeler-lab.html"""
    insert_after = '''      <div class="callout-note">
        <span class="callout-label">📝 Access</span>
        <p>CoModeler is available within Anaplan. Open any module in the app → look for the CoModeler icon in the toolbar. Complete Lab A before Lab B — Lab B builds on what you find in Lab A.</p>
      </div>'''
    show_block = '''

      <h2>What You'll See — CoModeler in Segmentation</h2>
      <p>The screenshots below show what CoModeler looks like when open in the Segmentation app.</p>

''' + ss_placeholder(
    "CoModeler panel open in Segmentation SG Account Scoring module",
    "Show CoModeler side panel alongside SG Account Scoring. Prompt input field visible. No live demo recorded — capture from Segmentation demo app with CoModeler enabled."
) + '''

''' + ss_placeholder(
    "CoModeler output — SG Account Scoring dictionary showing weight contributions",
    "Show CoModeler listing scoring line items, showing how each metric weight combines to produce the final account score."
) + '''

'''
    return content.replace(insert_after, insert_after + show_block)


def add_comodeler_show_cap07(content):
    """Add Show step screenshots before the labs in cap-07-comodeler-lab.html"""
    insert_after = '''      <div class="callout-note">
        <span class="callout-label">📝 Access</span>
        <p>CoModeler is available within Anaplan. Open any module in the app → look for the CoModeler icon in the toolbar. Complete Lab A before Lab B — Lab B builds on what you find in Lab A.</p>
      </div>'''
    show_block = '''

      <h2>What You'll See — CoModeler in Capacity</h2>
      <p>The screenshots below show what CoModeler looks like when open in the Capacity app.</p>

''' + ss_placeholder(
    "CoModeler panel open in Capacity HC Hiring Plan module",
    "Show CoModeler side panel alongside HC Hiring Plan. Prompt input field visible. No live demo recorded — capture from Capacity demo app with CoModeler enabled."
) + '''

''' + ss_placeholder(
    "CoModeler output — HC Hiring Plan ramp formula explanation",
    "Show CoModeler explaining how a hire date and ramp profile combine to generate a revenue projection. Ramp month offsets should be visible in the explanation."
) + '''

'''
    return content.replace(insert_after, insert_after + show_block)


# ================================================================
# MAIN
# ================================================================

def process_file(filename, content):
    """Apply all transforms to a single file."""

    # Nav update for all existing pages
    if filename not in SKIP_FILES:
        content = update_nav(content, filename)

    # Priority 3 — Sales language
    if filename == "01-spm-overview.html":
        content = fix_01_spm_overview(content)
    elif filename == "sf-01-overview.html":
        content = fix_sf_01_overview(content)
    elif filename == "cap-08-extensions.html":
        content = fix_cap_08_extensions(content)

    # Priority 1 — CoModeler screenshots in model review pages
    if filename == "tq-06-model-review.html":
        # Insert before closing content-body
        content = content.replace(
            '      \n    </div>\n  </main>',
            TQ_06_COMODELER_SECTION + '    </div>\n  </main>'
        )
    elif filename == "seg-06-model-review.html":
        content = content.replace(
            '      \n    </div>\n  </main>',
            SEG_06_COMODELER_SECTION + '    </div>\n  </main>'
        )
    elif filename == "cap-06-model-review.html":
        content = content.replace(
            '      \n    </div>\n  </main>',
            CAP_06_COMODELER_SECTION + '    </div>\n  </main>'
        )

    # Priority 1 — CoModeler screenshots in lab pages
    if filename == "tq-07-comodeler-lab.html":
        content = add_comodeler_show_tq07(content)
    elif filename == "seg-07-comodeler-lab.html":
        content = add_comodeler_show_seg07(content)
    elif filename == "cap-07-comodeler-lab.html":
        content = add_comodeler_show_cap07(content)

    return content


def main():
    changed = []
    skipped = []
    
    for filename in sorted(os.listdir(DOCS_DIR)):
        if not filename.endswith(".html"):
            continue
        if filename in SKIP_FILES:
            skipped.append(filename)
            continue
            
        filepath = os.path.join(DOCS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        updated = process_file(filename, original)
        
        if updated != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(updated)
            changed.append(filename)
            print(f"  ✅ Updated: {filename}")
        else:
            print(f"  ⏭  Unchanged: {filename}")
    
    print(f"\nDone. Changed {len(changed)} files, skipped {len(skipped)} new files.")
    print(f"Changed: {changed}")


if __name__ == "__main__":
    main()
