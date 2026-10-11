#!/usr/bin/env python3
"""
Lab guide nav restructure script.
Parts 1-5: nav update, 00-overview update, new page creation, index update, verification.
"""

import os
import re

BASE = '/home/gstoa/.openclaw/workspace/projects/work/workshops/lab-guide'
DOCS = os.path.join(BASE, 'docs')

# ─────────────────────────────────────────────────────────────
# 1. NEW NAV BLOCK (for /docs/ pages — uses ./filename.html hrefs)
# ─────────────────────────────────────────────────────────────
NEW_NAV = '''  <nav class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-title">RPM Apps Lab Guide</div>
    </div>
    <ul class="nav-list">
      <li class="nav-section-title">Getting Started</li>
      <li><a class="nav-link" href="./00-overview.html">Workshop Overview</a></li>
      <li><a class="nav-link" href="./01-spm-overview.html">SPM/RPM Overview</a></li>
      <li><a class="nav-link" href="./02-anaplan-way.html">Anaplan Way for Apps</a></li>
      <li class="nav-section-title">Territory &amp; Quota</li>
      <li><a class="nav-link" href="./tq-01-overview.html">Functional Overview</a></li>
      <li><a class="nav-link" href="./tq-02-sample-data.html">Sample Data</a></li>
      <li><a class="nav-link" href="./03-configurator-walkthrough.html">Configurator Review</a></li>
      <li><a class="nav-link" href="./04-configurator-exercise.html">Lab: Configurator</a></li>
      <li><a class="nav-link" href="./05-post-gen-steps.html">Post-Generation Steps</a></li>
      <li><a class="nav-link" href="./tq-06-model-review.html">Model Review</a></li>
      <li><a class="nav-link" href="./07-spoke-app-walkthrough.html">Application Review</a></li>
      <li><a class="nav-link" href="./06-ado-integration.html">Data Integration &amp; ADO</a></li>
      <li><a class="nav-link" href="./08-extensions.html">Common Extensions</a></li>
      <li class="nav-section-title">Account Segmentation</li>
      <li><a class="nav-link" href="./seg-01-overview.html">Functional Overview</a></li>
      <li><a class="nav-link" href="./seg-02-sample-data.html">Sample Data</a></li>
      <li><a class="nav-link" href="./10-segmentation-configurator.html">Configurator Review</a></li>
      <li><a class="nav-link" href="./seg-04-lab.html">Lab: Configurator</a></li>
      <li><a class="nav-link" href="./seg-05-post-gen.html">Post-Generation Steps</a></li>
      <li><a class="nav-link" href="./seg-06-model-review.html">Model Review</a></li>
      <li><a class="nav-link" href="./13-segmentation-walkthrough.html">Application Review</a></li>
      <li><a class="nav-link" href="./seg-08-extensions.html">Common Extensions</a></li>
      <li class="nav-section-title">Capacity Planning</li>
      <li><a class="nav-link" href="./cap-01-overview.html">Functional Overview</a></li>
      <li><a class="nav-link" href="./cap-02-sample-data.html">Sample Data</a></li>
      <li><a class="nav-link" href="./11-capacity-configurator.html">Configurator Review</a></li>
      <li><a class="nav-link" href="./cap-04-lab.html">Lab: Configurator</a></li>
      <li><a class="nav-link" href="./cap-05-post-gen.html">Post-Generation Steps</a></li>
      <li><a class="nav-link" href="./cap-06-model-review.html">Model Review</a></li>
      <li><a class="nav-link" href="./14-capacity-walkthrough.html">Application Review</a></li>
      <li><a class="nav-link" href="./cap-08-extensions.html">Common Extensions</a></li>
      <li class="nav-section-title">Reference</li>
      <li><a class="nav-link" href="./15-whats-coming.html">What's Coming</a></li>
      <li><a class="nav-link" href="./16-qanda.html">Q&amp;A from Sessions</a></li>
      <li><a class="nav-link" href="./17-resources.html">Resources &amp; Downloads</a></li>
      <li><a class="nav-link" href="./tq-appendix-answer-key.html">T&amp;Q Answer Key</a></li>
      <li><a class="nav-link" href="./18-facilitator.html">Facilitator Guide</a></li>
    </ul>
    <div class="lang-switcher">
      <span class="lang-switcher-label">🌐 Language</span>
      <select id="lang-select" class="lang-select">
        <option value="en">🇺🇸 English</option>
        <option value="ja">🇯🇵 日本語</option>
        <option value="es">🇪🇸 Español</option>
        <option value="fr">🇫🇷 Français</option>
        <option value="de">🇩🇪 Deutsch</option>
        <option value="pt">🇧🇷 Português</option>
        <option value="ko">🇰🇷 한국어</option>
        <option value="zh">🇨🇳 中文</option>
      </select>
    </div>
  </nav>'''

# Same nav for index.html but with ./docs/ prefix
INDEX_NAV = NEW_NAV.replace('href="./', 'href="./docs/')

def inject_active(nav_html, filename):
    """Add 'active' class to the nav-link matching this file's own filename."""
    # For docs files: href="./filename.html"
    # For index: href="./docs/filename.html"
    # We search for the href containing the filename
    name = os.path.basename(filename)
    # Replace class="nav-link" href="./NAME" with class="nav-link active" href="./NAME"
    # (handles both ./name and ./docs/name)
    pattern = r'(class="nav-link")( href="(?:\./(?:docs/)?)'  + re.escape(name) + r'")'
    result = re.sub(pattern, r'class="nav-link active"\2', nav_html)
    return result

