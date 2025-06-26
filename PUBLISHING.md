# Publishing to PyPI

This project is configured to automatically publish to PyPI when a GitHub release is created.

## Setup Requirements

### 1. PyPI Account and API Token

1. Create an account on [PyPI](https://pypi.org/)
2. Create an API token for your account at https://pypi.org/manage/account/token/
3. Add the token as a repository secret named `PYPI_API_TOKEN`

### 2. GitHub Repository Configuration

1. Go to your repository settings
2. Navigate to "Environments" and create an environment named `pypi`
3. Add the `PYPI_API_TOKEN` secret to this environment

### 3. Trusted Publishing (Recommended Alternative)

Instead of using API tokens, you can set up trusted publishing:

1. Go to your PyPI project settings
2. Navigate to "Publishing"
3. Add a new trusted publisher with:
   - Repository owner: `ikifar2012`
   - Repository name: `neosmartblue.py`
   - Workflow name: `publish.yml`
   - Environment name: `pypi`

## Publishing Process

### Automatic Publishing

1. Update the version in `pyproject.toml`
2. Commit and push your changes
3. Create a new release on GitHub:
   - Go to "Releases" in your repository
   - Click "Create a new release"
   - Create a new tag (e.g., `v0.1.0`)
   - Add release notes
   - Click "Publish release"
4. The GitHub workflow will automatically build and publish to PyPI

### Manual Version Updates

Before creating a release, update the version in `pyproject.toml`:

```toml
[project]
name = "neosmartblue.py"
version = "0.1.1"  # Update this
```

## Workflow Files

- `.github/workflows/publish.yml`: Publishes to PyPI on releases
- `.github/workflows/test.yml`: Runs tests and validation on PRs and pushes

## Testing the Build

The test workflow will run automatically on pushes and pull requests to validate:

- Package builds correctly
- Dependencies install properly
- Build artifacts are valid

You can also test the build locally:

```bash
poetry build
poetry run twine check dist/*
```
