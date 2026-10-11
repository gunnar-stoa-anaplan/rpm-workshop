// RPM Apps Workshop — Navigation, Sidebar Injection, Language Switcher

// ── Sidebar structure (single source of truth) ───────────────────────────────
// All hrefs are filenames only. Path prefix is computed at injection time
// based on whether the current page is at the site root or inside /docs/.
const SIDEBAR_SECTIONS = [
  {
    title: 'Getting Started',
    links: [
      { href: '00-overview.html',          text: 'Workshop Overview' },
      { href: '00-tenant-access.html',     text: 'Tenant Access & Prerequisites' },
      { href: '01-spm-overview.html',      text: 'SPM/RPM Overview' },
      { href: '02-anaplan-way.html',       text: 'Anaplan Way for Apps' },
    ],
  },
  {
    title: 'Territory & Quota',
    links: [
      { href: 'tq-01-overview.html',                text: 'Functional Overview' },
      { href: 'tq-02-sample-data.html',             text: 'Sample Data' },
      { href: '03-configurator-walkthrough.html',   text: 'Configurator Review' },
      { href: '04-configurator-exercise.html',      text: 'Lab: Configurator' },
      { href: '05-post-gen-steps.html',             text: 'Post-Generation Steps' },
      { href: 'tq-06-model-review.html',            text: 'Model Review' },
      { href: '07-spoke-app-walkthrough.html',      text: 'Application Review' },
      { href: '06-ado-integration.html',            text: 'Data Integration & ADO' },
      { href: '08-extensions.html',                 text: 'Common Extensions' },
      { href: 'tq-appendix-answer-key.html',        text: 'T&Q Answer Key' },
    ],
  },
  {
    title: 'Account Segmentation',
    links: [
      { href: 'seg-01-overview.html',                  text: 'Functional Overview' },
      { href: 'seg-02-sample-data.html',               text: 'Sample Data' },
      { href: '10-segmentation-configurator.html',     text: 'Configurator Review' },
      { href: 'seg-04-lab.html',                       text: 'Lab: Configurator' },
      { href: 'seg-05-post-gen.html',                  text: 'Post-Generation Steps' },
      { href: 'seg-06-model-review.html',              text: 'Model Review' },
      { href: '13-segmentation-walkthrough.html',      text: 'Application Review' },
      { href: 'seg-08-extensions.html',                text: 'Common Extensions' },
      { href: 'seg-appendix-answer-key.html',          text: 'Segmentation Answer Key' },
    ],
  },
  {
    title: 'Capacity Planning',
    links: [
      { href: 'cap-01-overview.html',                  text: 'Functional Overview' },
      { href: 'cap-02-sample-data.html',               text: 'Sample Data' },
      { href: '11-capacity-configurator.html',         text: 'Configurator Review' },
      { href: 'cap-04-lab.html',                       text: 'Lab: Configurator' },
      { href: 'cap-05-post-gen.html',                  text: 'Post-Generation Steps' },
      { href: 'cap-06-model-review.html',              text: 'Model Review' },
      { href: '14-capacity-walkthrough.html',          text: 'Application Review' },
      { href: 'cap-08-extensions.html',                text: 'Common Extensions' },
      { href: 'cap-appendix-answer-key.html',          text: 'Capacity Answer Key' },
    ],
  },
  {
    title: 'Sales Forecasting',
    links: [
      { href: 'sf-01-overview.html',        text: 'Functional Overview' },
      { href: 'sf-02-sample-data.html',     text: 'Sample Data' },
      { href: 'sf-03-deployment.html',      text: 'Deployment Model' },
      { href: 'sf-04-app-walkthrough.html', text: 'Application Review' },
      { href: 'sf-05-prediction-lab.html',  text: 'AI Prediction Lab' },
      { href: 'sf-06-extensions.html',      text: 'Common Extensions' },
    ],
  },
  {
    title: 'Reference',
    links: [
      { href: 'reference-inter-app-flows.html', text: 'Inter-App Data Flows' },
      { href: '15-whats-coming.html',           text: "What's Coming" },
      { href: '16-qanda.html',                  text: 'Q&A from Sessions' },
      { href: '17-resources.html',              text: 'Resources & Downloads' },
      { href: '19-workshop-wrap-up.html',       text: 'Workshop Wrap-up' },
    ],
  },
];

