# Store service

The Store service takes large model loads off the request path. A client uploads a file to
it; it saves the file to S3-compatible storage and returns a URL, and Layer 1 hands that
URL to the quadstore in a SPARQL `LOAD` so the data never has to travel through the API
service twice.

- Repository: [Open-MBEE/flexo-mms-store-service](https://github.com/Open-MBEE/flexo-mms-store-service) (Kotlin, Ktor)
- Image: `openmbee/flexo-mms-store-service`
- Documentation: [Store service on ReadTheDocs](https://flexo-mms-deployment-guide.readthedocs.io/en/latest/flexo-mms-store-service/index.html)

## How a load flows

1. The client sends a load request for a branch to [Layer 1](layer1.md) with the model
   file as the body.
2. Layer 1 forwards the body to the Store service, which writes it to a bucket and
   returns its URL.
3. Layer 1 issues `LOAD <url> INTO GRAPH …` to the quadstore, which fetches the file from
   the store directly.
4. Layer 1 records the result as a commit on the branch.

The client sees only the Layer 1 endpoint; the Store service is internal to the
deployment.

## Storage

Any S3-compatible object store works. The Docker Compose stack uses
[MinIO](https://min.io/); a cluster deployment typically points at Amazon S3 or an
equivalent. The service is configured by environment variables for the endpoint, region,
bucket and credentials, alongside the JWT settings it shares with the rest of Flexo MMS.
The [deployment repository](deployment.md) supplies them for both stacks.
