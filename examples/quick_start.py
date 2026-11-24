"""Inspect the installed pack identity."""

from oidc_authn_authz_boundary_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:oidc-authn-authz-boundary"
print(metadata["origin"]["id"])
