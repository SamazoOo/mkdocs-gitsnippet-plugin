# About

MkDocs plugin that allow to inject snippet or all markdown content from a given remote git repository.
The goal is to show different markdowns from different projects inside a MkDocs, you put together all info across some projects.

## Installation

Install the package with pip:

```bash
pip install mkdocs-gitsnippet-plugin
```

## Configuration

Enable the plugin in your `mkdocs.yml` if **you didn't change the folder name that contain your documentation source files.** By default `docs`.

```yaml
plugins:
- gitsnippet
```

Enable the plugin in your `mkdocs.yml` if **you changed the folder name that contain your documentation source files**. By default `docs`.

```yaml
plugins:
- gitsnippet:
base_path: docs
```

> This package requires MkDocs version 0.17 or higher.

## Usage

mkdocs-gitsnippet-plugin will download the file you specify from a remote git repository, extract the section or all content and inject that into you MkDocs file at render time. It's possible to specify brunch of repository

### Snippet a section

If you want to extract a section from a remote git repository, you can add the following to your markdown in MkDocs:

```markdown
{{ gitsnippet('git@github.com:SamazoOo/mkdocs-gitsnippet-plugin.git', 'README.md', '## Installation') }}
```

### All markdown content

If you want to get all context from a markdown in a remote git repository, you can add the following to your markdown in MkDocs:

```markdown
{{ gitsnippet('git@github.com:SamazoOo/mkdocs-gitsnippet-plugin.git', 'README.md', '') }}
```

### All markdown content and specify the name of the branch

If you want to get all context from a markdown in a remote git repository and get it from development brunch, you can add the following to your markdown in MkDocs:

```markdown
{{ gitsnippet('git@github.com:SamazoOo/mkdocs-gitsnippet-plugin.git', 'README.md', '', 'development') }}
```

### Images references

If the remote file has references to images, those will also be downloaded and placed in a `_gen` folder in the mkdocs hierarchy. You will probably want to include `**/gen_` in your `.gitignore` file so you don't put those into your git repository unless you want them there.
