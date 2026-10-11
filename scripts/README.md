# Workshop scripts

## `sync-design-system.sh`

`rpm-apps-workshop` is the canonical home for the shared design system used by every
Anaplan partner enablement workshop. The three files under canonical ownership are:

- `css/style.css` — design tokens, layout, components (including all `.lab-*`,
  `.callout-*`, sidebar / nav / quiz / check styles)
- `js/nav.js` — sidebar injection + collapse + language switcher + mobile hamburger
- `js/lab-quiz.js` — screenshot toggle, today's-date placeholder, inline mini-quiz,
  Check My Work POST handler

### Workflow

1. Edit the canonical file(s) in this repo (`rpm-apps-workshop`).
2. Commit them here.
3. Run `scripts/sync-design-system.sh` to copy them into the working trees of
   downstream workshop repos.
4. In each downstream repo, review the `git diff`, then commit + ship with a message
   like `Sync canonical design system from rpm-apps-workshop@<sha>`.

The script never commits or pushes — it only copies bytes. You review each downstream
diff before shipping it.

### Adding a new downstream workshop

Edit the `TARGETS` array near the top of `sync-design-system.sh` to include the new
workshop's repo path.

### Why not a shared repo / submodule?

Two consumers is below the breakeven for shared-repo infrastructure. When workshop #3
comes online, promote the canonical files to a dedicated `workshop-design-system` repo
and reference it via git submodule or a curl-in-build step. Until then, byte-mirroring
plus PR review keeps drift visible without adding moving parts.
