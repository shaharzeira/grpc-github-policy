package github.authz

default allow = false

allow if input.permissions.pull == true
allow if input.permissions.push == true
allow if input.permissions.admin == true
