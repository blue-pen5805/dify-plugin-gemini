# Dify Plugin Template

This is a template for creating a new Dify plugin. It contains the basic structure and some example code to get you started.

## Features

- Automatically install development tools
- Automatically create releases when Git tags are added

## Important Notes

- Tags must follow the format **x.y.z**
- Only one plugin is allowed per repository

## Usage

Read the [official documentation](https://docs.dify.ai/plugins/quick-start/develop-plugins).

### Create New Plugin

```bash
./dify-plugin plugin init
```

### Package Plugin

When you run this command, a file named `<AUTHOR>_<PLUGIN_NAME>_<VERSION>.difypkg` will be created.

```bash
./dify-plugin-package
```

### Create Release

When you add a Git tag, GitHub Actions will automatically create a new Release.

```bash
git tag -a x.y.z
git push origin x.y.z
```
