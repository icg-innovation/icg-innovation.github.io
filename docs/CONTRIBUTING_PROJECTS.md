# Contributing Projects to ICG Innovation Website

This guide will walk you through the process of adding a new project to the showcase.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Project File Structure](#project-file-structure)
3. [Front Matter Parameters](#front-matter-parameters)
4. [Adding Project Images](#adding-project-images)
5. [Adding Funders](#adding-funders)
6. [Adding Collaborators](#adding-collaborators)
7. [Project Content Sections](#project-content-sections)
8. [Testing Your Changes](#testing-your-changes)
9. [Submitting Your Changes](#submitting-your-changes)

---

## Quick Start

1. **Fork and clone** this repository
2. **Create a new markdown file** in the `_projects/` directory (e.g., `my-project.md`)
3. **Add your project images** to `assets/images/projects/my-project/`
4. **Fill in the project details** using the template below
5. **Test locally** using `bundle exec jekyll serve`
6. **Submit a pull request**

---

## Project File Structure

All project files are stored in the `_projects/` directory. Each project is a Markdown file with YAML front matter at the top.

### Basic Project Template

Create a new file: `_projects/my-project-name.md`

```markdown
---
layout: project
title: My Project Name
display: true
completed: false
featured: false
featured_order:
summary: A brief one-sentence description of what your project does
github: https://github.com/username/repo
paper: https://doi.org/10.xxxx/xxxxx
funding: Supported by the $Funding Agency$
grant: $Link to Grant$ e.g. https://gtr.ukri.org/projects?ref=GRANT_REF
image: /assets/images/projects/my-project/preview.jpg
tags: [Machine Learning, Python, Data Science]
authors: ["Your Name", "Collaborator Name"]
funders: [stfc, ukri]
collaborators: [uop, uni_southampton]
---

## Overview

Provide a detailed overview of your project here. Explain what it does, why it's important, and what problems it solves.

## Key Features

- Feature 1: Description
- Feature 2: Description
- Feature 3: Description

## Technology Stack

List the main technologies, programming languages, frameworks, and tools used:

- **Language**: Python 3.9+
- **Framework**: Django
- **Database**: PostgreSQL
- **Deployment**: Docker

## Funders & Collaborators

This section is automatically generated from the `funders` and `collaborators` fields in the front matter.

## Authors

Information about the authors is automatically pulled from the team data.
```

---

## Front Matter Parameters

The YAML front matter contains metadata about your project. Here's a detailed explanation of each parameter:

### Required Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `layout` | string | Must be `project` | `project` |
| `title` | string | The full name of your project | `SCIAMA HPC Cluster` |

### Display and Visibility Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `display` | boolean | Set to `true` to show on website, `false` to hide | `true` |
| `completed` | boolean | Set to `true` to list the project under Completed Projects | `false` |
| `featured` | boolean | Set to `true` to feature on homepage | `true` |
| `featured_order` | integer | Order of featured projects (lower = higher priority) (max 4?) | `1` |

### Content Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `summary` | string | Short one-line description (used in previews) | `High-performance computing cluster for astrophysics research` |
| `image` | string | Path to preview image | `/assets/images/projects/sciama/preview.jpg` |
| `tags` | list | Keywords/technologies (helps with searching) | `[Python, HPC, Astronomy]` |
| `authors` | list | Names matching `_data/team.yml` entries | `["Gareth Cabourn Davies", "Andy Berry"]` |

### External Links

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `github` | string | GitHub repository URL | `https://github.com/icg-innovation/project` |
| `paper` | string | DOI or paper URL | `https://doi.org/10.1234/example` |
| `funding` | string | Freeform funding description | `Supported by STFC Grant ST/Y005260/1` |
| `grant` | string | Direct link to grant information | `https://gtr.ukri.org/projects?ref=ST%2FY005260%2F1` |

### Organizations

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `funders` | list | IDs from `_data/funders.yml` | `[stfc, ukri, esa]` |
| `collaborators` | list | IDs from `_data/collaborators.yml` | `[uop, imperial, uni_southampton]` |

### Parameter Notes

- **Leave empty if not applicable**: You can leave fields blank or use `[]` for empty lists
- **Boolean values**: Use lowercase `true` or `false` without quotes
- **Lists**: Use YAML list format: `[item1, item2, item3]` or multi-line format
- **Strings with special characters**: Use quotes if your text contains colons, brackets, or other special YAML characters

---

## Adding Project Images

Project images should be stored in the `assets/images/projects/` directory.

### Image Directory Structure

```
assets/
└── images/
    └── projects/
        └── your-project-name/
            ├── preview.jpg          # Main preview image (required)
            ├── screenshot1.png      # Additional images
            ├── screenshot2.png
            └── logo.svg
```

### Image Guidelines

1. **Create a project subdirectory**: `assets/images/projects/your-project-name/`
2. **Preview image requirements**:
   - Recommended size: 1200x630px (2:1 aspect ratio)
   - Format: JPG or PNG
   - File size: Keep under 500KB for fast loading
3. **Naming convention**: Use lowercase with hyphens (e.g., `preview.jpg`, `architecture-diagram.png`)
4. **Reference in front matter**: Use the full path from the root: `/assets/images/projects/your-project-name/preview.jpg`

### Example Image Reference

```yaml
image: /assets/images/projects/dandeliion/dandeliion_large.png
```

You can also reference additional images in your project's markdown content:

```markdown
![Architecture Diagram](/assets/images/projects/my-project/architecture.png)
```

---

## Adding Funders

Funders are organizations that provide funding for your project. They are defined in `_data/funders.yml` and displayed with their logos.

### Using Existing Funders

Check `_data/funders.yml` for available funders. Current funders include:

- `ukri` - UK Research and Innovation
- `stfc` - Science and Technology Facilities Council
- `erc` - European Research Council
- `esa` - European Space Agency
- `uksa` - UK Space Agency
- `esrc` - Economic and Social Research Council
- `epsrc` - Engineering and Physical Sciences Research Council
- `TFI` - The Faraday Institution

**Add to your project:**

```yaml
funders: [stfc, ukri, esa]
```

### Adding a New Funder

If your funder is not listed, add it to `_data/funders.yml`:

```yaml
- id: new_funder_id
  name: "Full Funder Name"
  url: "https://www.funder-website.org/"
  logo: "/assets/images/logos/funder_logo.png"
  featured: false  # Set to true to display on homepage
```

**Steps:**

1. Add funder entry to `_data/funders.yml`
2. Add funder logo to `assets/images/logos/`
3. Use the `id` in your project's `funders` list

**Logo requirements:**
- Recommended format: PNG with transparent background or SVG
- Recommended size: 200-400px width
- Place in: `assets/images/logos/`

---

## Adding Collaborators

Collaborators are institutions or organizations you work with. They are defined in `_data/collaborators.yml`.

### Using Existing Collaborators

Check `_data/collaborators.yml` for available collaborators. Current collaborators include:

- `uop` - University of Portsmouth
- `imperial` - Imperial College London
- `uni_southampton` - University of Southampton
- `uni_surrey` - University of Surrey
- `uni_glasgow` - University of Glasgow
- `uni_birmingham` - University of Birmingham
- `uni_cardiff` - Cardiff University
- `uni_cambridge` - University of Cambridge
- `lancaster` - Lancaster University
- `warwick` - University of Warwick
- `helyx` - Helyx
- `space_south_central` - Space South Central

**Add to your project:**

```yaml
collaborators: [uop, imperial, uni_southampton]
```

### Adding a New Collaborator

If your collaborator is not listed, add it to `_data/collaborators.yml`:

```yaml
- id: new_collaborator_id
  name: "Institution or Organization Name"
  url: "https://www.institution-website.org/"
  logo: "/assets/images/logos/institution_logo.png"
  featured: false  # Set to true for featured collaborators
```

**Steps:**

1. Add collaborator entry to `_data/collaborators.yml`
2. Add collaborator logo to `assets/images/logos/`
3. Use the `id` in your project's `collaborators` list

**Logo requirements:**
- Same as funder logos (see above)

---

## Project Content Sections

The main body of your project file uses Markdown formatting. Here are recommended sections:

### Standard Sections

#### 1. Overview (Required)
Provide a comprehensive description of your project:
- What is the project about?
- What problem does it solve?
- Who is the target audience?
- What are the main goals?

#### 2. Key Features (Recommended)
List the main features or capabilities:
```markdown
## Key Features

- **Feature Name**: Brief description
- **Another Feature**: What it does
- **Advanced Capability**: Why it's useful
```

#### 3. Technology Stack (Recommended)
Describe the technical implementation:
```markdown
## Technology Stack

- **Language**: Python 3.9+
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **Frontend**: React with TypeScript
- **Deployment**: Docker, Kubernetes
- **Testing**: pytest, Jest
```

#### 4. Installation/Usage (Optional)
If relevant, provide instructions:
```markdown
## Getting Started

### Installation

\`\`\`bash
pip install your-project
\`\`\`

### Basic Usage

\`\`\`python
from your_project import main
main.run()
\`\`\`
```

#### 5. Results/Impact (Optional)
Share achievements, publications, or impact:
```markdown
## Results

This project has enabled:
- Analysis of 10,000+ astronomical objects
- 3 peer-reviewed publications
- Collaboration with 5 international institutions
```

#### 6. Future Work (Optional)
Outline planned developments:
```markdown
## Future Developments

- Integration with additional data sources
- Machine learning enhancements
- Real-time processing capabilities
```

### Markdown Tips

- Use `**bold**` for emphasis
- Use `*italics*` for titles or names
- Use `[link text](url)` for hyperlinks
- Use triple backticks for code blocks
- Use `![alt text](image-url)` for images
- Use `>` for blockquotes
- Use numbered lists (1., 2., 3.) or bullet points (-, *, +)

---

## Testing Your Changes

Before submitting, test your project page locally:

### 1. Install Dependencies

```bash
bundle install
```

### 2. Run Jekyll Locally

```bash
bundle exec jekyll serve
```

### 3. View Your Project

Open your browser to:
- Homepage: `http://localhost:4000`
- Projects page: `http://localhost:4000/projects/`
- Your project: `http://localhost:4000/projects/your-project-name/`

### 4. Check For Issues

- ✅ Preview image loads correctly
- ✅ All links work (GitHub, papers, grants)
- ✅ Funders and collaborators display with logos
- ✅ Author names are spelled correctly
- ✅ Tags are relevant and properly formatted
- ✅ Markdown formatting looks correct
- ✅ No YAML syntax errors

---

## Submitting Your Changes

### 1. Create a Branch

```bash
git checkout -b add-my-project
```

### 2. Add Your Files

```bash
git add _projects/my-project.md
git add assets/images/projects/my-project/
```

If you added new funders or collaborators:

```bash
git add _data/funders.yml
git add _data/collaborators.yml
git add assets/images/logos/
```

### 3. Commit Your Changes

```bash
git commit -m "Add [Project Name] to projects showcase"
```

### 4. Push to Your Fork

```bash
git push origin add-my-project
```

### 5. Create a Pull Request

1. Go to the GitHub repository
2. Click "Pull requests" → "New pull request"
3. Select your branch
4. Fill in the PR description:
   - What project are you adding?
   - Brief description of the project
   - Any special notes or dependencies

### Pull Request Checklist

- [ ] Project file created in `_projects/`
- [ ] Preview image added to `assets/images/projects/`
- [ ] All front matter fields filled in correctly
- [ ] Links tested (GitHub, papers, grants)
- [ ] New funders/collaborators added to YAML files (if applicable)
- [ ] Logos added for new funders/collaborators
- [ ] Tested locally with `bundle exec jekyll serve`
- [ ] No build errors or warnings
- [ ] Follows Markdown style guidelines
- [ ] Commit message is clear and descriptive

---

## Need Help?

If you encounter any issues or have questions:

1. **Check existing projects**: Look at files in `_projects/` for examples
2. **Review the data files**: Check `_data/funders.yml` and `_data/collaborators.yml`
3. **Open an issue**: Create a GitHub issue with your question
4. **Contact the team**: Reach out to the ICG Innovation RSE team

---

## Example Complete Project

Here's a complete example showing all parameters:

```yaml
---
layout: project
title: Gravitational Wave Detection Pipeline
display: true
featured: true
featured_order: 1
summary: Developing faster and more sensitive methods to detect and analyse gravitational waves from cosmic collisions
github: https://github.com/icg-innovation/gw-pipeline
paper: https://doi.org/10.1234/example-paper
funding: Supported by the Science and Technology Facilities Council
grant: https://gtr.ukri.org/projects?ref=ST%2FY005260%2F1
image: /assets/images/projects/gravitational-waves/preview.jpg
tags: [Gravitational Waves, Python, High-Performance Computing, LIGO]
authors: ["Gareth Cabourn Davies", "Andy Berry"]
funders: [stfc, ukri]
collaborators: [uop, uni_glasgow, uni_birmingham]
---

## Overview

Gravitational waves are ripples in spacetime caused by massive cosmic events...

## Key Features

- **Real-time Detection**: Process LIGO data streams in real-time
- **Parameter Estimation**: Accurate source parameter extraction
- **Multi-messenger Alerts**: Rapid sky localization for astronomers

## Technology Stack

- **Language**: Python 3.9+
- **Computing**: High-Performance Computing (HPC)
- **Data Processing**: NumPy, SciPy, LALSuite
- **Deployment**: SLURM on SCIAMA cluster
```

---

**Thank you for contributing to ICG Innovation!** 🚀


Disclaimer: AI Generated

Last Updated: 21st October 2025

