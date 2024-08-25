# Django Permissions and Groups Setup

## Overview

This project implements a permissions and groups system to control access to various parts of the application. Custom permissions are defined for the `Article` model and are managed using Django’s groups.

## Custom Permissions

The following custom permissions are defined in the `Article` model:
- `can_view`: Allows viewing articles.
- `can_create`: Allows creating new articles.
- `can_edit`: Allows editing existing articles.
- `can_delete`: Allows deleting articles.

## Groups and Permissions

The following groups and their associated permissions have been set up:

- **Editors**
  - Permissions: `can_create`, `can_edit`
  
- **Viewers**
  - Permissions: `can_view`
  
- **Admins**
  - Permissions: All permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)

## Enforcing Permissions in Views

The following decorators are used to enforce permissions in views:

- `@permission_required('app_name.can_view', raise_exception=True)`
- `@permission_required('app_name.can_create', raise_exception=True)`
- `@permissio
