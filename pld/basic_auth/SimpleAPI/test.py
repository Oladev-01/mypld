#!/usr/bin/env python3
"""test file"""
from api.v1.auth.auth import Auth

auth = Auth()
"""making test for the methods"""
# path is None, excluded is alr
# path is empty, excluded is alr
# path is alr, excluded is None
# path is alr, excluded is empty
# path is not in excluded
# path slash tolerance
# path is in excluded

print(auth.require_auth(None, ["/path/"])) # True
print(auth.require_auth("", ["/path/"])) # True
print(auth.require_auth("/path", None)) # True
print(auth.require_auth("/path", [])) # True
print(auth.require_auth("/stats", ["/status/"])) # True
print(auth.require_auth("/status", ["/status/"])) # False
print(auth.require_auth("/status/", ["/status/"])) # False

