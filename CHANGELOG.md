# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [0.8] - 2022-06-01
### Added
- `INVALID_COLOR_TYPE_ERROR` error
- `COLOR_NOT_FOUND_WARNING` warning
- `BOTH_COLOR_COMPLEMENT_WARNING` warning
- `set_background` function
- `is_valid_color` function
- `color_complement` function
- `select_color` function
### Changed
- Transparent mode support for `bgcolor` parameter
- Random mode modified
- Complementary color support for `color` and `bgcolor` parameters
- `filter_color` function modified
## [0.7] - 2022-05-04
### Added
- `fill_data` function
- `random_hex_color_gen` function
- `color`,`bgcolor` and `projection` parameters random mode
### Changed
- Calculation warning added to `generate` method
- Hex color support for `color` and `bgcolor` parameters
- Test system modified
- Random mode modified
- `filter_color` function modified
- `filter_projection` function modified
- `is_same_data` function modified
- `README.md` updated
## [0.6] - 2022-04-13
### Added
- `save_params_filter` function
### Changed
- `__del__` method updated
- `message` field changed in `save_fig_file` function
- `message` field changed in `save_config_file` function
- `message` field changed in `save_data_file` function
- `message` field changed in `nft_storage_upload` function
- `depth` section added to config/data file
- `linewidth` parameter added to `plot` method
- `linewidth` parameter added to `plot_params_filter` function
- Random mode modified
- `README.md` updated
## [0.5] - 2022-03-21
### Added
- `__del__` method
- Demo notebook
### Changed
- `depth` parameter added to `nft_storage` method
- `depth` parameter added to `save_fig_buf` function
- `alpha` parameter added to `plot` method
- `alpha` parameter added to `plot_params_filter` function
- Random mode modified
- `README.md` updated
## [0.4] - 2022-01-13
### Added
- `PLOT_DATA_ERROR` error message
- `_GI_initializer` function
- `generate_params_filter` function
- `plot_params_filter` function
- `filter_size` function
- `save_config` method
- `load_config` function
- `save_config_file` function
- `samilaConfigError` class
- `samilaPlotError` class
- `filter_float` function
- Random equations mode
- `function1_str` attribute
- `function2_str` attribute
### Changed
- `README.md` updated
- `plot` section added to data file
- `edgecolor` changed to `c` in `plot` method
- `config` parameter added to GenerativeImage `__init__`
- `filter_projection` function edited
- Test system updated
### Removed
- `NO_FUNCTION_ERROR` error message
- `DATA_PARSING_ERROR` error message
- `JUST_DATA_WARNING` warning message
## [0.3] - 2021-11-10
### Added
- Discord channel
- `load_data` function
- `save_data_file` function
- `save_data` method
### Changed
- `data` parameter added to GenerativeImage `__init__`
- `depth` parameter added to `save_image` method
- `depth` parameter added to `save_fig_file` function
- `save_image` and `nft_storage` methods background bug fixed
- `README.md` updated
- Test system updated
- `Python 3.10` added to `test.yml`
## [0.2] - 2021-10-14
### Added
- `dependabot.yml`
- `requirements-splitter.py`
- `samila_help` function
- `test.py`
- `function_test.py`
- `overall_test.py`
- `nft_upload_test.py`
- `is_same_data` function
- `save_image` method
### Changed
- `dev-requirements.txt` updated
- `README.md` updated
- `__main__.py` updated
- Test system updated
- `nft_storage` method updated
## [0.1] - 2021-09-30
### Added
- `GenerativeImage` class
- `plot` method
- `generate` method
- `nft_storage` method

[Unreleased]: https://github.com/sepandhaghighi/samila/compare/v0.8...dev
[0.8]: https://github.com/sepandhaghighi/samila/compare/v0.7...v0.8
[0.7]: https://github.com/sepandhaghighi/samila/compare/v0.6...v0.7
[0.6]: https://github.com/sepandhaghighi/samila/compare/v0.5...v0.6
[0.5]: https://github.com/sepandhaghighi/samila/compare/v0.4...v0.5
[0.4]: https://github.com/sepandhaghighi/samila/compare/v0.3...v0.4
[0.3]: https://github.com/sepandhaghighi/samila/compare/v0.2...v0.3
[0.2]: https://github.com/sepandhaghighi/samila/compare/v0.1...v0.2
[0.1]: https://github.com/sepandhaghighi/samila/compare/1058677...v0.1