def replace_nav_in_file(filepath):
    """Replace the <nav class="sidebar">...</nav> block in an HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    is_index = (filename == 'index.html')
    nav_template = INDEX_NAV if is_index else NEW_NAV
    new_nav = inject_active(nav_template, filepath)
    
    # Replace the nav block
    new_content = re.sub(
        r'<nav class="sidebar">.*?</nav>',
        new_nav,
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'  ✅ Updated nav: {filename}')

# ─────────────────────────────────────────────────────────────
# PART 1: Update nav in all existing docs/*.html files
# ─────────────────────────────────────────────────────────────
print('\n=== PART 1: Updating nav in existing docs/*.html ===')
for fname in sorted(os.listdir(DOCS)):
    if fname.endswith('.html'):
        replace_nav_in_file(os.path.join(DOCS, fname))

print('\n=== PART 1: Updating nav in index.html ===')
replace_nav_in_file(os.path.join(BASE, 'index.html'))

# ─────────────────────────────────────────────────────────────
# PART 2: Update 00-overview.html — add "How the Apps Work Together"
# ─────────────────────────────────────────────────────────────
print('\n=== PART 2: Updating 00-overview.html ===')
OVERVIEW_PATH = os.path.join(DOCS, '00-overview.html')
with open(OVERVIEW_PATH, 'r', encoding='utf-8') as f:
    overview = f.read()

HOW_TOGETHER = '''      <h2>How the Apps Work Together</h2>
      <p>The three RPM apps — Territory &amp; Quota, Account Segmentation, and Capacity Planning — are designed to work together as a suite. Each module in this workshop covers one app, but understanding how data flows between them is essential before you start.</p>
      <div class="callout-note">
        <span class="callout-label">⚠ These connections are not automatic</span>
        <p>Data flows between apps require a manual export/import step today. Native app-to-app connections are on the roadmap. Plan for this in your project timelines.</p>
      </div>
      <div class="two-col">
        <div class="card">
          <h3>Segmentation → T&amp;Q</h3>
          <p>Account segments drive territory carving and Rule Engine logic. Export segments from Segmentation, import as an account attribute in T&amp;Q.</p>
        </div>
        <div class="card">
          <h3>Segmentation → Capacity</h3>
          <p>Account mix changes drive headcount needs. Segment counts feed directly into Capacity coverage ratios.</p>
        </div>
      </div>
      <div class="two-col">
        <div class="card">
          <h3>Capacity → T&amp;Q</h3>
          <p>TPH (territories per headcount) output from Capacity informs how many territories to design in T&amp;Q.</p>
        </div>
        <div class="card">
          <h3>Recommended Sequence</h3>
          <ol style="padding-left:1.2rem;font-size:0.9rem;">
            <li>Segmentation → finalize account segments</li>
            <li>Capacity → determine headcount by role/geo</li>
            <li>T&amp;Q → design territories informed by both</li>
          </ol>
        </div>
      </div>
'''

# Insert before closing </div> of content-body
if HOW_TOGETHER not in overview:
    # Find the last </div> before </main> 
    # The content-body div closes just before </main>
    overview = overview.replace(
        '\n    </div>\n  </main>',
        '\n' + HOW_TOGETHER + '\n    </div>\n  </main>',
        1  # only the last occurrence — do it once from the end
    )
    # Actually let's find the content-body closing div more precisely
    # Re-read and do it differently
    with open(OVERVIEW_PATH, 'r', encoding='utf-8') as f:
        overview = f.read()
    
    # Find position of last </div> before </main>
    main_end = overview.rfind('</main>')
    content_body_close = overview.rfind('</div>', 0, main_end)
    overview = overview[:content_body_close] + HOW_TOGETHER + '    </div>\n  </main>\n\n  <script src="../js/nav.js"></script>\n</body>\n</html>\n'
    # Actually that would clobber the script tag. Let me find the exact insertion point.
    with open(OVERVIEW_PATH, 'r', encoding='utf-8') as f:
        overview = f.read()
    
    # The content-body ends with </div> then </main>
    # Find "</div>\n  </main>"
    insert_marker = '    </div>\n  </main>'
    insert_pos = overview.rfind(insert_marker)
    if insert_pos != -1:
        overview = overview[:insert_pos] + HOW_TOGETHER + '    </div>\n  </main>' + overview[insert_pos + len(insert_marker):]
        with open(OVERVIEW_PATH, 'w', encoding='utf-8') as f:
            f.write(overview)
        print('  ✅ Added "How the Apps Work Together" section to 00-overview.html')
    else:
        print('  ⚠ Could not find insertion point in 00-overview.html')
else:
    print('  ℹ Section already present in 00-overview.html')

# ─────────────────────────────────────────────────────────────
# PART 3: Create all new pages
# ─────────────────────────────────────────────────────────────
print('\n=== PART 3: Creating new pages ===')

def make_page(filename, title, h1, subtitle, badges, content):
    """Build a full HTML page and write it to /docs/."""
    filepath = os.path.join(DOCS, filename)
    nav_html = inject_active(NEW_NAV, filepath)
    badge_html = ''.join(f'        <span class="content-badge">{b}</span>\n' for b in badges)
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — RPM Apps Lab Guide</title>
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>
  <div class="mobile-header">
    <button id="hamburger">☰</button>
    <span>RPM Apps Lab Guide</span>
  </div>

{nav_html}

  <main class="main-content">
    <div class="content-header">
      <h1>{h1}</h1>
      <p class="subtitle">{subtitle}</p>
      <div class="badge-row">
{badge_html}      </div>
    </div>
    <div class="content-body">
{content}
    </div>
  </main>

  <script src="../js/nav.js"></script>
</body>
</html>
'''
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  ✅ Created: {filename}')


# ── tq-01-overview.html ──────────────────────────────────────
make_page(
    'tq-01-overview.html',
    'T&Q Functional Overview',
    'Territory &amp; Quota (T&amp;Q)',
    'What the app does, who uses it, and what it produces',
    ['T&amp;Q Module', '15 min'],
    '''      <div class="tsd-banner">
        <div class="tsd-step tsd-step-tell">
          <span class="tsd-step-label">📖 Tell</span>
          <span class="tsd-step-heading">What T&amp;Q Does</span>
          <span class="tsd-step-desc">The app's core workflows, generated outputs, and the planning lifecycle it supports.</span>
        </div>
        <div class="tsd-step tsd-step-show">
          <span class="tsd-step-label">👁 Show</span>
          <span class="tsd-step-heading">Facilitator Demo</span>
          <span class="tsd-step-desc">Instructor opens the T&amp;Q template app and briefly tours the 8 app categories.</span>
        </div>
        <div class="tsd-step tsd-step-do">
          <span class="tsd-step-label">✅ Do</span>
          <span class="tsd-step-heading">Access the App</span>
          <span class="tsd-step-desc">Log into your partner workspace and locate the T&amp;Q V2 template app before the next section.</span>
        </div>
      </div>

      <h2>What T&amp;Q Produces</h2>
      <p>The T&amp;Q configurator generates a fully functional Anaplan application containing approximately <strong>8,000 objects</strong> — modules, line items, lists, dashboards, and actions — pre-configured to your customer's exact specifications. No model building required.</p>

      <div class="two-col">
        <div class="card">
          <h3>Core Outputs</h3>
          <ul>
            <li>Territory hierarchy (up to 5 tiers)</li>
            <li>Account-to-territory assignment engine</li>
            <li>Target allocation (top-down, Finance-driven)</li>
            <li>Quota calculation per rep per territory</li>
            <li>Approval workflow for targets and quotas</li>
            <li>Rep-facing quota acknowledgement</li>
          </ul>
        </div>
        <div class="card">
          <h3>Who Uses It</h3>
          <ul>
            <li><strong>Sales Ops:</strong> Territory design, account assignment, rep management</li>
            <li><strong>Finance:</strong> Target import and allocation</li>
            <li><strong>Sales Leadership:</strong> Target approval, quota review</li>
            <li><strong>Sales Reps:</strong> Quota acknowledgement, territory view</li>
            <li><strong>Admins:</strong> Data loads, new year initialization</li>
          </ul>
        </div>
      </div>

      <h2>The Planning Lifecycle</h2>
      <div class="step">
        <div class="step-badge">1</div>
        <div class="step-content"><strong>Territory Design</strong> — Build or update the territory hierarchy. Assign accounts to territories using manual assignment, geo mapping, or the Rule Engine.</div>
      </div>
      <div class="step">
        <div class="step-badge">2</div>
        <div class="step-content"><strong>Target Setting</strong> — Finance imports annual targets at the configured entry tier. Targets cascade down the hierarchy using the selected allocation method.</div>
      </div>
      <div class="step">
        <div class="step-badge">3</div>
        <div class="step-content"><strong>Resource Assignment</strong> — Assign reps to territories with effective dates, assignment percentages, and ramp profiles.</div>
      </div>
      <div class="step">
        <div class="step-badge">4</div>
        <div class="step-content"><strong>Quota Calculation</strong> — Quotas are calculated automatically: territory target × assignment % × ramp factor. Multi-territory reps are consolidated.</div>
      </div>
      <div class="step">
        <div class="step-badge">5</div>
        <div class="step-content"><strong>Approval &amp; Publish</strong> — Sales leaders approve targets level by level. Approved targets lock. Quotas export to CRM, ICM, and HR systems.</div>
      </div>

      <h2>Key Differentiators</h2>
      <div class="callout-tip">
        <span class="callout-label">💡 Why T&amp;Q First</span>
        <p>T&amp;Q is the best landing app in the RPM suite — clearest ROI story, fastest time to value, and the strongest foundation for the full SPM platform. Almost every sales org sets quotas. Almost every org that sets quotas in Excel is in pain. That's your opening.</p>
      </div>

      <div class="callout-do">
        <span class="callout-label">✅ Do — Access Check</span>
        <p>Before moving on, confirm you have access to the T&amp;Q V2 template app in your Anaplan partner workspace. Search for "V2" in your apps list. You'll use this throughout the T&amp;Q module.</p>
      </div>'''
)

# ── tq-02-sample-data.html ──────────────────────────────────────
make_page(
    'tq-02-sample-data.html',
    'T&Q Sample Data Structures',
    'T&amp;Q Sample Data Structures',
    'Required data objects, field schemas, and the CloudWorks exercise dataset',
    ['T&amp;Q Module', 'Reference'],
    '''      <p>T&amp;Q requires five core data objects. Understanding their structure before configuration sessions prevents the most common data-related delays. The <strong>Data Prep Workbook</strong> (available in Resources) contains templates for each object.</p>

      <h2>Required Data Objects</h2>

      <div class="table-wrap">
        <table>
          <thead><tr><th>Object</th><th>Purpose</th><th>Source</th><th>Critical Fields</th></tr></thead>
          <tbody>
            <tr><td><strong>Account</strong></td><td>The universe of accounts to be assigned to territories</td><td>CRM (Salesforce)</td><td>Account ID, Account Name, Account Parent, Territory, Segment, Industry, Employee Count, Lat/Long</td></tr>
            <tr><td><strong>Territory</strong></td><td>The hierarchy of territories (all tiers)</td><td>Manual / Sales Ops</td><td>Territory ID, Territory Name, Territory Parent, Tier level</td></tr>
            <tr><td><strong>Employee</strong></td><td>Sales reps and managers with role and assignment data</td><td>HR / CRM</td><td>User ID, User Name, Sales Role, Job Family, Hire Date, Source Territory, Manager, Is Active?</td></tr>
            <tr><td><strong>Opportunity / Order</strong></td><td>Historical actuals for allocation and reporting</td><td>CRM / ERP</td><td>Account ID, Amount, Planning Measure, Service Date, Territory</td></tr>
            <tr><td><strong>Finance Targets</strong></td><td>Top-down targets from Finance</td><td>Finance / FP&amp;A</td><td>Territory/Region, Planning Measure, Period, Amount</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Account File Schema</h2>
      <p>The most complex data object. Key fields used in the T&amp;Q configurator exercise:</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Field</th><th>Type</th><th>Required</th><th>Used For</th></tr></thead>
          <tbody>
            <tr><td>Account ID</td><td>Text (unique)</td><td>✅ Required</td><td>Primary key — links accounts to actuals, assignments</td></tr>
            <tr><td>Account Name</td><td>Text</td><td>✅ Required</td><td>Display name throughout the app</td></tr>
            <tr><td>Account Parent</td><td>Text (Account ID)</td><td>Recommended</td><td>Global Ultimate Parent hierarchy for named accounts</td></tr>
            <tr><td>Territory</td><td>Text (Territory ID)</td><td>Recommended</td><td>Pre-existing assignment import</td></tr>
            <tr><td>Industry</td><td>List</td><td>If using Rule Engine</td><td>Rule Engine attribute, segmentation</td></tr>
            <tr><td>No. of Employees</td><td>Number</td><td>If using Rule Engine</td><td>Rule Engine attribute (use banded version)</td></tr>
            <tr><td>Account Segment</td><td>List</td><td>If using Segmentation</td><td>Segment attribute from Segmentation app output</td></tr>
            <tr><td>Ship to Latitude</td><td>Decimal</td><td>If using Geo Mapping</td><td>Map card and lasso assignment</td></tr>
            <tr><td>Ship to Longitude</td><td>Decimal</td><td>If using Geo Mapping</td><td>Map card and lasso assignment</td></tr>
            <tr><td>ARR Spend</td><td>Currency</td><td>Recommended</td><td>Potential Spend — primary allocation method</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Territory File Schema</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Field</th><th>Type</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>Territory ID</td><td>Text (unique)</td><td>Primary key. Use a stable code (e.g. "S01") not a display name</td></tr>
            <tr><td>Territory Name</td><td>Text</td><td>Display name (e.g. "Northeast")</td></tr>
            <tr><td>Territory Parent</td><td>Text (Territory ID)</td><td>ID of the parent territory — defines the hierarchy rollup</td></tr>
            <tr><td>Territory Manager</td><td>Text (User ID)</td><td>Optional — the manager responsible for this territory</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout-warning">
        <span class="callout-label">⚠ V2 vs V3 Territory Format</span>
        <p><strong>V2:</strong> One flat file with all tiers as columns. <strong>V3 (ADO):</strong> One separate source view per hierarchy tier. If you're configuring V3, you need a separate file per tier — not one combined flat file.</p>
      </div>

      <h2>Employee File Schema</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Field</th><th>Type</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>User ID</td><td>Text (unique)</td><td>Primary key — must match the Anaplan user ID</td></tr>
            <tr><td>User Name</td><td>Text</td><td>Display name</td></tr>
            <tr><td>Sales Role</td><td>List</td><td>Must match the Sales Role list configured in the configurator</td></tr>
            <tr><td>Job Family</td><td>List</td><td>Role grouping for quota composition</td></tr>
            <tr><td>Source Territory</td><td>Text (Territory ID)</td><td>The territory this rep is assigned to at import time</td></tr>
            <tr><td>Hire Date</td><td>Date</td><td>Used for ramp calculation — must be accurate</td></tr>
            <tr><td>Is Active?</td><td>Boolean</td><td>Inactive reps are excluded from quota calculations</td></tr>
            <tr><td>Manager</td><td>Text (User ID)</td><td>Manager's User ID — used for approval routing</td></tr>
          </tbody>
        </table>
      </div>

      <h2>CloudWorks Exercise Dataset</h2>
      <p>The following files are provided in your lab workspace. These are the actual files used in the T&amp;Q configurator exercise.</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>File</th><th>Rows</th><th>Key Fields</th></tr></thead>
          <tbody>
            <tr><td><code>Configurator Exercise Account_Flat File.csv</code></td><td>~4,200</td><td>Account Name, Account ID, Industry, No. of Employees, Annual Revenue, Account Segment, Territory, Ship to Latitude/Longitude, ARR Spend</td></tr>
            <tr><td><code>Configurator Exercise Territory_Flat File.csv</code></td><td>~220</td><td>Territory Name, Territory ID, Territory Parent, Territory Manager</td></tr>
            <tr><td><code>Configurator Exercise Employee File.xlsx</code></td><td>~205</td><td>User ID, User Name, User Title, Sales Role, Job Family, Hire Date, Source Territory, Manager, Is Active?</td></tr>
            <tr><td><code>Configurator Exercise Opportunity line File.csv</code></td><td>~18,000</td><td>Opportunity Line ID, Account, Amount, Planning Measure, Service Date</td></tr>
          </tbody>
        </table>
      </div>

      <div class="callout-tip">
        <span class="callout-label">💡 Session Zero Tip</span>
        <p>Share the T&amp;Q Data Prep Workbook with the customer as early as possible — ideally before the SOW is signed. The workbook defines exactly what format each file needs to be in. Customers who complete it before kickoff move 2–3× faster through configuration sessions.</p>
      </div>'''
)

# ── tq-06-model-review.html ──────────────────────────────────────
make_page(
    'tq-06-model-review.html',
    'T&Q Model Review',
    'T&amp;Q Model Review',
    'Understanding the generated model structure using CoModeler',
    ['T&amp;Q Module', '45 min'],
    '''      <p>After generation, the T&amp;Q app contains approximately 8,000 Anaplan objects. You don't need to understand all of them — but you need to understand the key structural patterns before you can confidently implement, extend, or troubleshoot the app. CoModeler accelerates this significantly.</p>

      <h2>What is CoModeler?</h2>
      <p>CoModeler is Anaplan's AI-powered model documentation tool. It reads your model's structure and lets you ask natural language questions about it — generating line item dictionaries, explaining formula logic, mapping dependencies, and surfacing patterns you'd otherwise spend hours tracing manually.</p>

      <div class="callout-note">
        <span class="callout-label">📝 Access</span>
        <p>CoModeler is available within Anaplan. Navigate to your T&amp;Q template app → open any module → look for the CoModeler icon in the toolbar. You need the T&amp;Q V2 template app open in your partner workspace to complete these labs.</p>
      </div>

      <h2>Key T&amp;Q Modules to Know</h2>
      <p>Focus your review on these modules — they drive the core planning logic:</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Module</th><th>Purpose</th><th>Why It Matters</th></tr></thead>
          <tbody>
            <tr><td>SYS Territory Quota</td><td>Core quota calculation</td><td>Every quota value flows through here — understand it first</td></tr>
            <tr><td>SYS Resource Assignment</td><td>Rep-to-territory assignment with effective dates</td><td>Drives all downstream quota and target routing</td></tr>
            <tr><td>SYS Target Allocation</td><td>Top-down target cascade</td><td>Allocation methods, over-allocation, approval locking</td></tr>
            <tr><td>SYS Account Assignment</td><td>Account-to-territory mapping</td><td>Source of truth for which accounts belong to which territory</td></tr>
            <tr><td>DCA modules</td><td>Access control</td><td>Controls who can edit what — wrong DCA = broken approval flow</td></tr>
          </tbody>
        </table>
      </div>

      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">A</div>
          <div class="mini-lab-title">CoModeler Lab A — Generate a Line Item Dictionary</div>
          <div class="mini-lab-duration">⏱ 15 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Use CoModeler to generate a complete line item dictionary for the SYS Territory Quota module — the core quota calculation module in T&amp;Q.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Open the <strong>T&amp;Q V2 template app</strong> in your partner workspace.</li>
            <li><span class="mini-lab-step-num">2</span> Navigate to the <strong>SYS Territory Quota</strong> module (use the model map or search).</li>
            <li><span class="mini-lab-step-num">3</span> Open <strong>CoModeler</strong> for this module.</li>
            <li><span class="mini-lab-step-num">4</span> Prompt CoModeler: <em>"Generate a line item dictionary for this module. For each line item include: name, formula summary, data type, and purpose."</em></li>
            <li><span class="mini-lab-step-num">5</span> Review the output. Identify which line items calculate: (a) the base target, (b) the assignment percentage adjustment, and (c) the ramp factor adjustment.</li>
            <li><span class="mini-lab-step-num">6</span> Export or copy the dictionary — you'll use it as a reference during the extension exercise.</li>
          </ol>
          <div class="callout-tip" style="margin-top:0.75rem;">
            <span class="callout-label">💡 What to Look For</span>
            <p>The quota calculation follows this pattern: <strong>Base Target × Assignment % × Ramp Factor = Rep Quota</strong>. Find the line items that represent each of these three inputs and confirm you understand how they connect.</p>
          </div>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ Done when you can answer</div>
          <p style="font-size:0.88rem;color:#14532d;margin:0;">Which line item in SYS Territory Quota holds the final calculated quota value for a rep? What are its inputs?</p>
        </div>
      </div>

      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">C</div>
          <div class="mini-lab-title">CoModeler Lab C — Explain the Quota Calculation Logic</div>
          <div class="mini-lab-duration">⏱ 15 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Use CoModeler to understand exactly how quota is calculated for a rep who covers multiple territories with different assignment percentages.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> With the T&amp;Q template app open, launch <strong>CoModeler</strong>.</li>
            <li><span class="mini-lab-step-num">2</span> Ask: <em>"How does the quota calculation work when a single rep is assigned to multiple territories at different assignment percentages? Walk me through the formula logic step by step."</em></li>
            <li><span class="mini-lab-step-num">3</span> Read the explanation. Then ask a follow-up: <em>"Which module consolidates the quota across all territories for a single rep, and what is the output used for downstream systems like ICM?"</em></li>
            <li><span class="mini-lab-step-num">4</span> Note the module name that consolidates multi-territory quota (hint: it's the one you'd export to CRM/ICM).</li>
            <li><span class="mini-lab-step-num">5</span> Ask one more: <em>"If a rep has a ramp profile that starts at 0% in month 1 and reaches 100% in month 4, how does the app calculate their prorated annual quota?"</em></li>
          </ol>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ Done when you can answer</div>
          <p style="font-size:0.88rem;color:#14532d;margin:0;">What is the name of the module that holds the consolidated quota for a rep across all their territory assignments? Why does this matter for ICM integration?</p>
        </div>
      </div>

      <div class="callout-do">
        <span class="callout-label">✅ Do — Model Review Debrief</span>
        <p>After completing both CoModeler labs, discuss with your partner:</p>
        <ul>
          <li>What surprised you about the quota calculation? Was it more or less complex than you expected?</li>
          <li>How would you explain the quota formula to a Sales Ops stakeholder in plain language?</li>
          <li>Which module would you check first if a rep's quota looked wrong after generation?</li>
        </ul>
      </div>'''
)

# ── seg-01-overview.html ──────────────────────────────────────
make_page(
    'seg-01-overview.html',
    'Segmentation Functional Overview',
    'Account Segmentation &amp; Scoring',
    'What the app does, who uses it, and how it connects to T&amp;Q and Capacity',
    ['Segmentation Module', '15 min'],
    '''      <div class="tsd-banner">
        <div class="tsd-step tsd-step-tell">
          <span class="tsd-step-label">📖 Tell</span>
          <span class="tsd-step-heading">What Segmentation Does</span>
          <span class="tsd-step-desc">How the app classifies every account into a segment and feeds that data into T&amp;Q and Capacity.</span>
        </div>
        <div class="tsd-step tsd-step-show">
          <span class="tsd-step-label">👁 Show</span>
          <span class="tsd-step-heading">Facilitator Demo</span>
          <span class="tsd-step-desc">Instructor opens the Segmentation demo app and shows the rule-based segmentation flow end to end.</span>
        </div>
        <div class="tsd-step tsd-step-do">
          <span class="tsd-step-label">✅ Do</span>
          <span class="tsd-step-heading">Access the App</span>
          <span class="tsd-step-desc">Locate the Segmentation demo UX app in your partner workspace before the next section.</span>
        </div>
      </div>

      <h2>The Core Question</h2>
      <p>The Segmentation app answers one question: <strong>which segment does each account belong to, and why?</strong></p>
      <p>The answer drives everything downstream — territory carving in T&amp;Q, coverage ratios in Capacity, and wallet size calculations for target allocation. Getting segmentation right is a prerequisite for accurate planning across the entire RPM suite.</p>

      <div class="two-col">
        <div class="card">
          <h3>Core Outputs</h3>
          <ul>
            <li>Segment attribute per account (e.g. Strategic, Named, Commercial, SMB)</li>
            <li>Wallet size / addressable spend per account</li>
            <li>Segment inflow/outflow analysis (vs. prior segmentation)</li>
            <li>GTM hierarchy planning sandbox</li>
          </ul>
        </div>
        <div class="card">
          <h3>Two Segmentation Methods</h3>
          <ul>
            <li><strong>Rule-Based:</strong> Explicit conditions — if account matches attribute criteria, assign to segment. High precision for accounts that clearly fit a profile.</li>
            <li><strong>Score-Based:</strong> Numeric scoring model — every account gets a score that maps to a segment. Acts as catch-all for accounts that don't match any explicit rule.</li>
          </ul>
        </div>
      </div>

      <h2>Downstream Impact</h2>
      <div class="callout-note">
        <span class="callout-label">🔗 Connected to T&amp;Q and Capacity</span>
        <p>Segment outputs from this app flow directly into: <strong>T&amp;Q</strong> (as account attributes for territory carving and the Rule Engine) and <strong>Capacity</strong> (as account counts per segment driving coverage ratio calculations). Changing segmentation changes headcount requirements — the two are tightly linked.</p>
      </div>

      <div class="callout-do">
        <span class="callout-label">✅ Do — Access Check</span>
        <p>Locate the <strong>Segmentation Demo UX App</strong> in your Anaplan partner workspace. You'll follow along with this app during the Application Review section.</p>
      </div>'''
)

# ── seg-02-sample-data.html ──────────────────────────────────────
make_page(
    'seg-02-sample-data.html',
    'Segmentation Sample Data Structures',
    'Segmentation Sample Data Structures',
    'Required data objects and the CloudWorks exercise dataset',
    ['Segmentation Module', 'Reference'],
    '''      <p>Segmentation shares its core data objects with T&amp;Q — accounts, employees, opportunities, and territories. The key differences are the <strong>firmographic attributes</strong> required for scoring and the <strong>banded format</strong> needed for rule dimensions.</p>

      <h2>Required Data Objects</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Object</th><th>Purpose</th><th>Key Difference from T&amp;Q</th></tr></thead>
          <tbody>
            <tr><td><strong>Account</strong></td><td>Universe of accounts to be segmented</td><td>Requires firmographic data: Industry (list), Employee Band (list), Revenue Band (list), Annual Revenue (number)</td></tr>
            <tr><td><strong>Employee</strong></td><td>Sales reps — used for historical performance context</td><td>Same as T&amp;Q</td></tr>
            <tr><td><strong>Opportunity</strong></td><td>Historical performance data per account</td><td>Same as T&amp;Q</td></tr>
            <tr><td><strong>Territory</strong></td><td>Hierarchy for GTM planning sandbox</td><td>Same as T&amp;Q</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Critical: List-Formatted Attributes</h2>
      <div class="callout-important">
        <span class="callout-label">🚫 Raw Numbers Don't Work as Rule Dimensions</span>
        <p>The Segmentation rule engine only accepts <strong>list-formatted attributes</strong> as rule dimensions. Raw numeric fields (like Employee Count = 1,547) cannot be used directly. You must provide a <strong>banded version</strong> — a list attribute that maps the number to a band (e.g. Employee Band = "1,000–5,000"). Confirm this is in your account data before the configurator session.</p>
      </div>

      <h2>Firmographic Fields for CloudWorks</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Field</th><th>Format</th><th>Used For</th><th>Example Values</th></tr></thead>
          <tbody>
            <tr><td>Industry</td><td>List</td><td>Rule dimension, scoring metric</td><td>Technology, Financial Services, Healthcare, Manufacturing</td></tr>
            <tr><td>No. of Employees (raw)</td><td>Number</td><td>Source for banding</td><td>1547, 23000, 450</td></tr>
            <tr><td>Employee Band</td><td>List</td><td>Rule dimension</td><td>0–250, 250–1K, 1K–5K, 5K–25K, 25K+</td></tr>
            <tr><td>Annual Revenue (raw)</td><td>Currency</td><td>Source for banding, wallet size</td><td>$2.4M, $180M</td></tr>
            <tr><td>Revenue Band</td><td>List</td><td>Rule dimension</td><td>&lt;$10M, $10M–$100M, $100M–$1B, $1B+</td></tr>
            <tr><td>Account Segment</td><td>List</td><td>Output field — written by the app</td><td>Strategic, Named, Commercial, SMB</td></tr>
            <tr><td>ARR Spend</td><td>Currency</td><td>Wallet size input</td><td>Current ARR from Salesforce</td></tr>
          </tbody>
        </table>
      </div>

      <div class="callout-tip">
        <span class="callout-label">💡 Data Prep Tip</span>
        <p>If the customer's CRM only has raw employee count, you'll need to create the employee band as a derived field during data transformation. Build this into your Session Zero data assessment — ask: "Do you have a segment tier or size band already in your CRM, or will we need to derive it?"</p>
      </div>'''
)

# ── seg-04-lab.html ──────────────────────────────────────
# Content: copy Part 1 from 12-seg-cap-exercise.html + debrief questions
make_page(
    'seg-04-lab.html',
    'Lab: Segmentation Configurator',
    'Lab: Segmentation Configurator',
    'CloudWorks case study — Segmentation configurator exercise',
    ['Lab', '45 min', 'Hands-On'],
    '''      <h2>Exercise Overview</h2>
      <p>Using the <strong>CloudWorks case study</strong>, complete the Segmentation section of the configurator. Navigate to <strong>section 1A</strong> in the left nav of the configurator app.</p>
      <div class="callout-tip">After each configurator page, hit <strong>Apply / Calculate</strong> before moving on.</div>
      <hr>

      <h2>Part 1: Segmentation Configuration</h2>
      <p>Navigate to the <strong>Segmentation section</strong> of the configurator (section 1A in the left nav). Complete these mini-labs in order.</p>

      <!-- SEG MINI-LAB 1 -->
      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">S1</div>
          <div class="mini-lab-title">Data Setup — Page 1A.01</div>
          <div class="mini-lab-duration">⏱ 8 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Configure the account data attributes that will drive segmentation rules and scoring. Get this right — attributes must be list-formatted to work as rule dimensions.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Navigate to <strong>Page 1A.01: SG GTM Performance Analysis Guided Setup</strong>.</li>
            <li><span class="mini-lab-step-num">2</span> Review the CloudWorks account data: key firmographic fields are Industry, Employee Count, and Revenue Band.</li>
            <li><span class="mini-lab-step-num">3</span> Enable <strong>list-formatted attributes</strong> for: Industry, Employee Band, Revenue Band. Raw numeric fields (Employee Count) must be banded — confirm the banded version is enabled, not the raw number.</li>
            <li><span class="mini-lab-step-num">4</span> Enable <em>Enable for Calculate</em> for any attribute you plan to use in scoring.</li>
            <li><span class="mini-lab-step-num">5</span> Click <strong>Apply / Calculate</strong> before moving on.</li>
          </ol>
          <div class="callout-tip" style="margin-top:0.75rem;">
            <span class="callout-label">💡 Tip</span>
            <p>Numeric values (like raw employee count) cannot be used directly as rule dimensions — only list-formatted attributes work. Always use banded versions for segmentation rules.</p>
          </div>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ What it should look like when complete</div>
          <figure class="screenshot" style="margin:0;">
            <img src="../img/day2/10-seg-config-overview.png" alt="Segmentation configurator data setup — attributes configured" style="width:100%;border-radius:4px;border:1px solid #e2e8f0;">
            <figcaption style="font-size:0.78rem;color:#6b7280;margin-top:0.35rem;text-align:center;">Page 1A.01: Data setup — firmographic attributes configured and enabled for segmentation</figcaption>
          </figure>
        </div>
      </div>

      <!-- SEG MINI-LAB 2 -->
      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">S2</div>
          <div class="mini-lab-title">Rule-Based Segmentation — Page 1A.05</div>
          <div class="mini-lab-duration">⏱ 10 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Define the 4 CloudWorks segments and the account attributes that will serve as rule dimensions for explicit rule-based assignment.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Navigate to <strong>Page 1A.05: SG Segmentation Configuration Guided Setup</strong>.</li>
            <li><span class="mini-lab-step-num">2</span> Configure the segment list: <strong>Strategic, Named, Commercial, SMB</strong>.</li>
            <li><span class="mini-lab-step-num">3</span> Enable the following as rule dimensions: <strong>Industry, Employee Band, Revenue Band</strong>.</li>
            <li><span class="mini-lab-step-num">4</span> Enable Wallet Size Tier as a rule dimension if you completed the wallet size setup.</li>
            <li><span class="mini-lab-step-num">5</span> Click <strong>Apply / Calculate</strong>.</li>
          </ol>
          <div class="callout-tip" style="margin-top:0.75rem;">
            <span class="callout-label">💡 Tip</span>
            <p>Keep segments to 4 or fewer. Every extra segment multiplies complexity in T&amp;Q and Capacity — more territory types, more coverage ratios, more headcount rows.</p>
          </div>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ What it should look like when complete</div>
          <figure class="screenshot" style="margin:0;">
            <img src="../img/day2/10-seg-config-rules.png" alt="Segmentation configurator — 4 segments defined with rule dimensions" style="width:100%;border-radius:4px;border:1px solid #e2e8f0;">
            <figcaption style="font-size:0.78rem;color:#6b7280;margin-top:0.35rem;text-align:center;">Page 1A.05: 4 segments configured (Strategic, Named, Commercial, SMB) with rule dimensions enabled</figcaption>
          </figure>
        </div>
      </div>

      <!-- SEG MINI-LAB 3 -->
      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">S3</div>
          <div class="mini-lab-title">Score-Based Segmentation — Page 1A.05</div>
          <div class="mini-lab-duration">⏱ 10 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Configure the scoring model that assigns every account a numeric score — acting as a catch-all for accounts that don't match any explicit rule.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Scroll to the scoring section of <strong>Page 1A.05</strong>.</li>
            <li><span class="mini-lab-step-num">2</span> Configure scoring metrics using CloudWorks's account data. Suggested: Employee Band (40%), Revenue Band (35%), Industry (25%).</li>
            <li><span class="mini-lab-step-num">3</span> Verify <strong>weights sum to exactly 100%</strong> — the configurator will warn you if they don't.</li>
            <li><span class="mini-lab-step-num">4</span> Define score-to-segment thresholds: 7–10 = Strategic, 5–7 = Named, 3–5 = Commercial, 0–3 = SMB.</li>
            <li><span class="mini-lab-step-num">5</span> Click <strong>Apply / Calculate</strong>.</li>
          </ol>
          <div class="callout-note" style="margin-top:0.75rem;">
            <span class="callout-label">📝 Note</span>
            <p>Score-based acts as the default — every account gets a score and therefore a segment. Rule-based overrides the score for accounts that explicitly match your defined conditions. Use both.</p>
          </div>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ What it should look like when complete</div>
          <figure class="screenshot" style="margin:0;">
            <img src="../img/day2/13-seg-score-based.png" alt="Score-based segmentation — metrics, weights, and segment thresholds configured" style="width:100%;border-radius:4px;border:1px solid #e2e8f0;">
            <figcaption style="font-size:0.78rem;color:#6b7280;margin-top:0.35rem;text-align:center;">Score-based segmentation — scoring metrics with weights summing to 100% and score-to-segment thresholds</figcaption>
          </figure>
        </div>
      </div>

      <!-- SEG MINI-LAB 4 -->
      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">S4</div>
          <div class="mini-lab-title">Wallet Size — Page 1A.03</div>
          <div class="mini-lab-duration">⏱ 8 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Configure the wallet size model that estimates total addressable spend per account. CloudWorks uses the Revenue method. This feeds directly into T&amp;Q as the default target allocation metric.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Navigate to <strong>Page 1A.03: SG Wallet Size Calculation Guided Setup</strong>.</li>
            <li><span class="mini-lab-step-num">2</span> Select <strong>Revenue method</strong> for wallet size calculation.</li>
            <li><span class="mini-lab-step-num">3</span> Set addressable market % assumptions by industry using the CloudWorks case study data.</li>
            <li><span class="mini-lab-step-num">4</span> Configure geo index if prompted — use 1.0 (neutral) for all regions for this exercise.</li>
            <li><span class="mini-lab-step-num">5</span> Click <strong>Apply / Calculate</strong>.</li>
          </ol>
          <div class="callout-note" style="margin-top:0.75rem;">
            <span class="callout-label">📝 Note</span>
            <p>Wallet size is optional. If a customer doesn't have reliable firmographic data, skip it. Don't over-engineer a model the customer won't trust or maintain.</p>
          </div>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ What it should look like when complete</div>
          <figure class="screenshot" style="margin:0;">
            <img src="../img/configurator/seg-wallet-size.png" alt="Wallet Size configuration — Revenue method selected with spending assumptions" style="width:100%;border-radius:4px;border:1px solid #e2e8f0;">
            <figcaption style="font-size:0.78rem;color:#6b7280;margin-top:0.35rem;text-align:center;">Page 1A.03: Wallet Size Calculation — Revenue method with spending calculation and wallet calculation drivers configured</figcaption>
          </figure>
        </div>
      </div>

      <hr>

      <h2>Debrief Questions — Segmentation</h2>
      <ol>
        <li>You configured 4 segments for CloudWorks (Strategic, Named, Commercial, SMB). A customer pushes back and says they want 8 segments. How do you respond? What's the downstream impact?</li>
        <li>The scoring weights must sum to 100%. You assigned weights to 3 metrics. A 4th stakeholder now wants to add "recent growth rate" as a scoring factor. How does this change your weights, and what data would you need?</li>
        <li>What would happen if 30% of CloudWorks's accounts had missing employee count data — a field you relied on for both rule-based and score-based segmentation? What's your mitigation plan?</li>
        <li>A customer says: "We already have segments in Salesforce — why do we need the Segmentation app?" How do you answer?</li>
      </ol>'''
)

# ── seg-05-post-gen.html ──────────────────────────────────────
make_page(
    'seg-05-post-gen.html',
    'Segmentation Post-Generation Steps',
    'Segmentation Post-Generation Steps',
    'From generation to a working Segmentation app',
    ['Segmentation Module', '30 min'],
    '''      <p>Segmentation post-gen is significantly simpler than T&amp;Q. The app is smaller (~40% the complexity) and has fewer formula errors. Estimated hands-on work: <strong>4–6 hours</strong> with clean data.</p>

      <h2>Key Differences from T&amp;Q Post-Gen</h2>
      <div class="two-col">
        <div class="card">
          <h3>Simpler</h3>
          <ul>
            <li>Fewer generated modules and dashboards</li>
            <li>No approval workflow to configure</li>
            <li>No quota calculation logic to validate</li>
            <li>Data load is primarily account + firmographic data</li>
          </ul>
        </div>
        <div class="card">
          <h3>Watch Out For</h3>
          <ul>
            <li>Banded attribute mapping — ensure bands load correctly</li>
            <li>Wallet size calculation validation — spot-check against manual calculation</li>
            <li>Segment distribution check — are the right % of accounts in each segment?</li>
            <li>GTM hierarchy sandbox initialization</li>
          </ul>
        </div>
      </div>

      <h2>Post-Gen Checklist</h2>
      <ul class="checklist">
        <li>Review generation error log — count errors (0–50 is normal for Segmentation)</li>
        <li>Fix any formula reference errors in the Segmentation spoke</li>
        <li>Load account data with firmographic attributes</li>
        <li>Validate banded attributes loaded correctly (spot-check 5–10 accounts)</li>
        <li>Run initial segmentation calculation</li>
        <li>Review segment distribution — Strategic %, Named %, Commercial %, SMB %</li>
        <li>Validate wallet size calculations against a manual spot-check</li>
        <li>Confirm segment inflow/outflow view shows expected changes</li>
        <li>Initialize GTM hierarchy planning sandbox</li>
        <li>Demo app to customer with their own accounts</li>
      </ul>

      <div class="callout-do">
        <span class="callout-label">✅ Do — Segment Distribution Check</span>
        <p>After running the initial segmentation on CloudWorks data: What percentage of accounts fall into each segment? Is the Strategic count realistic (typically 1–5% of total accounts)? If you see 40% Strategic, your rules or scoring thresholds need recalibration.</p>
      </div>'''
)

# ── seg-06-model-review.html ──────────────────────────────────────
make_page(
    'seg-06-model-review.html',
    'Segmentation Model Review',
    'Segmentation Model Review',
    'Understanding the generated Segmentation model using CoModeler',
    ['Segmentation Module', '30 min'],
    '''      <p>The Segmentation app is smaller than T&amp;Q but contains some nuanced scoring logic that benefits from CoModeler exploration. Focus on the scoring and segment assignment modules.</p>

      <h2>Key Segmentation Modules</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Module</th><th>Purpose</th></tr></thead>
          <tbody>
            <tr><td>SG Account Scoring</td><td>Calculates the numeric score for each account based on weighted metrics</td></tr>
            <tr><td>SG Segmentation Rules</td><td>Rule-based segment assignment — explicit conditions per segment</td></tr>
            <tr><td>SG Final Segment</td><td>Combines rule-based and score-based to produce the final segment output</td></tr>
            <tr><td>SG Wallet Size</td><td>Calculates addressable spend per account using the configured method</td></tr>
          </tbody>
        </table>
      </div>

      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">A</div>
          <div class="mini-lab-title">CoModeler Lab A — Document the Account Scoring Module</div>
          <div class="mini-lab-duration">⏱ 15 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Generate a line item dictionary for the SG Account Scoring module to understand how each scoring metric contributes to the final account score.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Open the <strong>Segmentation demo app</strong> in your partner workspace.</li>
            <li><span class="mini-lab-step-num">2</span> Navigate to the <strong>SG Account Scoring</strong> module.</li>
            <li><span class="mini-lab-step-num">3</span> Open CoModeler and prompt: <em>"Generate a line item dictionary for this module. Include name, formula summary, and how each line item contributes to the final score."</em></li>
            <li><span class="mini-lab-step-num">4</span> Identify which line item holds the final weighted score and which holds the segment assignment derived from that score.</li>
          </ol>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ Done when you can answer</div>
          <p style="font-size:0.88rem;color:#14532d;margin:0;">How does the app decide whether rule-based or score-based takes precedence when both apply to the same account?</p>
        </div>
      </div>

      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">C</div>
          <div class="mini-lab-title">CoModeler Lab C — Explain the Score-to-Segment Mapping</div>
          <div class="mini-lab-duration">⏱ 15 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Use CoModeler to understand the exact logic that converts a numeric score (0–10) into a segment assignment.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Launch CoModeler in the Segmentation app.</li>
            <li><span class="mini-lab-step-num">2</span> Ask: <em>"How does the app map a numeric score to a segment? Walk me through the formula logic that converts a score of 7.2 to the 'Named' segment."</em></li>
            <li><span class="mini-lab-step-num">3</span> Follow up: <em>"If I want to change the threshold so that accounts scoring above 8 are Strategic instead of 7, which line item or admin setting do I change?"</em></li>
          </ol>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ Done when you can answer</div>
          <p style="font-size:0.88rem;color:#14532d;margin:0;">Where in the Segmentation app does an admin change the score thresholds without requiring a re-generation?</p>
        </div>
      </div>'''
)

# ── seg-08-extensions.html ──────────────────────────────────────
make_page(
    'seg-08-extensions.html',
    'Segmentation Common Extensions',
    'Segmentation Common Extensions',
    'Typical customizations and how to scope them',
    ['Segmentation Module', 'Reference'],
    '''      <p>Segmentation has fewer extensions than T&amp;Q, but several come up consistently. Most involve adding scoring dimensions, customizing segment definitions, or enhancing the GTM planning sandbox.</p>

      <div class="table-wrap">
        <table>
          <thead><tr><th>Extension</th><th>Size</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>Custom Scoring Dimensions</td><td>S</td><td>Adding a scoring metric not in the base app (e.g. "number of products purchased"). Requires a new attribute in the account data and a new scoring line item. Small effort, high value for customers with differentiated scoring criteria.</td></tr>
            <tr><td>Additional Segments</td><td>S–M</td><td>The base app supports a configurable number of segments. Adding segments post-gen requires updating segment lists, rules, thresholds, and dashboards. Challenge: every extra segment adds complexity in T&amp;Q and Capacity — push back to 4 or fewer.</td></tr>
            <tr><td>Custom Wallet Size Method</td><td>M</td><td>When none of the three built-in methods (OpEx, Employee, Revenue) fits the customer's TAM model. Requires a net-new calculation module. Common for SaaS companies with usage-based pricing models.</td></tr>
            <tr><td>Segment Override Workflow</td><td>M</td><td>Allows sales reps or managers to request a segment override for specific accounts, with approval. The base app allows admin overrides; this adds a structured request/approve workflow.</td></tr>
            <tr><td>T&amp;Q Integration Automation</td><td>S</td><td>The segment-to-T&amp;Q data flow is currently manual export/import. Adding a scheduled ADO pipeline or action to automate the transfer. Small effort once ADO is set up, high operational value.</td></tr>
            <tr><td>Enhanced GTM Hierarchy Reporting</td><td>M</td><td>Custom dashboards showing hierarchy balance (accounts per territory, wallet size distribution) before committing the new structure to T&amp;Q. V2 improves this significantly out of the box.</td></tr>
          </tbody>
        </table>
      </div>

      <div class="callout-tip">
        <span class="callout-label">💡 Positioning Tip</span>
        <p>The most common objection to the Segmentation app: "We already have segments in Salesforce." Your response: "Great — let's import those as the starting point. The Segmentation app gives you a governed, data-driven process to review and refine those segments every year, and feeds the output automatically into your territory and headcount planning." That's the value-add.</p>
      </div>'''
)

# ── cap-01-overview.html ──────────────────────────────────────
make_page(
    'cap-01-overview.html',
    'Capacity Planning Functional Overview',
    'Go-to-Market Capacity Planning',
    'What the app does, who uses it, and the hiring plan it produces',
    ['Capacity Module', '15 min'],
    '''      <div class="tsd-banner">
        <div class="tsd-step tsd-step-tell">
          <span class="tsd-step-label">📖 Tell</span>
          <span class="tsd-step-heading">What Capacity Does</span>
          <span class="tsd-step-desc">How the app answers "how many people do I need to hire, when, and where" — from finance guardrails to tactical hiring plans.</span>
        </div>
        <div class="tsd-step tsd-step-show">
          <span class="tsd-step-label">👁 Show</span>
          <span class="tsd-step-heading">Facilitator Demo</span>
          <span class="tsd-step-desc">Instructor opens the Capacity demo app and shows the tops-down → bottoms-up hiring plan flow.</span>
        </div>
        <div class="tsd-step tsd-step-do">
          <span class="tsd-step-label">✅ Do</span>
          <span class="tsd-step-heading">Access the App</span>
          <span class="tsd-step-desc">Locate the Capacity UX Demo App in your partner workspace before the next section.</span>
        </div>
      </div>

      <h2>The Core Question</h2>
      <p>The Capacity app answers: <strong>how many people do I need to hire, when, and where, to hit my revenue target?</strong></p>
      <p>It combines finance-driven guardrails (tops-down) with tactical field planning (bottoms-up), connected through ramp profiles that model when each new hire actually starts contributing revenue.</p>

      <div class="two-col">
        <div class="card">
          <h3>Core Outputs</h3>
          <ul>
            <li>Month-by-month hiring plan by role and geography</li>
            <li>Revenue coverage gap analysis (target vs. projected output)</li>
            <li>NTE (Not-to-Exceed) guardrails per geo/role</li>
            <li>Cost analysis — payback period per hire</li>
            <li>AOP snapshot for in-year plan vs. actual comparison</li>
          </ul>
        </div>
        <div class="card">
          <h3>Who Uses It</h3>
          <ul>
            <li><strong>Finance:</strong> Set tops-down NTE guardrails, revenue targets</li>
            <li><strong>Sales Leadership:</strong> Review suggested headcount, approve budgets</li>
            <li><strong>Sales Ops / HR:</strong> Enter bottoms-up hiring plans by month</li>
            <li><strong>RevOps:</strong> Scenario modeling, cost analysis</li>
          </ul>
        </div>
      </div>

      <h2>The Two Planning Layers</h2>
      <div class="step">
        <div class="step-badge">1</div>
        <div class="step-content"><strong>Tops-Down (Finance)</strong> — Finance sets a revenue target and budget. The app calculates suggested headcount by role based on coverage ratios and productivity assumptions. Finance sets NTE ceilings per geo and role family.</div>
      </div>
      <div class="step">
        <div class="step-badge">2</div>
        <div class="step-content"><strong>Bottoms-Up (Field)</strong> — Planners enter the actual month-by-month hiring plan. The model calculates projected revenue contribution factoring in ramp profiles. The "holy grail" page shows: hire X people on Y dates → here's when you close the gap to target.</div>
      </div>

      <div class="callout-important">
        <span class="callout-label">⚠ Start Simple</span>
        <p>When Anaplan used this tool internally, even their own team found the full app too complex with all features enabled. Start with the minimum configuration to answer the core question. Add complexity only when there's demonstrated demand for it.</p>
      </div>

      <div class="callout-do">
        <span class="callout-label">✅ Do — Access Check</span>
        <p>Locate the <strong>Capacity UX Demo App</strong> in your Anaplan partner workspace. Always check the workflow status (top right) before making changes — locked scenarios can't be edited.</p>
      </div>'''
)

# ── cap-02-sample-data.html ──────────────────────────────────────
make_page(
    'cap-02-sample-data.html',
    'Capacity Planning Sample Data Structures',
    'Capacity Planning Sample Data Structures',
    'Required data objects and role hierarchy setup',
    ['Capacity Module', 'Reference'],
    '''      <p>Capacity shares most of its data objects with T&amp;Q and Segmentation. The key additions are <strong>role hierarchy data</strong> (Job Family, Job Family Group, Sales Role) and <strong>productivity / ramp profile inputs</strong>.</p>

      <h2>Required Data Objects</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Object</th><th>Purpose</th><th>Key Difference from T&amp;Q</th></tr></thead>
          <tbody>
            <tr><td><strong>Employee</strong></td><td>Headcount data including role hierarchy</td><td>Requires Job Family, Job Family Group, and Sales Role — must match the hierarchy configured in the Capacity configurator</td></tr>
            <tr><td><strong>Account</strong></td><td>Account counts per segment per geo (from Segmentation output)</td><td>Segment attribute required — drives coverage ratio calculations</td></tr>
            <tr><td><strong>Territory</strong></td><td>Geo hierarchy for tops-down and bottoms-up planning</td><td>Same structure as T&amp;Q</td></tr>
            <tr><td><strong>Position</strong></td><td>Open headcount positions (optional)</td><td>New in Capacity — links to Anaplan Workforce Planning (OWP) if used</td></tr>
            <tr><td><strong>Job Family</strong></td><td>Role grouping hierarchy</td><td>New in Capacity — defines the 2–3 level role hierarchy</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Role Hierarchy Setup</h2>
      <p>Capacity requires a structured role hierarchy. This is one of the most important data design decisions — get it wrong and you'll need to reconfigure:</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Level</th><th>Example Values</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>Job Family Group (L1)</td><td>Core, Support</td><td>Highest level — typically separates revenue-generating from support roles</td></tr>
            <tr><td>Job Family (L2)</td><td>AE, CS, Pre-Sales, Management</td><td>Groups related roles</td></tr>
            <tr><td>Sales Role (L3)</td><td>Strategic AE, Commercial AE, SMB AE, CSM, PSE, Regional Manager</td><td>The level at which coverage ratios and ramp profiles are defined</td></tr>
          </tbody>
        </table>
      </div>

      <div class="callout-warning">
        <span class="callout-label">⚠ Do Not Enable Role Grade Unless Needed</span>
        <p>Role grade (P1–P5 or similar) adds a 4th level to the hierarchy. Every grade multiplies the number of rows in every coverage, productivity, and hiring table. Challenge this requirement hard before enabling it.</p>
      </div>

      <h2>Ramp Profile Inputs</h2>
      <p>Ramp profiles are the foundation of all productivity calculations. You need to agree on these with the customer before or during the configurator session:</p>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Sales Role</th><th>Month 1</th><th>Month 2</th><th>Month 3</th><th>Month 4</th><th>Month 5+</th></tr></thead>
          <tbody>
            <tr><td>Strategic AE (example)</td><td>0%</td><td>20%</td><td>50%</td><td>75%</td><td>100%</td></tr>
            <tr><td>Commercial AE (example)</td><td>0%</td><td>30%</td><td>70%</td><td>100%</td><td>100%</td></tr>
            <tr><td>SMB AE (example)</td><td>20%</td><td>60%</td><td>100%</td><td>100%</td><td>100%</td></tr>
          </tbody>
        </table>
      </div>
      <div class="callout-tip">
        <span class="callout-label">💡 Hire Date Rule</span>
        <p>Hired in the first half of the month → ramp starts that month. Hired in the second half → ramp starts next month. Make sure the customer understands this rule before they start entering hiring dates — it has material impact on projected revenue output.</p>
      </div>'''
)

# ── cap-04-lab.html ──────────────────────────────────────
make_page(
    'cap-04-lab.html',
    'Lab: Capacity Configurator',
    'Lab: Capacity Configurator',
    'CloudWorks case study — Capacity configurator exercise',
    ['Lab', '45 min', 'Hands-On'],
    '''      <h2>Exercise Overview</h2>
      <p>Using the <strong>CloudWorks case study</strong>, complete the Capacity section of the configurator. Navigate to <strong>section 1.2</strong> in the left nav of the configurator app.</p>
      <div class="callout-tip">After each configurator page, hit <strong>Apply / Calculate</strong> before moving on. If you already completed the Segmentation exercise, data setup is shared — skip it here.</div>
      <hr>

      <h2>Part 2: Capacity Configuration</h2>
      <p>Navigate to the <strong>Capacity section</strong> (section 1.2 in the left nav). Data setup is shared with Segmentation — skip it if you already configured it above.</p>

      <!-- CAP MINI-LAB 1 -->
      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">C1</div>
          <div class="mini-lab-title">Role Hierarchy — Page 1.2.x</div>
          <div class="mini-lab-duration">⏱ 8 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Define CloudWorks's sales role hierarchy — the structure that determines how headcount is planned and reported.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Navigate to the role hierarchy page in <strong>section 1.2</strong> of the configurator.</li>
            <li><span class="mini-lab-step-num">2</span> Configure <strong>3 levels</strong>: Job Family Group → Job Family → Sales Role.</li>
            <li><span class="mini-lab-step-num">3</span> Job Family Groups: <strong>Core, Support</strong>.</li>
            <li><span class="mini-lab-step-num">4</span> Job Families: <strong>AE, CS, Pre-Sales, Management</strong>.</li>
            <li><span class="mini-lab-step-num">5</span> Sales Roles: <strong>Strategic AE, Commercial AE, SMB AE, Customer Success Manager, Pre-Sales Engineer, Regional Manager</strong>.</li>
            <li><span class="mini-lab-step-num">6</span> <strong>Do NOT enable role grade</strong> — not needed for CloudWorks and adds unnecessary complexity.</li>
            <li><span class="mini-lab-step-num">7</span> Click <strong>Apply / Calculate</strong>.</li>
          </ol>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ What it should look like when complete</div>
          <figure class="screenshot" style="margin:0;">
            <img src="../img/day2/11-cap-config-overview.png" alt="Capacity configurator — role hierarchy configured" style="width:100%;border-radius:4px;border:1px solid #e2e8f0;">
            <figcaption style="font-size:0.78rem;color:#6b7280;margin-top:0.35rem;text-align:center;">Capacity configurator: role hierarchy — Job Family Group → Job Family → Sales Role, 3 levels, no role grade</figcaption>
          </figure>
        </div>
      </div>

      <!-- CAP MINI-LAB 2 -->
      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">C2</div>
          <div class="mini-lab-title">Coverage &amp; Workload — Page 1.2.3</div>
          <div class="mini-lab-duration">⏱ 10 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Define how roles cover accounts — the fundamental input for calculating how many people CloudWorks needs.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Navigate to <strong>Page 1.2.3: GTM Coverage &amp; Workload Capacity Guided Setup</strong>.</li>
            <li><span class="mini-lab-step-num">2</span> Configure coverage at the <strong>Americas level</strong>.</li>
            <li><span class="mini-lab-step-num">3</span> Set account-based coverage ratios: Strategic AE → 1:5 accounts (Strategic + Named), Commercial AE → 1:30 (Commercial), SMB AE → 1:100 (SMB).</li>
            <li><span class="mini-lab-step-num">4</span> Map derived coverage for overlay roles: 1 Pre-Sales generalist per 8 AEs, 1 Regional Manager per 10 AEs.</li>
            <li><span class="mini-lab-step-num">5</span> Click <strong>Apply / Calculate</strong>.</li>
          </ol>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ What it should look like when complete</div>
          <figure class="screenshot" style="margin:0;">
            <img src="../img/day2/11-cap-config-coverage.png" alt="Coverage and workload — role-to-segment mapping and coverage ratios configured" style="width:100%;border-radius:4px;border:1px solid #e2e8f0;">
            <figcaption style="font-size:0.78rem;color:#6b7280;margin-top:0.35rem;text-align:center;">Page 1.2.3: Coverage &amp; Workload — role coverage ratios and segment mapping configured</figcaption>
          </figure>
        </div>
      </div>

      <!-- CAP MINI-LAB 3 -->
      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">C3</div>
          <div class="mini-lab-title">Revenue Target Dimensions — Page 1.2.x</div>
          <div class="mini-lab-duration">⏱ 8 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Define the dimensionality of revenue targets — how Finance provides the numbers that drive tops-down planning.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Navigate to the Revenue Target configuration page in section 1.2.</li>
            <li><span class="mini-lab-step-num">2</span> Set target level → <strong>Sub-region</strong> (CloudWorks Finance provides targets at the sub-region level).</li>
            <li><span class="mini-lab-step-num">3</span> Enable <strong>by account segment</strong> dimensionality (targets are broken down by Strategic/Named/Commercial/SMB).</li>
            <li><span class="mini-lab-step-num">4</span> Click <strong>Apply / Calculate</strong>.</li>
          </ol>
          <div class="callout-warning" style="margin-top:0.75rem;">
            <span class="callout-label">⚠ Flag for Post-Gen</span>
            <p>Sub-region + account segment dimensionality requires post-generation routing work to connect the productivity model to the target properly. Note this as a post-gen task before moving on.</p>
          </div>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ What it should look like when complete</div>
          <figure class="screenshot" style="margin:0;">
            <img src="../img/configurator/cap-headcount-data.png" alt="Capacity configurator — headcount data and revenue target dimensions configured" style="width:100%;border-radius:4px;border:1px solid #e2e8f0;">
            <figcaption style="font-size:0.78rem;color:#6b7280;margin-top:0.35rem;text-align:center;">Revenue target configuration — sub-region level with account segment dimensionality</figcaption>
          </figure>
        </div>
      </div>

      <!-- CAP MINI-LAB 4 -->
      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">C4</div>
          <div class="mini-lab-title">Tops-Down Planning — Page 1.2.2</div>
          <div class="mini-lab-duration">⏱ 8 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Configure the guardrail structure for finance-driven headcount planning — the NTE ceiling that constrains all bottoms-up plans.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Navigate to <strong>Page 1.2.2: GTM Top-Down HC Target Setting Guided Setup</strong>.</li>
            <li><span class="mini-lab-step-num">2</span> Set tops-down planning level → <strong>Americas</strong> (all Americas as the top-level guardrail).</li>
            <li><span class="mini-lab-step-num">3</span> Configure <strong>2 scenarios</strong>: Base and Conservative.</li>
            <li><span class="mini-lab-step-num">4</span> Click <strong>Apply / Calculate</strong>.</li>
          </ol>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ What it should look like when complete</div>
          <figure class="screenshot" style="margin:0;">
            <img src="../img/day2/14-cap-topdown-hiring.png" alt="Tops-down planning — Americas level with 2 scenarios configured" style="width:100%;border-radius:4px;border:1px solid #e2e8f0;">
            <figcaption style="font-size:0.78rem;color:#6b7280;margin-top:0.35rem;text-align:center;">Page 1.2.2: Tops-Down — Americas guardrail level with Base and Conservative scenarios</figcaption>
          </figure>
        </div>
      </div>

      <!-- CAP MINI-LAB 5 -->
      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">C5</div>
          <div class="mini-lab-title">Bottoms-Up Planning — Page 1.2.4</div>
          <div class="mini-lab-duration">⏱ 8 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Configure the tactical hiring plan layer — where planners enter month-by-month hires, constrained by the tops-down NTE.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Navigate to <strong>Page 1.2.4: GTM Bottom-Up Hiring Plan Guided Setup</strong>.</li>
            <li><span class="mini-lab-step-num">2</span> Set bottoms-up entry level → <strong>Territory</strong>.</li>
            <li><span class="mini-lab-step-num">3</span> Set approval level → <strong>Region</strong> (plans submitted at territory, approved at region).</li>
            <li><span class="mini-lab-step-num">4</span> Leave OWP connection disabled for this exercise.</li>
            <li><span class="mini-lab-step-num">5</span> Click <strong>Apply / Calculate</strong>.</li>
          </ol>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ What it should look like when complete</div>
          <figure class="screenshot" style="margin:0;">
            <img src="../img/day2/11-cap-config-bottoms-up.png" alt="Bottoms-up planning — territory entry level with region approval configured" style="width:100%;border-radius:4px;border:1px solid #e2e8f0;">
            <figcaption style="font-size:0.78rem;color:#6b7280;margin-top:0.35rem;text-align:center;">Page 1.2.4: Bottoms-Up — territory-level entry, region-level approval, OWP connection disabled</figcaption>
          </figure>
        </div>
      </div>

      <hr>

      <h2>Debrief Questions — Capacity</h2>
      <ol>
        <li>You configured coverage ratios at the Americas level. A stakeholder says EMEA needs different ratios (EMEA AEs cover fewer accounts due to relationship-based selling). How does this affect your configuration? What would you change?</li>
        <li>CloudWorks's revenue targets are provided at sub-region level by account segment. You learned this requires post-generation routing work. What's the risk if you don't flag this clearly during configuration? How would you communicate it?</li>
        <li>You configured 2 scenarios (base + conservative). Sales leadership now wants a 3rd scenario (stretch/optimistic). Is this a configuration change or a post-gen setup? What's the effort?</li>
        <li>A customer's ramp profile shows new AEs at 0% in Month 1 and 20% in Month 2. Their Finance team insists on using a simpler model: full quota from Month 3. How does this difference affect your capacity calculations over a 12-month planning horizon?</li>
      </ol>'''
)

# ── cap-05-post-gen.html ──────────────────────────────────────
make_page(
    'cap-05-post-gen.html',
    'Capacity Post-Generation Steps',
    'Capacity Post-Generation Steps',
    'From generation to a working Capacity Planning app',
    ['Capacity Module', '30 min'],
    '''      <p>Capacity post-gen is comparable to Segmentation in complexity — simpler than T&amp;Q but with some specific validation steps around the tops-down/bottoms-up connection and ramp profile loading.</p>

      <h2>Post-Gen Checklist</h2>
      <ul class="checklist">
        <li>Review generation error log (0–50 errors expected)</li>
        <li>Fix formula reference errors in Capacity spoke modules</li>
        <li>Load employee data with role hierarchy (Job Family Group → Job Family → Sales Role)</li>
        <li>Load account data with segment attribute (from Segmentation output)</li>
        <li>Configure ramp profiles per sales role</li>
        <li>Validate ramp profile calculations — spot-check: hire an AE in month 1, confirm month-2 revenue output matches profile</li>
        <li>Load coverage ratios per role per segment</li>
        <li>Run tops-down suggested headcount calculation — confirm numbers look reasonable</li>
        <li>Enter a test bottoms-up hiring plan for one region</li>
        <li>Validate revenue projection output on the "holy grail" page</li>
        <li>Demo app to customer — show the revenue gap closing as hires are added</li>
      </ul>

      <h2>Watch Out For</h2>
      <div class="two-col">
        <div class="card">
          <h3>Revenue Target Routing</h3>
          <p>If you configured revenue targets at sub-region + segment level in the configurator, you need post-gen work to route the productivity model correctly. This is the #1 source of Capacity post-gen issues — flag it early.</p>
        </div>
        <div class="card">
          <h3>Scenario Locking</h3>
          <p>Always check workflow status before making changes. Locked scenarios are read-only. If a scenario is locked unexpectedly, check who submitted it and at what level — you may need to re-open it from the tops-down section.</p>
        </div>
      </div>'''
)

# ── cap-06-model-review.html ──────────────────────────────────────
make_page(
    'cap-06-model-review.html',
    'Capacity Model Review',
    'Capacity Planning Model Review',
    'Understanding the generated Capacity model using CoModeler',
    ['Capacity Module', '30 min'],
    '''      <p>The Capacity model's complexity lives in the ramp calculation logic and the tops-down/bottoms-up connection. CoModeler is particularly useful here because the formula chains are longer than in T&amp;Q or Segmentation.</p>

      <h2>Key Capacity Modules</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Module</th><th>Purpose</th></tr></thead>
          <tbody>
            <tr><td>HC Hiring Plan</td><td>The bottoms-up hiring plan input — month-by-month by role and geo</td></tr>
            <tr><td>HC Revenue Projection</td><td>Converts headcount plan to projected revenue output via ramp profiles</td></tr>
            <tr><td>HC Tops-Down NTE</td><td>Finance guardrails — NTE ceilings per geo and role family</td></tr>
            <tr><td>HC Ramp Profile</td><td>Productivity ramp table by role — foundation of all revenue calculations</td></tr>
            <tr><td>HC Coverage Ratios</td><td>Role-to-account ratios used to calculate suggested headcount</td></tr>
          </tbody>
        </table>
      </div>

      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">A</div>
          <div class="mini-lab-title">CoModeler Lab A — Document the Hiring Plan Module</div>
          <div class="mini-lab-duration">⏱ 15 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Generate a line item dictionary for the HC Hiring Plan module to understand the inputs and outputs of the bottoms-up hiring plan.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Open the <strong>Capacity demo app</strong> in your partner workspace.</li>
            <li><span class="mini-lab-step-num">2</span> Navigate to the <strong>HC Hiring Plan</strong> module.</li>
            <li><span class="mini-lab-step-num">3</span> Open CoModeler and prompt: <em>"Generate a line item dictionary for this module. Include name, formula summary, data type, and what downstream modules depend on each line item."</em></li>
            <li><span class="mini-lab-step-num">4</span> Identify which line item represents planned new hires by month and which line item represents cumulative headcount.</li>
          </ol>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ Done when you can answer</div>
          <p style="font-size:0.88rem;color:#14532d;margin:0;">Which module reads from HC Hiring Plan to calculate projected revenue? What is the key formula that connects a hire date to a revenue contribution?</p>
        </div>
      </div>

      <div class="mini-lab">
        <div class="mini-lab-header">
          <div class="mini-lab-number">C</div>
          <div class="mini-lab-title">CoModeler Lab C — Explain the Ramp-to-Revenue Logic</div>
          <div class="mini-lab-duration">⏱ 15 min</div>
        </div>
        <div class="mini-lab-body">
          <div class="mini-lab-objective">
            <strong>Objective</strong>
            Use CoModeler to understand exactly how the ramp profile converts a hire date into a monthly revenue contribution.
          </div>
          <ol class="mini-lab-steps">
            <li><span class="mini-lab-step-num">1</span> Launch CoModeler in the Capacity app.</li>
            <li><span class="mini-lab-step-num">2</span> Ask: <em>"If I hire a Commercial AE on March 15th, and the ramp profile is 0% month 1, 30% month 2, 70% month 3, 100% month 4+, what is the projected revenue contribution for April, May, June, and July? Walk me through the exact calculation."</em></li>
            <li><span class="mini-lab-step-num">3</span> Follow up: <em>"How does the hire-date-to-ramp rule work — what is the cutoff rule for whether ramp starts in the hire month or the next month?"</em></li>
          </ol>
        </div>
        <div class="mini-lab-completion">
          <div class="mini-lab-completion-label">✅ Done when you can answer</div>
          <p style="font-size:0.88rem;color:#14532d;margin:0;">A hire on the 20th of March — does ramp start in March or April? What is the revenue impact of this decision over a 12-month planning horizon for a $1M quota AE?</p>
        </div>
      </div>'''
)

# ── cap-08-extensions.html ──────────────────────────────────────
make_page(
    'cap-08-extensions.html',
    'Capacity Common Extensions',
    'Capacity Planning Common Extensions',
    'Typical customizations and how to scope them',
    ['Capacity Module', 'Reference'],
    '''      <p>Capacity has fewer extensions than T&amp;Q but the ones that come up tend to add meaningful complexity. Most are driven by Finance wanting more granular cost modeling or Sales wanting more flexible scenario management.</p>

      <div class="table-wrap">
        <table>
          <thead><tr><th>Extension</th><th>Size</th><th>Notes</th></tr></thead>
          <tbody>
            <tr><td>Custom Ramp Profiles</td><td>S</td><td>The base app provides 3 ramp profiles. Adding more requires a new profile in the admin setup and corresponding formula updates. Common when different geos (APAC vs. EMEA) have materially different ramp times.</td></tr>
            <tr><td>Revenue Target by Product Line</td><td>M</td><td>When Finance provides separate targets for different product lines. Requires adding product dimension to the revenue target and coverage modules — significant dimensionality addition.</td></tr>
            <tr><td>OWP Integration</td><td>M–L</td><td>Connecting Anaplan Workforce Planning data (approved positions, cost data) to the Capacity hiring plan. High value for customers with mature headcount planning processes, but requires both products to be live.</td></tr>
            <tr><td>Custom Cost Modeling</td><td>M</td><td>Adding fully-loaded cost per hire (base + benefits + equipment + recruiting cost) to the financial liability analysis. Common for CFOs who want full cost-of-hire visibility, not just quota capacity.</td></tr>
            <tr><td>Additional Scenario Management</td><td>S</td><td>The configurator sets the number of scenarios at generation time. Adding scenarios post-gen requires extending the scenario list and replicating scenario logic across modules. Small effort but needs careful testing.</td></tr>
            <tr><td>Segmentation Auto-Sync</td><td>S</td><td>Automating the segment-count feed from Segmentation to Capacity coverage ratios. Currently manual export/import. An ADO pipeline makes this seamless — small setup effort once ADO is configured.</td></tr>
          </tbody>
        </table>
      </div>

      <div class="callout-tip">
        <span class="callout-label">💡 Positioning Tip</span>
        <p>The most powerful Capacity demo moment is showing a VP of Sales Finance the "holy grail" page: "Hire 2 AEs in January, 3 in April — here's exactly when you close the revenue gap." Lead with that. Everything else is detail.</p>
      </div>'''
)

# ─────────────────────────────────────────────────────────────
# PART 4: Update index.html nav and content
# ─────────────────────────────────────────────────────────────
print('\n=== PART 4: Updating index.html nav and content ===')
INDEX_PATH = os.path.join(BASE, 'index.html')
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Nav already updated in Part 1; now update the content body
# Update hero subtitle
index_html = index_html.replace(
    '<p>Territory &amp; Quota (T&amp;Q) Application Lab Guide</p>',
    '<p>Territory &amp; Quota · Account Segmentation · Capacity Planning</p>'
)

# Update the intro paragraphs
old_welcome = '''      <h2>Welcome</h2>
      <p>This lab guide accompanies the <strong>RPM Apps Technical Enablement Workshop</strong> — a hands-on, full-day session designed to equip Anaplan delivery practitioners with the knowledge and skills to confidently implement the Territory &amp; Quota (T&amp;Q) application.</p>
      <p>Use the left sidebar to navigate between sections. Start with the <a href="./docs/00-overview.html">Workshop Overview</a> to review the agenda and learning objectives, then work through each section in order.</p>'''

new_welcome = '''      <h2>Welcome</h2>
      <p>This lab guide accompanies the <strong>RPM Apps Technical Enablement Workshop</strong> — a hands-on, multi-day session designed to equip Anaplan delivery practitioners with the knowledge and skills to confidently implement the three core RPM apps: <strong>Territory &amp; Quota (T&amp;Q)</strong>, <strong>Account Segmentation &amp; Scoring</strong>, and <strong>Go-to-Market Capacity Planning</strong>.</p>
      <p>Use the left sidebar to navigate between sections. Start with the <a href="./docs/00-overview.html">Workshop Overview</a> to review the agenda and learning objectives, then work through each module in order. Each module follows the same structure: functional overview → sample data → configurator → lab → post-gen → model review → application review → extensions.</p>'''

index_html = index_html.replace(old_welcome, new_welcome)

# Replace the index-nav-grid section
old_grid_start = '      <h2>Workshop Sections</h2>\n      <div class="index-nav-grid">'
new_grid = '''      <h2>Workshop Modules</h2>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#1e3a5f;">Getting Started</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/00-overview.html">
          <div class="inc-num">Overview</div>
          <div class="inc-title">Workshop Overview</div>
          <div class="inc-desc">Agenda, objectives, prerequisites, how the apps work together</div>
        </a>
        <a class="index-nav-card" href="./docs/01-spm-overview.html">
          <div class="inc-num">Section 1</div>
          <div class="inc-title">SPM/RPM Overview</div>
          <div class="inc-desc">5 pillars, T&amp;Q positioning, key concepts</div>
        </a>
        <a class="index-nav-card" href="./docs/02-anaplan-way.html">
          <div class="inc-num">Section 2</div>
          <div class="inc-title">Anaplan Way for Apps</div>
          <div class="inc-desc">7-step implementation methodology</div>
        </a>
      </div>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#1e3a5f;">Territory &amp; Quota</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/tq-01-overview.html">
          <div class="inc-num">T&amp;Q</div>
          <div class="inc-title">Functional Overview</div>
          <div class="inc-desc">What T&amp;Q does, who uses it, planning lifecycle</div>
        </a>
        <a class="index-nav-card" href="./docs/tq-02-sample-data.html">
          <div class="inc-num">T&amp;Q</div>
          <div class="inc-title">Sample Data</div>
          <div class="inc-desc">Required data objects, field schemas, CloudWorks dataset</div>
        </a>
        <a class="index-nav-card" href="./docs/03-configurator-walkthrough.html">
          <div class="inc-num">T&amp;Q</div>
          <div class="inc-title">Configurator Review</div>
          <div class="inc-desc">All 14 configurator pages in detail</div>
        </a>
        <a class="index-nav-card" href="./docs/04-configurator-exercise.html">
          <div class="inc-num">Lab</div>
          <div class="inc-title">Lab: Configurator</div>
          <div class="inc-desc">Hands-on CloudWorks scenario lab</div>
        </a>
        <a class="index-nav-card" href="./docs/05-post-gen-steps.html">
          <div class="inc-num">T&amp;Q</div>
          <div class="inc-title">Post-Generation Steps</div>
          <div class="inc-desc">Checklist, known issues, model readiness</div>
        </a>
        <a class="index-nav-card" href="./docs/tq-06-model-review.html">
          <div class="inc-num">T&amp;Q</div>
          <div class="inc-title">Model Review</div>
          <div class="inc-desc">CoModeler labs — quota calculation, key modules</div>
        </a>
        <a class="index-nav-card" href="./docs/07-spoke-app-walkthrough.html">
          <div class="inc-num">T&amp;Q</div>
          <div class="inc-title">Application Review</div>
          <div class="inc-desc">All 8 app categories, page-by-page guide</div>
        </a>
        <a class="index-nav-card" href="./docs/08-extensions.html">
          <div class="inc-num">T&amp;Q</div>
          <div class="inc-title">Common Extensions</div>
          <div class="inc-desc">Extension catalog, sizing, discovery questions</div>
        </a>
      </div>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#1e3a5f;">Account Segmentation &amp; Scoring</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/seg-01-overview.html">
          <div class="inc-num">Seg</div>
          <div class="inc-title">Functional Overview</div>
          <div class="inc-desc">What Segmentation does, downstream impact on T&amp;Q and Capacity</div>
        </a>
        <a class="index-nav-card" href="./docs/seg-02-sample-data.html">
          <div class="inc-num">Seg</div>
          <div class="inc-title">Sample Data</div>
          <div class="inc-desc">Firmographic fields, banded attributes, CloudWorks dataset</div>
        </a>
        <a class="index-nav-card" href="./docs/10-segmentation-configurator.html">
          <div class="inc-num">Seg</div>
          <div class="inc-title">Configurator Review</div>
          <div class="inc-desc">All Segmentation configurator pages in detail</div>
        </a>
        <a class="index-nav-card" href="./docs/seg-04-lab.html">
          <div class="inc-num">Lab</div>
          <div class="inc-title">Lab: Configurator</div>
          <div class="inc-desc">CloudWorks Segmentation configurator exercise</div>
        </a>
        <a class="index-nav-card" href="./docs/seg-05-post-gen.html">
          <div class="inc-num">Seg</div>
          <div class="inc-title">Post-Generation Steps</div>
          <div class="inc-desc">Checklist, segment distribution validation</div>
        </a>
        <a class="index-nav-card" href="./docs/seg-06-model-review.html">
          <div class="inc-num">Seg</div>
          <div class="inc-title">Model Review</div>
          <div class="inc-desc">CoModeler labs — scoring logic, segment mapping</div>
        </a>
        <a class="index-nav-card" href="./docs/13-segmentation-walkthrough.html">
          <div class="inc-num">Seg</div>
          <div class="inc-title">Application Review</div>
          <div class="inc-desc">Segmentation app walkthrough, all views</div>
        </a>
        <a class="index-nav-card" href="./docs/seg-08-extensions.html">
          <div class="inc-num">Seg</div>
          <div class="inc-title">Common Extensions</div>
          <div class="inc-desc">Custom scoring, segments, wallet size methods</div>
        </a>
      </div>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#1e3a5f;">Go-to-Market Capacity Planning</h3>
      <div class="index-nav-grid">
        <a class="index-nav-card" href="./docs/cap-01-overview.html">
          <div class="inc-num">Cap</div>
          <div class="inc-title">Functional Overview</div>
          <div class="inc-desc">What Capacity does, tops-down vs. bottoms-up layers</div>
        </a>
        <a class="index-nav-card" href="./docs/cap-02-sample-data.html">
          <div class="inc-num">Cap</div>
          <div class="inc-title">Sample Data</div>
          <div class="inc-desc">Role hierarchy, ramp profile inputs, data requirements</div>
        </a>
        <a class="index-nav-card" href="./docs/11-capacity-configurator.html">
          <div class="inc-num">Cap</div>
          <div class="inc-title">Configurator Review</div>
          <div class="inc-desc">All Capacity configurator pages in detail</div>
        </a>
        <a class="index-nav-card" href="./docs/cap-04-lab.html">
          <div class="inc-num">Lab</div>
          <div class="inc-title">Lab: Configurator</div>
          <div class="inc-desc">CloudWorks Capacity configurator exercise</div>
        </a>
        <a class="index-nav-card" href="./docs/cap-05-post-gen.html">
          <div class="inc-num">Cap</div>
          <div class="inc-title">Post-Generation Steps</div>
          <div class="inc-desc">Checklist, ramp validation, scenario locking</div>
        </a>
        <a class="index-nav-card" href="./docs/cap-06-model-review.html">
          <div class="inc-num">Cap</div>
          <div class="inc-title">Model Review</div>
          <div class="inc-desc">CoModeler labs — ramp-to-revenue logic, hiring plan</div>
        </a>
        <a class="index-nav-card" href="./docs/14-capacity-walkthrough.html">
          <div class="inc-num">Cap</div>
          <div class="inc-title">Application Review</div>
          <div class="inc-desc">Capacity app walkthrough, hiring plan to revenue gap</div>
        </a>
        <a class="index-nav-card" href="./docs/cap-08-extensions.html">
          <div class="inc-num">Cap</div>
          <div class="inc-title">Common Extensions</div>
          <div class="inc-desc">Custom ramp profiles, cost modeling, OWP integration</div>
        </a>
      </div>

      <h3 style="margin-top:1.5rem;margin-bottom:0.5rem;color:#1e3a5f;">Reference</h3>
      <div class="index-nav-grid">'''

# Find the old grid section and replace
old_grid_section = index_html[index_html.find('      <h2>Workshop Sections</h2>'):index_html.find('      </div>\n\n      <div class="callout-note"')]
if old_grid_section:
    new_grid_section = new_grid + '''
        <a class="index-nav-card" href="./docs/15-whats-coming.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">What's Coming</div>
          <div class="inc-desc">Roadmap updates across T&amp;Q, Segmentation, and Capacity</div>
        </a>
        <a class="index-nav-card" href="./docs/16-qanda.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">Q&amp;A from Sessions</div>
          <div class="inc-desc">Real questions from workshop sessions with answers</div>
        </a>
        <a class="index-nav-card" href="./docs/17-resources.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">Resources &amp; Downloads</div>
          <div class="inc-desc">Data prep workbooks, exercise files, reference decks</div>
        </a>
        <a class="index-nav-card" href="./docs/18-facilitator.html">
          <div class="inc-num">Ref</div>
          <div class="inc-title">Facilitator Guide</div>
          <div class="inc-desc">Session plans, timing, facilitation tips</div>
        </a>
      </div>'''
    index_html = index_html.replace(old_grid_section, new_grid_section)

# Update the callout note
index_html = index_html.replace(
    '<p>This guide is intended for internal use by Anaplan delivery practitioners attending the RPM Apps Technical Enablement Workshop. All content, screenshots, and exercises are based on the T&amp;Q V3 application.</p>',
    '<p>This guide is intended for internal use by Anaplan delivery practitioners attending the RPM Apps Technical Enablement Workshop. Content covers T&amp;Q V2/V3, Account Segmentation, and Go-to-Market Capacity Planning.</p>'
)

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(index_html)
print('  ✅ Updated index.html content and nav')

# ─────────────────────────────────────────────────────────────
# PART 5: Verification
# ─────────────────────────────────────────────────────────────
print('\n=== PART 5: Verification ===\n')

expected_new = [
    'tq-01-overview.html', 'tq-02-sample-data.html', 'tq-06-model-review.html',
    'seg-01-overview.html', 'seg-02-sample-data.html', 'seg-04-lab.html',
    'seg-05-post-gen.html', 'seg-06-model-review.html', 'seg-08-extensions.html',
    'cap-01-overview.html', 'cap-02-sample-data.html', 'cap-04-lab.html',
    'cap-05-post-gen.html', 'cap-06-model-review.html', 'cap-08-extensions.html',
]

for f in expected_new:
    path = os.path.join(DOCS, f)
    exists = os.path.exists(path)
    size = os.path.getsize(path) if exists else 0
    print(f"{'✅' if exists and size > 500 else '❌'} {f} ({size} bytes)")

print('\nNav check — all docs files should have tq-01-overview in nav:')
files = [f for f in os.listdir(DOCS) if f.endswith('.html')]
for f in sorted(files):
    content = open(os.path.join(DOCS, f)).read()
    has_new_nav = 'tq-01-overview' in content
    print(f"{'✅' if has_new_nav else '❌'} {f}")

print('\nActive link check — each file should have exactly one active link pointing to itself:')
for f in sorted(files):
    path = os.path.join(DOCS, f)
    content = open(path).read()
    active_matches = re.findall(r'class="nav-link active" href="\./' + re.escape(f) + '"', content)
    # Also check without ./
    active_matches2 = re.findall(r'nav-link active.*?' + re.escape(f), content)
    count = len(active_matches)
    print(f"{'✅' if count == 1 else '⚠ (' + str(count) + ')'} {f} — active links to self: {count}")

print('\n=== ALL DONE ===')
