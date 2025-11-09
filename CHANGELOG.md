# Changelog

All notable changes to this project will be documented in this file starting with **v2.0.0**.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `TorrentOptions` for fine grained control of torrents _(replacement for `ParamArgs`)_.
- `DelugeWebClient`:
  - Arg for `daemon_port` that defaults to **58846**.
  - Method `start_daemon`.
    - Start local daemon.
  - Method `stop_daemon`.
    - Stop local daemon.
  - Method `update_ui`.
    - Gathers detailed information to update UIs.
  - Method `add_host`.
    - Add a host to the host list.
  - Method `remove_host`.
    - Remove a host from the host list.
  - Method `edit_host`.
    - Edit a host in the host list.
  - Method `find_host_id_by_name`.
    - Find a host ID by its name.

### Changed

- Swap from **Poetry** to **uv**.
- Improved error handling.

### Removed

- `ParamArgs` _(replaced with `TorrentOptions`)_.
- Signature for `Response` has been changed:
  - Removed `id` arg.

### Fixed

- Potential error for for case insensitive enum.
