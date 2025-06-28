from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserRequest(_message.Message):
    __slots__ = ("username",)
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class RepoList(_message.Message):
    __slots__ = ("repositories",)
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, repositories: _Optional[_Iterable[str]] = ...) -> None: ...
