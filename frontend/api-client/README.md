# @honest-practice/api-client

Typed client for the Honest Practice API.

Phase 0 exports the health response type by hand. Phase 6 generates this
package from the FastAPI OpenAPI schema, and CI fails if the generated file
drifts from the schema. Do not add fetch helpers here that the generator
would overwrite. Keep hand-written code in a separate module when that day
comes.
