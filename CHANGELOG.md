<a name="unreleased"></a>
## [Unreleased]


<a name="0.2.2"></a>
## [0.2.2] - 2021-03-29
### feat
- add typed interfaces [f98e44d](https://github.com/fffonion/kong-pdk/commit/f98e44d75271d5daceaf00f8f011ce7efaa19865)

### fix
- correct license in setup.py ([#3](https://github.com/fffonion/kong-pdk/issues/3)) [b257c98](https://github.com/fffonion/kong-pdk/commit/b257c98298343e2911de35d89dc44c1cb0f59547)
- threading mode pipe and styles [6f73ac7](https://github.com/fffonion/kong-pdk/commit/6f73ac76c6f3fc49081ba67b62e0d9ea4547cbb1)
- enable plugin server without gevent mode [a29c4d7](https://github.com/fffonion/kong-pdk/commit/a29c4d765fb9e2dfa1a8b27fccb333864a61d529)


<a name="0.2.1"></a>
## [0.2.1] - 2021-02-24
### feat
- set friendly process title [aa59083](https://github.com/fffonion/kong-pdk/commit/aa59083e6ede0394fdf2cb25f9925a36a7cc5aae)
- multiprocessing mode [1a97d26](https://github.com/fffonion/kong-pdk/commit/1a97d26e773c399149f12bee08943821a3dd9c7b)

### fix
- disable gevent in multiprocessing and make it optional [5b6fb68](https://github.com/fffonion/kong-pdk/commit/5b6fb682d9237ebb75bc653c0536678f3efe7d67)
- chmod+x on examples [1f5905d](https://github.com/fffonion/kong-pdk/commit/1f5905dc879528c519411b2914e20e2b5236e749)


<a name="0.2.0"></a>
## [0.2.0] - 2021-02-22
### feat
- exit server if parent is dead [0ee2183](https://github.com/fffonion/kong-pdk/commit/0ee2183c5679d9cc255435ff98c82d28fbf22f5b)
- embed server in plugin [af55deb](https://github.com/fffonion/kong-pdk/commit/af55deb6d2f65a8a2be654cd4c8d7f13247869ee)

### fix
- sync with Kong 2.3 update [d42de7e](https://github.com/fffonion/kong-pdk/commit/d42de7ef9565f316890aad3132e432e6a04c77f7)

### refactor
- rename kong_pluginserver to kong_pdk [e802627](https://github.com/fffonion/kong-pdk/commit/e802627436e4b856a16e4d68b9329914f2a3a4cc)


<a name="0.1.2"></a>
## [0.1.2] - 2020-02-21
### fix
- python2 compatibility [0e4cf1c](https://github.com/fffonion/kong-pdk/commit/0e4cf1cda574db778e8152b30359e6e9927b0432)


<a name="0.1.1"></a>
## [0.1.1] - 2020-02-20

<a name="0.1.0"></a>
## 0.1.0 - 2020-01-03

[Unreleased]: https://github.com/fffonion/kong-pdk/compare/0.2.2...HEAD
[0.2.2]: https://github.com/fffonion/kong-pdk/compare/0.2.1...0.2.2
[0.2.1]: https://github.com/fffonion/kong-pdk/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/fffonion/kong-pdk/compare/0.1.2...0.2.0
[0.1.2]: https://github.com/fffonion/kong-pdk/compare/0.1.1...0.1.2
[0.1.1]: https://github.com/fffonion/kong-pdk/compare/0.1.0...0.1.1
