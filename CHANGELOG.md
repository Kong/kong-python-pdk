<a name="unreleased"></a>
## [Unreleased]


<a name="0.3.2"></a>
## [0.3.2] - 2022-10-07
### bug fixes
- add version field in PluginInfo rpc ([#79](https://github.com/Kong/kong-python-pdk/issues/79)) [132f31d](https://github.com/Kong/kong-python-pdk/commit/132f31d526ff3589ac9b93dc079adb18359519cd)


<a name="0.3.1"></a>
## [0.3.1] - 2022-06-13
### bug fixes
- plugin closure syntax correction ([#64](https://github.com/Kong/kong-python-pdk/issues/64)) [920cc26](https://github.com/Kong/kong-python-pdk/commit/920cc26acb84ac357411a5d1d7232a6a540fb9f3)
- removing upper() to allow matching of attributes ([#69](https://github.com/Kong/kong-python-pdk/issues/69)) [1997a6c](https://github.com/Kong/kong-python-pdk/commit/1997a6c9991a6bc21d96d1a7f3c0141a43e01248)
- [#50](https://github.com/Kong/kong-python-pdk/issues/50): return type of get_raw_bodys should be binary string [59ab367](https://github.com/Kong/kong-python-pdk/commit/59ab367c47a3fb56e85c90674d66749dcd4ab937)
- catch error from PDK methods ([#53](https://github.com/Kong/kong-python-pdk/issues/53)) [7f82677](https://github.com/Kong/kong-python-pdk/commit/7f82677de3560c23c6c95bfaccaba6cd302aa571)
- [#50](https://github.com/Kong/kong-python-pdk/issues/50): return type should support binary string [fdb2c9b](https://github.com/Kong/kong-python-pdk/commit/fdb2c9b51d3081cb605af056c3c49e2048061b4e)


<a name="0.3.0"></a>
## [0.3.0] - 2022-02-17
### bug fixes
- add option to use python style error handling to be consistent with style headers [39a75bd](https://github.com/Kong/kong-python-pdk/commit/39a75bd3b060dbda9aec4e84afa01ae6c3000fed)
- include correct instances list in get_status [56d7ad7](https://github.com/Kong/kong-python-pdk/commit/56d7ad762b07d780068384cc1072d3a54f373083)
- exit immediately from kong.response.{error,exit} [ba3d5fa](https://github.com/Kong/kong-python-pdk/commit/ba3d5fae2b040804b1463585641919f76390feda)


<a name="0.2.7"></a>
## [0.2.7] - 2021-08-04
### bug fixes
- correctly pass schema in embedded server [099a498](https://github.com/Kong/kong-python-pdk/commit/099a4987d06602b094274ffd523300daa7985b5a)
- no longer normalize hyphens in socket name in embedded server to keep consistent with what Kong expects [20c01da](https://github.com/Kong/kong-python-pdk/commit/20c01dae1f422e577ec107904f47a57e18788508)


<a name="0.2.6"></a>
## [0.2.6] - 2021-07-19
### bug fixes
- listener to use msgpack.Unpacker iterrator [bed56c4](https://github.com/Kong/kong-python-pdk/commit/bed56c49160d1adb0e591f69b74337ced7820dba)


<a name="0.2.5"></a>
## [0.2.5] - 2021-06-24
### bug fixes
- use .py file for type hint ([#13](https://github.com/Kong/kong-python-pdk/issues/13)) [1bf3820](https://github.com/Kong/kong-python-pdk/commit/1bf3820e316f73d6021897b5979af4826e9f34d6)


<a name="0.2.4"></a>
## [0.2.4] - 2021-06-17
### bug fixes
- check correct flags existence in dedicated server ([#10](https://github.com/Kong/kong-python-pdk/issues/10)) [b18dd45](https://github.com/Kong/kong-python-pdk/commit/b18dd458def039a6a2dad4c42baa7b55d64fe027)
- set larger listen queue size ([#9](https://github.com/Kong/kong-python-pdk/issues/9)) [a3eb340](https://github.com/Kong/kong-python-pdk/commit/a3eb3404a42a106cdc4a164ee2c12dcafab90684)


<a name="0.2.3"></a>
## [0.2.3] - 2021-05-13
### bug fixes
- display defaults on cli and print PluginServerException to warning [13991ec](https://github.com/Kong/kong-python-pdk/commit/13991ec5d6373463d847c5ef073543568c0894bb)
- skip running cleanup timer [e10c098](https://github.com/Kong/kong-python-pdk/commit/e10c098a5f4c959f6fce4fc74c3d987443e386bc)
- standarlize error on instance not found [0dfc94f](https://github.com/Kong/kong-python-pdk/commit/0dfc94f3a6cf4ffc90cd2edb8891b1264d26b27c)

### features
- add response phase ([#4](https://github.com/Kong/kong-python-pdk/issues/4)) [3aca283](https://github.com/Kong/kong-python-pdk/commit/3aca2836a63eaa6bee09c76777c8cdb39a495c39)


<a name="0.2.2"></a>
## [0.2.2] - 2021-03-29
### bug fixes
- correct license in setup.py ([#3](https://github.com/Kong/kong-python-pdk/issues/3)) [b257c98](https://github.com/Kong/kong-python-pdk/commit/b257c98298343e2911de35d89dc44c1cb0f59547)
- threading mode pipe and styles [6f73ac7](https://github.com/Kong/kong-python-pdk/commit/6f73ac76c6f3fc49081ba67b62e0d9ea4547cbb1)
- enable plugin server without gevent mode [a29c4d7](https://github.com/Kong/kong-python-pdk/commit/a29c4d765fb9e2dfa1a8b27fccb333864a61d529)

### features
- add typed interfaces [f98e44d](https://github.com/Kong/kong-python-pdk/commit/f98e44d75271d5daceaf00f8f011ce7efaa19865)


<a name="0.2.1"></a>
## [0.2.1] - 2021-02-24
### bug fixes
- disable gevent in multiprocessing and make it optional [5b6fb68](https://github.com/Kong/kong-python-pdk/commit/5b6fb682d9237ebb75bc653c0536678f3efe7d67)
- chmod+x on examples [1f5905d](https://github.com/Kong/kong-python-pdk/commit/1f5905dc879528c519411b2914e20e2b5236e749)

### features
- set friendly process title [aa59083](https://github.com/Kong/kong-python-pdk/commit/aa59083e6ede0394fdf2cb25f9925a36a7cc5aae)
- multiprocessing mode [1a97d26](https://github.com/Kong/kong-python-pdk/commit/1a97d26e773c399149f12bee08943821a3dd9c7b)


<a name="0.2.0"></a>
## [0.2.0] - 2021-02-22
### bug fixes
- sync with Kong 2.3 update [d42de7e](https://github.com/Kong/kong-python-pdk/commit/d42de7ef9565f316890aad3132e432e6a04c77f7)

### code refactoring
- rename kong_pluginserver to kong_pdk [e802627](https://github.com/Kong/kong-python-pdk/commit/e802627436e4b856a16e4d68b9329914f2a3a4cc)

### features
- exit server if parent is dead [0ee2183](https://github.com/Kong/kong-python-pdk/commit/0ee2183c5679d9cc255435ff98c82d28fbf22f5b)
- embed server in plugin [af55deb](https://github.com/Kong/kong-python-pdk/commit/af55deb6d2f65a8a2be654cd4c8d7f13247869ee)


<a name="0.1.2"></a>
## [0.1.2] - 2020-02-21
### bug fixes
- python2 compatibility [0e4cf1c](https://github.com/Kong/kong-python-pdk/commit/0e4cf1cda574db778e8152b30359e6e9927b0432)


<a name="0.1.1"></a>
## [0.1.1] - 2020-02-20

<a name="0.1.0"></a>
## 0.1.0 - 2020-01-03

[Unreleased]: https://github.com/Kong/kong-python-pdk/compare/0.3.2...HEAD
[0.3.2]: https://github.com/Kong/kong-python-pdk/compare/0.3.1...0.3.2
[0.3.1]: https://github.com/Kong/kong-python-pdk/compare/0.3.0...0.3.1
[0.3.0]: https://github.com/Kong/kong-python-pdk/compare/0.2.7...0.3.0
[0.2.7]: https://github.com/Kong/kong-python-pdk/compare/0.2.6...0.2.7
[0.2.6]: https://github.com/Kong/kong-python-pdk/compare/0.2.5...0.2.6
[0.2.5]: https://github.com/Kong/kong-python-pdk/compare/0.2.4...0.2.5
[0.2.4]: https://github.com/Kong/kong-python-pdk/compare/0.2.3...0.2.4
[0.2.3]: https://github.com/Kong/kong-python-pdk/compare/0.2.2...0.2.3
[0.2.2]: https://github.com/Kong/kong-python-pdk/compare/0.2.1...0.2.2
[0.2.1]: https://github.com/Kong/kong-python-pdk/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/Kong/kong-python-pdk/compare/0.1.2...0.2.0
[0.1.2]: https://github.com/Kong/kong-python-pdk/compare/0.1.1...0.1.2
[0.1.1]: https://github.com/Kong/kong-python-pdk/compare/0.1.0...0.1.1
