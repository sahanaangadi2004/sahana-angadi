# Copilot Instructions for this Repository

This file gives targeted, actionable guidance for AI coding agents working in this repo (a small static HTML/CSS/JS website with a `Python/` utilities folder).

- Repo Scope: static website examples and small Python scripts.
  - Primary content: HTML files in repository root (e.g., `basic.html`, `form-validation.html`, `register-bootstrap.html`).
  - Styling: CSS files live in `css/` (`bootstrap.css`, `sample.css`).
  - Scripts: single `myscript.js` at repository root for page JS examples.
  - Extras: `website/` contains a small multi-page example (`about.html`, `login.html`, `register.html`, `reset.html`).
  - Utilities: Python examples under `Python/` (e.g., `basic.py`, `datatype.py`).

- Big picture / architecture
  - This is a collection of static example pages rather than a single packaged app. Each HTML file demonstrates a specific concept (selectors, positioning, transitions, forms).
  - There is no build tool, bundler, or package manager — treat each HTML/CSS/JS file as the canonical source.
  - CSS is shared via `css/sample.css` and `css/bootstrap.css`. Prefer editing `css/sample.css` for custom styles; `css/bootstrap.css` appears to be a local copy of Bootstrap and should be modified only if necessary.
  - The `website/` subfolder appears to be a small demo site; keep changes there isolated unless the user asks to refactor global assets.

- Developer workflows and common commands
  - Local preview (any OS / Windows PowerShell):
    - With Python (quick HTTP server):

      ```powershell
      cd "c:\Users\HP\Desktop\sahana angadi\HTML"; python -m http.server 8000
      # Open http://localhost:8000 in a browser
      ```

    - With VS Code Live Server: open the folder in VS Code and use "Open with Live Server" to preview pages with auto-reload.
  - Running Python examples:

    ```powershell
    python .\Python\basic.py
    ```

  - There are no automated tests or CI configured — don't add heavy infra without user approval.

- Project-specific conventions and patterns
  - One-file-per-concept: Many HTML files are standalone demos. When implementing fixes or examples, prefer editing the specific example file rather than changing global/shared files unless the change should be visible across examples.
  - CSS placement varies: some pages use inline or internal CSS (e.g., `internalcss.html`, `inline.html`). When modernizing or consolidating styles, move rules into `css/sample.css` and update linked references.
  - Form examples: `form-validation.html`, `register-bootstrap.html`, and `website/register.html` show different form patterns (native validation vs Bootstrap styled). Match the form style to the target file when editing (do not mix Bootstrap markup into a plain example unless updating that example).
  - JavaScript: `myscript.js` is the only top-level JS file. For page-specific scripts, prefer adding small `<script>` blocks at the bottom of the HTML file unless the user asks to create modular JS.

- Integration points and external dependencies
  - No package.json or requirements.txt present. Assume no Node or pip-managed dependencies are required.
  - `css/bootstrap.css` is a local bootstrap copy — external CDN isn't used; keep modifications consistent with that choice.
  - Images are referenced from the `images/` folder; `images/multimedia.html` is a page (not an image folder). Confirm resource paths before editing.

- Editing and PR guidance for AI agents
  - Make small, focused edits. Each PR should:
    - Explain the change goal in the description (files changed, how to verify).
    - Provide manual verification steps (open X page, check Y behavior).
  - When adding new pages, follow the existing filename conventions (lowercase, hyphen-separated, `.html` extension) and link from an appropriate index or `website/` page if requested.

- Examples and file references (be explicit)
  - To update site-wide styles: edit `css/sample.css` and verify `basic.html`, `internalcss.html`, and `cssbox.html` for regressions.
  - To fix a form example: review `form-validation.html` and `website/register.html` to understand current validation approach.
  - To add a small interactive example, prefer appending a script to `myscript.js` and adding a single `<script src="myscript.js"></script>` to the target HTML file if not already present.

- Safety and scope constraints for the agent
  - Do not add CI or package managers without explicit user consent.
  - Avoid broad refactors across many example files in a single change — this repository intentionally keeps examples isolated.
  - When running commands, use the repository root described above. Watch out for the Windows path that contains spaces: `c:\Users\HP\Desktop\sahana angadi\HTML`.

If anything in this file is unclear or you want more detail about a section (for example, example-by-example verification steps or a list of pages to check after a CSS change), tell me which area to expand and I will iterate.