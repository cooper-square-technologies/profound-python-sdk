# Changelog

## 0.13.0 (2025-12-03)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.12.0...v0.13.0)

### Features

* **api:** api update ([bf9299c](https://github.com/cooper-square-technologies/profound-python-sdk/commit/bf9299c3b9f844311dedbbc536c02db13db3100e))
* **api:** api update ([a8d74d3](https://github.com/cooper-square-technologies/profound-python-sdk/commit/a8d74d33b8cc6f4d04634e6d3e8afb25662ddc0f))


### Bug Fixes

* ensure streams are always closed ([49a5d37](https://github.com/cooper-square-technologies/profound-python-sdk/commit/49a5d37750aa6adf7f671c592e9c4a6514f98105))


### Chores

* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([0715bd2](https://github.com/cooper-square-technologies/profound-python-sdk/commit/0715bd2a8b92ff962259d6dc473563788b95d6f2))
* **docs:** use environment variables for authentication in code snippets ([426dd1c](https://github.com/cooper-square-technologies/profound-python-sdk/commit/426dd1c47cddc5e573f40c4ada52d0e58c74e37d))
* update lockfile ([1ab8506](https://github.com/cooper-square-technologies/profound-python-sdk/commit/1ab850656e13f8555453740d58c1be30d656f7be))

## 0.12.0 (2025-11-25)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.11.0...v0.12.0)

### Features

* **api:** api update ([10996e0](https://github.com/cooper-square-technologies/profound-python-sdk/commit/10996e0ad8c482f33a97195d2a7cf1f7f33ce286))
* **api:** api update ([6b1f48e](https://github.com/cooper-square-technologies/profound-python-sdk/commit/6b1f48e1a6fe0103afe327d5b79d26656add4f3f))


### Chores

* add Python 3.14 classifier and testing ([4041368](https://github.com/cooper-square-technologies/profound-python-sdk/commit/4041368c3f8987738cc3a5e5e33f5e0f7d0e27e9))

## 0.11.0 (2025-11-21)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.10.0...v0.11.0)

### Features

* **api:** added `get /v1/org/assets` ([0c82b6b](https://github.com/cooper-square-technologies/profound-python-sdk/commit/0c82b6b859c3c1099d5fec3702c6cb49d5a23aa1))

## 0.10.0 (2025-11-20)

Full Changelog: [v0.9.1...v0.10.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.9.1...v0.10.0)

### Features

* **api:** add assets endpoint ([8ec3780](https://github.com/cooper-square-technologies/profound-python-sdk/commit/8ec378015028d3d9b1ec4da7dd4a5e26f795e1a3))

## 0.9.1 (2025-11-13)

Full Changelog: [v0.9.0...v0.9.1](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.9.0...v0.9.1)

## 0.9.0 (2025-11-12)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.8.0...v0.9.0)

### Features

* **api:** api update ([47d3e50](https://github.com/cooper-square-technologies/profound-python-sdk/commit/47d3e50261b0c6554bd6ce507932dd72d138cdab))


### Bug Fixes

* **client:** close streams without requiring full consumption ([9ae7af9](https://github.com/cooper-square-technologies/profound-python-sdk/commit/9ae7af92567de6cfbe7739b2a12470b4518420f5))
* compat with Python 3.14 ([a41771d](https://github.com/cooper-square-technologies/profound-python-sdk/commit/a41771db29daa4c0f73ac248c5794eff0394f999))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([e25c18a](https://github.com/cooper-square-technologies/profound-python-sdk/commit/e25c18a3d1d954cf005ea667c1d1cc1f2ed8f08d))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([48e555a](https://github.com/cooper-square-technologies/profound-python-sdk/commit/48e555a385eacdb968e459946e53806dff35a028))
* **internal:** grammar fix (it's -&gt; its) ([8233893](https://github.com/cooper-square-technologies/profound-python-sdk/commit/82338939c32ee3997a20e30ee24aab86d97c5ec9))
* **package:** drop Python 3.8 support ([db71ed2](https://github.com/cooper-square-technologies/profound-python-sdk/commit/db71ed2ad307fb5cefba7dd30f4374c5bb94f10e))

## 0.8.0 (2025-10-28)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.7.0...v0.8.0)

### Features

* **api:** api update ([7958299](https://github.com/cooper-square-technologies/profound-python-sdk/commit/7958299a1156ad45de08e406fd0d520c32dac51c))

## 0.7.0 (2025-10-27)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.6.0...v0.7.0)

### Features

* **api:** api update ([375f64d](https://github.com/cooper-square-technologies/profound-python-sdk/commit/375f64db88b85ce558e5132e00067af6bdc4ff1f))

## 0.6.0 (2025-10-21)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([4e244ad](https://github.com/cooper-square-technologies/profound-python-sdk/commit/4e244ad88c7e6185b4a3865b3db3b83981e2a865))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([c4d4695](https://github.com/cooper-square-technologies/profound-python-sdk/commit/c4d46955efd31cff4e9d7d22bdd943b116ef5c08))

## 0.5.0 (2025-10-17)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([e0655be](https://github.com/cooper-square-technologies/profound-python-sdk/commit/e0655be0272e66cfed2a71244594557ff5599bc5))

## 0.4.0 (2025-10-15)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([186f6c4](https://github.com/cooper-square-technologies/profound-python-sdk/commit/186f6c4159e5317e67c7b2c3682c06f75243eabc))

## 0.3.0 (2025-10-15)

Full Changelog: [v0.2.1...v0.3.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.2.1...v0.3.0)

### Features

* **api:** api update ([53cac67](https://github.com/cooper-square-technologies/profound-python-sdk/commit/53cac6701202525be9cf6b1e26df6470c92c657a))
* **api:** api update ([1ac0003](https://github.com/cooper-square-technologies/profound-python-sdk/commit/1ac00030a0d587441d3748427852431d6591edbc))

## 0.2.1 (2025-10-11)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.2.0...v0.2.1)

### Chores

* **internal:** detect missing future annotations with ruff ([6089e80](https://github.com/cooper-square-technologies/profound-python-sdk/commit/6089e80afdf7d32aa06eaee1c3598620999d04fd))

## 0.2.0 (2025-10-08)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.1.0...v0.2.0)

### ⚠ BREAKING CHANGES

* **api:** move Pagination to shared models
* **api:** rename reports models

### Features

* **api:** api update ([dfc3d79](https://github.com/cooper-square-technologies/profound-python-sdk/commit/dfc3d7909d6c41534e267114514bd9b94bd0bc0a))
* **api:** manual updates ([99bf2bc](https://github.com/cooper-square-technologies/profound-python-sdk/commit/99bf2bcf8300c6bc8db63e8bfee7c9a9c4bf3bfc))
* **api:** move Pagination to shared models ([aeae55d](https://github.com/cooper-square-technologies/profound-python-sdk/commit/aeae55d2461ad5bacb206c4e887faad4a6e904fa))
* **api:** rename reports models ([435b4fb](https://github.com/cooper-square-technologies/profound-python-sdk/commit/435b4fb8f08c8e7526d58f7bc2515b9826062fc3))

## 0.1.0 (2025-10-03)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/cooper-square-technologies/profound-python-sdk/compare/v0.0.1...v0.1.0)

### Features

* **api:** api update ([2572b3c](https://github.com/cooper-square-technologies/profound-python-sdk/commit/2572b3c3be7bf6cddc832478cee783e3033065d8))
* **api:** api update ([c0c8f82](https://github.com/cooper-square-technologies/profound-python-sdk/commit/c0c8f8200192aa74cea5b419cb30f9c143f2c35a))
* **api:** api update ([50d7655](https://github.com/cooper-square-technologies/profound-python-sdk/commit/50d765510b400352beb48d3b4f93948e7d37659a))
* **api:** api update ([a9288cf](https://github.com/cooper-square-technologies/profound-python-sdk/commit/a9288cff233e74cce029f1b3985c619f954e45f6))
* **api:** manual updates ([35b9d06](https://github.com/cooper-square-technologies/profound-python-sdk/commit/35b9d06f6add37221a19f0f514f375c108e29318))
* **api:** manual updates ([10650c8](https://github.com/cooper-square-technologies/profound-python-sdk/commit/10650c803530ec140b973ea1159491ed826dd966))
* **api:** manual updates ([555ef71](https://github.com/cooper-square-technologies/profound-python-sdk/commit/555ef71c7d84621e1f60752afd5e17e8e543f631))
* **api:** manual updates ([8aeebd9](https://github.com/cooper-square-technologies/profound-python-sdk/commit/8aeebd9a655310d8f9e34fd6adad982f2bfbd09c))
* **api:** manual updates ([d2b48ca](https://github.com/cooper-square-technologies/profound-python-sdk/commit/d2b48ca9ed0bb2dc836c5bcf5c4fe72ce45b43e1))
* **api:** manual updates ([53a38b1](https://github.com/cooper-square-technologies/profound-python-sdk/commit/53a38b17411e7596a61f9cab7a8e73f058fe71fc))
* **api:** manual updates ([744b812](https://github.com/cooper-square-technologies/profound-python-sdk/commit/744b8125ebd1b2841523497416615a8f7a29a47b))
* **api:** manual updates ([a252b75](https://github.com/cooper-square-technologies/profound-python-sdk/commit/a252b75817d07c3fca801b1e14bbffa31036a088))
* **api:** manual updates ([a777a52](https://github.com/cooper-square-technologies/profound-python-sdk/commit/a777a52c3c7b98a9d5cb7a1d4269a293160ab086))
* **api:** manual updates ([59b83c0](https://github.com/cooper-square-technologies/profound-python-sdk/commit/59b83c01f5bd18d00adeeae9cad709747d1b6d03))


### Chores

* internal changes ([8298af1](https://github.com/cooper-square-technologies/profound-python-sdk/commit/8298af12a5732b34b5935aaa379d5680e25387e2))
* update SDK settings ([986fbd7](https://github.com/cooper-square-technologies/profound-python-sdk/commit/986fbd7a2732151af5e1bd49ff0a7ca610b30e8c))
* update SDK settings ([ed9b35e](https://github.com/cooper-square-technologies/profound-python-sdk/commit/ed9b35e5047fa9fac3f04c37b5e383f293e0c231))
