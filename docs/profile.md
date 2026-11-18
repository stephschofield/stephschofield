# Editing the animated profile

The profile is ordinary GitHub Markdown plus local SVGs. It does not need
JavaScript, a hosted image service, credentials, or GitHub Actions.

- Edit the greeting, portrait, project descriptions, or icons in
  `src/build_profile.py`.
- Keep `README.md` image descriptions, links, and the text-only profile in sync.
- Rebuild: `python src/build_profile.py`
- Check: `python -m unittest discover -s tests -v`
- Commit the regenerated `assets/*.svg` files along with the source.

The picture elements select dedicated phone layouts below 600px and light/dark
desktop artwork. Phone SVGs include both palettes. All animations stop when the
viewer requests reduced motion, leaving the full greeting and a still portrait.
Every picture has descriptive alt text, and the expandable text-only profile
preserves selectable project descriptions and ordinary links.

The wave and typing animation come from the reference profile. Its Nim game,
issue bot, and write-enabled workflow were not imported.

See `THIRD_PARTY_NOTICES.md` for the upstream license.
