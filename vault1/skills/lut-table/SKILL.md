---
name: lut-table
description: How to create/update lookup tables for optimized navigation within a codebase
---
Use md-formatted tables. These are located in repo's rootdir: `LUT.md`

Do not make these for every single facet of the codebase. It's mainly to track the location of major features.

Current entries should be kept up-to-date as the codebase evolves over time.

New features should create new entries in the LUT.

## Structure

| Spec                                                                        | Code                                                  | Purpose                       |
| --------------------------------------------------------------------------- | ----------------------------------------------------- | ----------------------------- |
| spec dir loc + line num of where feature is described in spec (if relevant) | loc of relevant code in repo + line num (if relevant) | brief desc of purpose/feature |

## Example

| Spec                     | Code                     | Purpose                 |
| ------------------------ | ------------------------ | ----------------------- |
| specs/feature_spec.md 49 | src/my_py_pkg/cli.py 145 | handler for xyz command |