const LANG_OPTIONS = [
  { value: 'en', label: '🇺🇸 English' },
  { value: 'ja', label: '🇯🇵 日本語' },
  { value: 'es', label: '🇪🇸 Español' },
  { value: 'fr', label: '🇫🇷 Français' },
  { value: 'de', label: '🇩🇪 Deutsch' },
  { value: 'pt', label: '🇧🇷 Português' },
  { value: 'ko', label: '🇰🇷 한국어' },
  { value: 'zh', label: '🇨🇳 中文' },
];

function getLinkPrefix() {
  // Sibling-relative for pages inside /docs/, otherwise prefix with ./docs/
  return window.location.pathname.includes('/docs/') ? './' : './docs/';
}

function buildSidebarHTML() {
  const prefix = getLinkPrefix();
  const sectionsHTML = SIDEBAR_SECTIONS.map(section => {
    const linksHTML = section.links.map(link =>
      `<li><a class="nav-link" href="${prefix}${link.href}">${link.text}</a></li>`
    ).join('');
    return `<li class="nav-section-title">${section.title}</li>
      <ul class="nav-submenu">${linksHTML}</ul>`;
  }).join('');

  const langOptionsHTML = LANG_OPTIONS.map(opt =>
    `<option value="${opt.value}">${opt.label}</option>`
  ).join('');

  return `
    <div class="sidebar-header">
      <div class="sidebar-title">RPM Apps Lab Guide</div>
    </div>
    <ul class="nav-list">${sectionsHTML}</ul>
    <div class="lang-switcher">
      <span class="lang-switcher-label">🌐 Language</span>
      <select id="lang-select" class="lang-select">${langOptionsHTML}</select>
    </div>`;
}

document.addEventListener('DOMContentLoaded', function () {

  // ── Inject sidebar into placeholder ────────────────────────────────────────
  // Pages have <nav class="sidebar"></nav> as an empty placeholder.
  // (Skip injection if the nav already has content — supports legacy pages.)
  const sidebarEl = document.querySelector('nav.sidebar');
  if (sidebarEl && sidebarEl.children.length === 0) {
    sidebarEl.innerHTML = buildSidebarHTML();
  }

  // ── Mark active nav link based on current page filename ────────────────────
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href').split('/').pop();
    if (href === currentPage) {
      link.classList.add('active');
    }
  });

  // ── Collapsible nav sections ───────────────────────────────────────────────
  // Section titles act as toggles; their submenu is the following <ul class="nav-submenu">
  const sectionTitles = document.querySelectorAll('.nav-section-title');

  sectionTitles.forEach(title => {
    const submenu = title.nextElementSibling;
    if (!submenu || !submenu.classList.contains('nav-submenu')) return;

    const hasActive = submenu.querySelector('.nav-link.active');

    if (hasActive) {
      title.classList.add('open');
      submenu.style.display = 'block';
    } else {
      title.classList.remove('open');
      submenu.style.display = 'none';
    }

    title.style.cursor = 'pointer';
    title.addEventListener('click', () => {
      const isOpen = title.classList.toggle('open');
      submenu.style.display = isOpen ? 'block' : 'none';
    });
  });

  // ── Mobile hamburger toggle ────────────────────────────────────────────────
  const hamburger = document.getElementById('hamburger');
  const sidebar = document.querySelector('.sidebar');
  if (hamburger && sidebar) {
    hamburger.addEventListener('click', () => sidebar.classList.toggle('open'));
  }

  // ── Language switcher ──────────────────────────────────────────────────────
  const langSelect = document.getElementById('lang-select');
  if (langSelect) {
    const pathParts = window.location.pathname.split('/');
    const langIndex = pathParts.indexOf('docs') + 1;
    const currentLang = (langIndex > 0 && pathParts[langIndex] && pathParts[langIndex].length === 2)
      ? pathParts[langIndex]
      : 'en';
    langSelect.value = currentLang;

    langSelect.addEventListener('change', function () {
      const selectedLang = this.value;
      const currentPath = window.location.pathname;

      let newPath;
      if (selectedLang === 'en') {
        newPath = currentPath.replace(/\/docs\/[a-z]{2}\//, '/docs/');
      } else {
        if (currentPath.includes('/docs/') && !currentPath.match(/\/docs\/[a-z]{2}\//)) {
          newPath = currentPath.replace('/docs/', `/docs/${selectedLang}/`);
        } else {
          newPath = currentPath.replace(/\/docs\/[a-z]{2}\//, `/docs/${selectedLang}/`);
        }
      }
      window.location.href = newPath;
    });
  }

});
