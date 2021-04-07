# Splinter Lettuce Functional Tests Boilerplate

A python boilerplate for functional tests with [splinter](https://github.com/cobrateam/splinter) and [lettuce](http://lettuce.it/)

- Contains predefined steps for most interactions that can be performed on a web page (see `functional_tests/features/steps path`)
- Contains the basic configuration structure for running the tests in the chrome browser (headless or not)
- Save screenshot when a test fails
- Automatically captures javascript coverage (if the page have it)


## Requirements

 - `pip install fabric`
 - python 2.x
 - Other requirements will be installed on execution (see `conf` path) :


## Executing tests

 - `fab functional_tests:$FEATURE_PATH,%SCENARIOS_NUMBER`

None of parameters are mandatory
