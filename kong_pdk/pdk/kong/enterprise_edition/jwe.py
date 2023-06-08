# AUTO GENERATED BASED ON Kong 3.4.x, DO NOT EDIT
# Original source path: kong/pdk/enterprise_edition/jwe.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class jwe():


    @staticmethod
    def decode(token: str) -> Tuple[str, str]:
        """

            This function will return a table that looks like this:
            ```
            {
              [1] = protected header (as it appears in token)
              [2] = encrypted key (as it appears in token)
              [3] = initialization vector (as it appears in token)
              [4] = ciphertext (as it appears in token)
              [5] = authentication tag (as it appears in token)
              protected = protected key (base64url decoded and json decoded)
              encrypted_key = encrypted key (base64url decoded)
              iv = initialization vector (base64url decoded)
              ciphertext = ciphertext (base64url decoded)
              tag = authentication tag (base64url decoded)
              aad = protected header (as it appears in token)
            }
            ```
            The original input can be reconstructed with:
            ```
            local token = table.concat(<decoded-table>, ".")
            ```
            If there is not exactly 5 parts in JWT token, or any decoding fails,
            the error is returned.
            @usage
            local jwe = require "kong.enterprise_edition.jwe"
            local jwt, err = jwe.decode(
              "eyJhbGciOiJFQ0RILUVTIiwiZW5jIjoiQTI1NkdDTSIsImFwdSI6Ik1lUFhUS2oyWFR1NUktYldUSFI2bXci" ..
              "LCJhcHYiOiJmUHFoa2hfNkdjVFd1SG5YWFZBclVnIiwiZXBrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYi" ..
              "LCJ4IjoiWWd3eF9NVXRLTW9NYUpNZXFhSjZjUFV1Z29oYkVVc0I1NndrRlpYRjVMNCIsInkiOiIxaEYzYzlR" ..
              "VEhELVozam1vYUp2THZwTGJqcVNaSW9KNmd4X2YtUzAtZ21RIn19..4ZrIopIhLi3LeXyE.-Ke4ofA.MI5lT" ..
              "kML5NIa-Twm-92F6Q")
            if jwt then
              print(jwt.protected.alg) -- outputs "ECDH-ES"
            end

        :parameter token: JWE encrypted JWT token
        :type token: str

        :return: A table containing JWT token parts decoded, or nil

        :rtype: str
        :return: Error message, or nil

        :rtype: str
        """
        pass

    @staticmethod
    def decrypt(key: Any, token: str) -> Tuple[str, str]:
        """

            Supported keys (`key` argument):
            * Supported key formats:
              * `JWK` (given as a `string` or `table`)
              * `PEM` (given as a `string`)
              * `DER` (given as a `string`)
            * Supported key types:
              * `RSA`
              * `EC`, supported curves:
                * `P-256`
                * `P-384`
                * `P-521`
            @usage
            local jwe = require "kong.enterprise_edition.jwe"
            local jwk = {
              kty = "EC",
              crv = "P-256",
              use = "enc",
              x   = "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
              y   = "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
              d   = "870MB6gfuTJ4HtUnUvYMyJpr5eUZNP4Bk43bVdj3eAE",
            }
            local plaintext, err = jwe.decrypt(jwk,
              "eyJhbGciOiJFQ0RILUVTIiwiZW5jIjoiQTI1NkdDTSIsImFwdSI6Ik1lUFhUS2oyWFR1NUktYldUSFI2bXci" ..
              "LCJhcHYiOiJmUHFoa2hfNkdjVFd1SG5YWFZBclVnIiwiZXBrIjp7Imt0eSI6IkVDIiwiY3J2IjoiUC0yNTYi" ..
              "LCJ4IjoiWWd3eF9NVXRLTW9NYUpNZXFhSjZjUFV1Z29oYkVVc0I1NndrRlpYRjVMNCIsInkiOiIxaEYzYzlR" ..
              "VEhELVozam1vYUp2THZwTGJqcVNaSW9KNmd4X2YtUzAtZ21RIn19..4ZrIopIhLi3LeXyE.-Ke4ofA.MI5lT" ..
              "kML5NIa-Twm-92F6Q")
            if plaintext then
              print(plaintext) -- outputs "hello"
            end

        :parameter key: Private key
        :type key: Any
        :parameter token: JWE encrypted JWT token
        :type token: str

        :return: JWT token payload in plaintext, or nil

        :rtype: str
        :return: Error message, or nil

        :rtype: str
        """
        pass

    @staticmethod
    def encrypt(alg: str, enc: str, key: Any, plaintext: str, options: Optional[table]) -> Tuple[str, str]:
        """

            Supported algorithms (`alg` argument):
            * `"RSA-OAEP"`
            * `"ECDH-ES"`
            Supported encryption algorithms (`enc` argument):
            * `"A256GCM"`
            Supported keys (`key` argument):
            * Supported key formats:
              * `JWK` (given as a `string` or `table`)
              * `PEM` (given as a `string`)
              * `DER` (given as a `string`)
            * Supported key types:
              * `RSA`
              * `EC`, supported curves:
                * `P-256`
                * `P-384`
                * `P-521`
            Supported options (`options` argument):
            * `{ zip = "DEF" }`: whether to deflate the plaintext before encrypting
            * `{ apu = <string|boolean> }`: Agreement PartyUInfo header parameter
            * `{ apv = <string|boolean> }`: Agreement PartyVInfo header parameter
            The `apu` and `apv` can also be set to `false` to prevent them from
            being auto-generated (sixteen random bytes) and added to ephemeral
            public key.
            @usage
            local jwe = require "kong.enterprise_edition.jwe"
            local jwk = {
              kty = "EC",
              crv = "P-256",
              use = "enc",
              x   = "MKBCTNIcKUSDii11ySs3526iDZ8AiTo7Tu6KPAqv7D4",
              y   = "4Etl6SRW2YiLUrN5vfvVHuhp7x8PxltmWWlbbM4IFyM",
            }
            local token, err = jwe.encrypt("ECDH-ES", "A256GCM", jwk, "hello", {
              zip = "DEF,
            })
            if token then
              print(token)
            end

        :parameter alg: Algorithm used for key management
        :type alg: str
        :parameter enc: Encryption algorithm used for content encryption
        :type enc: str
        :parameter key: Public key
        :type key: Any
        :parameter plaintext: Plaintext
        :type plaintext: str
        :parameter options: Options (optional), default: nil
        :type options: table

        :return: JWE encrypted JWT token, or nil

        :rtype: str
        :return: Error message, or nil

        :rtype: str
        """
        pass

    pass