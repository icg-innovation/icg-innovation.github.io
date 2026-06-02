# ICG Innovation GitHub Pages

This repository hosts the official GitHub Pages website for ICG Innovation. It serves as a central hub for showcasing our projects, initiatives, and resources.

You can visit the live site here: https://icg-innovation.github.io

## About

This site is built with [Jekyll](https://jekyllrb.com/) and uses the Cayman theme as its base design. Most content is managed as Markdown files with YAML front matter, plus a few YAML data files for reusable people, funder, and collaborator information.

## Local Development

To run this site locally:

1. Clone the repository: `git clone https://github.com/icg-innovation/icg-innovation.github.io.git`
2. Navigate to the directory: `cd icg-innovation.github.io`
3. Install Jekyll and theme dependencies: `script/bootstrap`
4. Serve the site: `script/server`
5. Open your browser to `http://localhost:4000`

You can also build the site without starting a server:

```sh
bundle exec jekyll build
```

## Adding Content

Create a branch, make the content change, run the site locally, and open a pull request. The most common content locations are:

| Content type | Where to edit | Notes |
| --- | --- | --- |
| Project pages | `_projects/*.md` | Use one Markdown file per project. See [docs/CONTRIBUTING_PROJECTS.md](docs/CONTRIBUTING_PROJECTS.md) for the full project template and image guidance. |
| Blog posts | `_posts/YYYY-MM-DD-title.markdown` | File names must start with a date. Posts appear automatically on the blog page and recent posts list. |
| Team members | `_data/team.yml` | Names used in project `authors` lists should match team member names here. |
| Funders | `_data/funders.yml` | Project `funders` values should use IDs from this file. |
| Collaborators | `_data/collaborators.yml` | Project `collaborators` values should use IDs from this file. |
| Static pages | `about/index.md`, `funding/index.md`, `projects/index.md`, `blog/index.md`, or `index.md` | Edit existing page files unless you intentionally want to add a new route. |
| Images and assets | `assets/images/` | Put project images under `assets/images/projects/<project-name>/` and reference them with root-relative paths such as `/assets/images/projects/my-project/preview.jpg`. |

### Project Pages

For a new project, create a file such as `_projects/my-project.md`:

```markdown
---
layout: project
title: "My Project"
display: true
completed: false
featured: false
summary: "One sentence describing the project."
github: https://github.com/icg-innovation/my-project
paper:
image: /assets/images/projects/my-project/preview.jpg
tags: [python, astronomy]
authors: ["Your Name"]
funders: []
collaborators: []
---

## Overview

Describe the project, who it is for, and what problem it solves.
```

Use `display: false` if the page is still a draft and should not appear in project listings.

### Blog Posts

For a new post, create a file such as `_posts/2026-05-19-my-post-title.markdown`:

```markdown
---
layout: post
title: "My Post Title"
date: 2026-05-19
author: Your Name
categories: [tutorial]
---

Write the post content here.
```

## Checking Changes

Before opening a pull request, run:

```sh
script/cibuild
```

If you changed project pages, also check `/projects/` locally to confirm the project card and detail page render as expected.
