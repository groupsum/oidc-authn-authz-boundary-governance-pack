"""Find a specification and its downstream path in the installed manifest."""

from oidc_authn_authz_boundary_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:authn-authz-boundary-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-authn-authz-boundary-contract.yaml"
